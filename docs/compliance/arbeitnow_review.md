# Arbeitnow Source Review

## Source

- **Source:** Arbeitnow
- **Market segment:** Remote work / employment comparison cohort
- **Collection method:** Official public job-search API
- **Authentication:** No API key required
- **Initial review date:** 2026-06-20

## Official API Information

The official API page states that the free job-search API:

- requires no API key;
- returns job data in a consistent format;
- includes a `remote` field;
- supports a `visa_sponsorship` filter.

## Terms Considered

The API terms require a link back to Arbeitnow.com and state that permission
to use the API may be revoked.

The general site terms restrict copying and public display of website materials.
Therefore, the project will avoid publishing raw job descriptions or complete
source datasets.

## Approved Uses

- Read-only API schema inspection
- Small educational test retrievals
- Internal analytical processing
- Aggregated reporting with source attribution
- Sanitized examples that do not reproduce full job descriptions

## Prohibited Uses

- Scraping HTML pages
- Republishing full source job descriptions
- Republishing the complete raw dataset
- Creating a competing job board
- Bypassing rate limits or access controls
- Collecting personal contact information

## Current Decision

**Status: Test approved; bulk collection pending schema inspection and collector
validation.**

## Required Attribution

Any dashboard, report, or public portfolio page using Arbeitnow-derived
aggregates must include:

> Data source: Arbeitnow — https://www.arbeitnow.com

## Next Review Trigger

Reassess this decision before:

1. Bulk collection begins.
2. Any raw-data retention policy changes.
3. Public dashboard publication.
4. Any commercial use of the dataset.
