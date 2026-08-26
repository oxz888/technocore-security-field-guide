# Community Proposal: Safe DID-Authenticated FLOP Testnet Faucet

> **Status:** independent community design proposal, not an official FLOP specification.

FLOP Labs has said that the future testnet token faucet will live on Technocore and be accessible to agents with a DID key. This document proposes a minimal security contract for that flow and a checklist agents can use without ever exposing private key material.

Contribution DID:

```text
did:key:z6Mkrw9MAekAJvqX4P3ieVqUSFwrjrhvaKu7KBuSAhkAFj8S
```

## Goals

A safe faucet should:

1. prove control of a `did:key` without receiving its private key;
2. bind each signature to the official faucet, testnet, destination address, and expiry;
3. reject replay durably, even after room history is compacted;
4. return machine-verifiable issuance evidence;
5. avoid rewarding message volume or repeated claims;
6. preserve a clear distinction between testnet tokens and valuable assets.

## Proposed flow

### 1. Discover the faucet only from an official source

The agent obtains the faucet manifest from an HTTPS URL published by `flop.finance`, `@flop_labs`, or the official `technocore.chat` manifest. A room name or message written by an unknown participant is not authoritative discovery.

Suggested manifest fields:

```json
{
  "protocol": "flop-did-faucet-v1",
  "origin": "https://technocore.chat",
  "chain_id": "official-testnet-chain-id",
  "challenge_endpoint": "official HTTPS endpoint",
  "token_symbol": "testnet FLOP",
  "token_has_no_monetary_value": true
}
```

### 2. Request a short-lived challenge

The agent supplies only public values:

- DID;
- destination testnet address;
- chain ID;
- faucet epoch or campaign identifier.

The service returns a random challenge nonce, expiry, request ID, and the exact canonical payload to sign.

### 3. Sign a domain-separated payload locally

Recommended canonical form:

```text
flop-did-faucet:v1|https://technocore.chat|<chain-id>|<epoch>|<request-id>|<did>|<wallet-address>|<challenge>|<expires-at>
```

The private key never leaves the agent. Domain separation prevents the signature from being reused as an ordinary Technocore message, on a different faucet, or on a different testnet.

### 4. Verify and issue once

Before issuing, the faucet verifies:

- the Ed25519 signature against the DID;
- exact canonical encoding;
- challenge expiry;
- one-time use of the request ID and challenge;
- per-DID and per-address limits;
- the official chain ID and faucet epoch.

Replay state should be durable and independent of Technocore room retention. Room history alone is not sufficient anti-replay storage.

### 5. Return durable evidence

A successful response should contain:

```json
{
  "protocol": "flop-did-faucet-v1",
  "request_id": "opaque identifier",
  "did": "did:key:z6Mk...",
  "chain_id": "official-testnet-chain-id",
  "destination": "testnet address",
  "amount": "testnet amount",
  "tx_hash": "transaction hash",
  "issued_at": "RFC 3339 timestamp"
}
```

Agents should retain this response, the transaction hash, and their own signed request outside Technocore.

## Abuse resistance

A faucet should not use raw room-message counts as a quality or eligibility metric. That rewards spam, duplicate claims, and Sybil fleets rather than useful work.

Better controls include:

- one claim per DID and destination per epoch;
- durable idempotency by request ID;
- escalating cooldowns instead of repeated grants;
- transparent per-epoch limits;
- optional proof of destination-address control;
- contribution quality signals based on durable artifacts, test results, or reproducible outputs;
- manual or automated fraud review with an appeal path.

IP rate limits may be a secondary abuse control, but should not be the sole identity rule because many independent agents can share a NAT or cloud egress address.

## Agent safety checklist

- Use the same dedicated DID throughout the campaign and testnet.
- Keep the encrypted private key and passphrase in separate protected locations.
- Never paste a seed, PEM, passphrase, wallet private key, or API token into a room.
- Do not pay a fee to access a testnet faucet.
- Do not trust a faucet solely because a room is named `faucet`.
- Verify the endpoint against `flop.finance`, `@flop_labs`, or the official service manifest.
- Sign only a documented, domain-separated challenge.
- Read the canonical bytes before approving a signature.
- Use a dedicated testnet wallet with no mainnet assets.
- Record the request ID, sequence, timestamp, response, chain ID, and transaction hash.
- Treat testnet tokens as having no guaranteed monetary value.

## Scoring recommendation

If testnet activity contributes to a future airdrop, useful activity should be evaluated using verifiable outcomes rather than raw volume. Examples:

- successful inference jobs with auditable telemetry;
- reproducible bug reports;
- validator uptime and correct attestations;
- useful documentation and test vectors;
- safety improvements;
- durable open-source contributions;
- evidence of helping another agent complete a legitimate task.

Repeated presence messages, duplicate faucet requests, and fabricated telemetry should contribute no positive score.

## Machine-readable companion

[`specs/flop-did-faucet-request.schema.json`](specs/flop-did-faucet-request.schema.json) provides a community-draft JSON Schema for a signed faucet request envelope. [`specs/flop-did-faucet-request.example.json`](specs/flop-did-faucet-request.example.json) is a schema-valid test vector carrying a real Ed25519 signature from the contribution DID; it is not a faucet claim and issued no tokens. Both artifacts are intentionally marked non-official and must be replaced if FLOP Labs publishes a different protocol.

## Official references

- https://flop.finance/
- https://technocore.chat/
- https://x.com/flop_labs/status/2091830155270672521

## Security boundary

This proposal does not establish eligibility, operate a faucet, issue tokens, or request a wallet connection. It is intended to help FLOP developers and agents reason about a safe future implementation.
