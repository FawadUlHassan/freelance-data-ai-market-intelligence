# Sampling Plan

## Objective

Collect approximately 1,000 valid and unique job postings for market
intelligence analysis covering freelance Data and AI services and an adjacent
remote-employment comparison cohort.

## Analytical Populations

The project separates two populations:

1. Freelance demand: clients purchasing project-based services.
2. Remote employment demand: employers hiring staff or contractors.

These populations will not be combined without retaining the market segment.

## Provisional Source Allocation

| Source | Market segment | Target |
|---|---|---:|
| Freelancer | Freelance | 500 |
| Upwork | Freelance | 200 |
| RemoteOK | Remote work | 150 |
| Arbeitnow | Remote work | 150 |
| Total | | 1,000 |

The Upwork quota is conditional on approved API access. If approval is not
received, its records will be replaced using another formally approved source.

## Sampling Method

The initial project uses a time-bounded observational sample.

Records will be collected through repeated incremental runs rather than one
large one-time pull. Each collection run will retain its timestamp, source,
search group, returned-record count, accepted-record count and rejection count.

## Search Groups

The following search groups define the market scope:

1. Data analysis and reporting
2. Excel and spreadsheet automation
3. SQL and databases
4. Business intelligence and dashboards
5. Python and pandas
6. Data cleaning and transformation
7. ETL and data pipelines
8. Data engineering
9. Analytics engineering
10. Statistics and forecasting
11. Machine learning
12. NLP and text analytics
13. Generative AI
14. RAG and vector databases
15. AI and business-process automation
16. Telecom, VoIP and CDR analytics

## Inclusion Rules

A record is eligible when:

- It represents a real job, project or contract opportunity.
- It was obtained using an approved collection method.
- Its title or description relates to at least one search group.
- It has a source identifier or stable source URL.
- It passes the job-posting data contract.
- It is not classified as a duplicate.

## Exclusion Rules

Exclude:

- Freelancer service profiles or seller advertisements
- Training courses
- Affiliate advertisements
- Unpaid internships unless intentionally analyzed
- Records without enough content for classification
- Duplicate or reposted records
- Private contact information
- Records collected through unapproved methods

## Bias Controls

- Preserve the source and market segment for every record.
- Report source-level and combined KPIs separately.
- Do not treat remote employment jobs as freelance projects.
- Record query/search group with each collection.
- Distinguish organic records from strategic oversampling.
- Do not claim platform-wide market share from the sample.
- Use median rather than mean for highly skewed budgets.
- Report missing-value rates for financial fields.

## Completion Criteria

Collection is complete when:

- Approximately 1,000 valid unique records are available.
- At least 650 records represent freelance demand.
- Every active source has passed compliance review.
- Duplicate and rejection statistics are documented.
- Each record can be traced to a collection run.

## Relevance Classification

Every collected record must pass the Data and AI relevance filter before it
counts toward a source target.

- `accepted`: counts toward the target;
- `needs_review`: retained for manual review but does not count automatically;
- `rejected`: excluded from the analytical dataset.

The initial classifier is transparent and rule-based. It records a score,
matched terms and a decision explanation for every evaluated record.
