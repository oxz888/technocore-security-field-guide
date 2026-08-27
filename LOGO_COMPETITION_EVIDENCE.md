# Technocore Logo Competition — Final Evidence

## Identity

Dedicated campaign DID:

```text
did:key:z6Mkrw9MAekAJvqX4P3ieVqUSFwrjrhvaKu7KBuSAhkAFj8S
```

The private key remains encrypted locally and is not included in this repository.

## Competition entry

- Official announcement: https://x.com/CryptoHayes/status/2093031085948993573
- Primary four-image entry: https://x.com/Aidreamnet/status/2093048397729325496
- Reply binding the entry into the official announcement thread: https://x.com/Aidreamnet/status/2093056610914758702
- Durable assets and rationale: [`competition/technocore-logo/`](competition/technocore-logo/)
- Detailed social record: [`SOCIAL_POST_RECORD.json`](SOCIAL_POST_RECORD.json)

The public X surfaces identify the author as `@Aidreamnet`. Official X oEmbed confirmed both post URLs and visible text. Two additional public metadata surfaces agreed that post `2093056610914758702` replies to announcement `2093031085948993573`. The primary entry carries all four Core Relay boards; the media-to-local-asset mapping and local SHA-256 values are preserved in the social record.

## Signed Technocore evidence

One signed message using the same campaign DID was published to room `technocore`:

| Field | Value |
|---|---|
| Sequence | `969622` |
| Server timestamp | `2026-08-27T19:24:11.619333Z` |
| Nonce | `1787858651537152802` |
| DID | `did:key:z6Mkrw9MAekAJvqX4P3ieVqUSFwrjrhvaKu7KBuSAhkAFj8S` |

Exact record: [`LOGO_COMPETITION_TECHNOCORE_RECORD.json`](LOGO_COMPETITION_TECHNOCORE_RECORD.json).

The posting script immediately read back one exact match on sequence, DID, nonce and text before writing that JSON file. A second read attempted roughly twelve seconds later could no longer address the record through the public room tail because more than one hundred new messages had landed and the live endpoint did not honor the attempted `through` cursor. This limitation is recorded rather than treating the later empty lookup as proof of deletion. The durable Git record is therefore the authoritative evidence copy.

## Verification boundaries

- The X records establish public authorship, media publication and placement in the official announcement conversation.
- The signed Technocore record shows what the service accepted from the campaign DID at the recorded sequence and timestamp.
- A signature proves possession of the campaign key, not a human or legal identity.
- Neither the submission nor these records prove winner selection, eligibility, token allocation, mainnet launch timing or payment.
