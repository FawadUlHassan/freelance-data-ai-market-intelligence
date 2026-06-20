# Data and AI Relevance Filter

## Purpose

The relevance filter determines whether a source job posting belongs in the
project's Data, BI, Data Engineering, Data Science, AI, or business-automation
market-intelligence dataset.

## Decision Classes

| Decision | Meaning | Treatment |
|---|---|---|
| accepted | Clearly relevant to the project scope | Eligible for the analytical dataset |
| needs_review | Potentially relevant but ambiguous | Requires manual review before counting toward the target |
| rejected | Not relevant to the project scope | Excluded from the analytical dataset |

## Explainable Rule-Based Baseline

The first classifier is intentionally rule-based and fully explainable.

| Evidence | Score |
|---|---:|
| High-signal term in job title | 3 |
| High-signal term in description | 2 |
| Supporting term anywhere | 1 |

### Thresholds

- Score 3 or greater: `accepted`
- Score 1 or 2: `needs_review`
- Score 0: `rejected`

## Examples

| Title | Expected decision | Why |
|---|---|---|
| Data Analyst | accepted | High-signal title term |
| Build a Power BI dashboard | accepted | High-signal BI and dashboard evidence |
| Excel reporting assistant | needs_review | Supporting evidence only |
| Artist Manager | rejected | No Data/AI relevance evidence |

## Governance Rules

1. Only accepted records count toward source quotas.
2. Needs-review records must be reviewed before inclusion.
3. Every decision must retain score, matched terms and explanation.
4. The taxonomy is version-controlled in `config/relevance_taxonomy.yml`.
5. The rule-based output will later become a baseline for AI-assisted classification.
