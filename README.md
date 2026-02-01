# Palindrome Checker

Single-purpose API. Stateless. Deterministic. Returns JSON only.

## Endpoints
- GET `/health`
- GET `/v1/is-palindrome?text=`

## Example

Request:
`/v1/is-palindrome?text=Madam%20Im%20Adam`

Response:
```json
{
  "input": "Madam Im Adam",
  "is_palindrome": true
}
