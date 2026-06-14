# Data Dictionary

## Raw Job Posting Contract

**Grain:** One record per job posting returned by a permitted source.

| Field | Type | Required | Description |
|---|---|---:|---|
| platform | Text | Yes | Source platform name |
| source_job_id | Text | Yes | Job identifier supplied by the source |
| source_url | URL | Yes | Original source URL |
| market_segment | Category | Yes | freelance, remote_work, or employment |
| collected_at | Timestamp | Yes | UTC pipeline collection timestamp |
| posted_at | Timestamp | No | Original publication timestamp |
| title | Text | Yes | Original job title |
| description | Text | Yes | Original job description |
| engagement_type | Category | Yes | fixed, hourly, salary, or unknown |
| experience_level | Category | Yes | entry, intermediate, expert, or unknown |
| currency_code | Text | No | ISO-style three-letter currency code |
| budget_min | Decimal | No | Minimum fixed-price budget |
| budget_max | Decimal | No | Maximum fixed-price budget |
| hourly_rate_min | Decimal | No | Minimum hourly rate |
| hourly_rate_max | Decimal | No | Maximum hourly rate |
| client_country | Text | No | Client or employer country |
| language_code | Text | No | Two-letter detected language code |
| raw_payload | JSON object | Yes | Original permitted API fields |

## Initial Validation Rules

1. Platform and source job ID must not be empty.
2. Source URL must be valid.
3. Title must contain at least three characters.
4. Description must contain at least twenty characters.
5. Currency must use a three-letter uppercase code.
6. Monetary values cannot be negative.
7. Minimum values cannot exceed maximum values.
8. Unexpected fields are rejected.
9. Personal client contact data is not part of the approved contract.
