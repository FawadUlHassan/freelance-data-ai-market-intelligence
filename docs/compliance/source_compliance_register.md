# Source Compliance Register

This register records the access and publication decision for every potential
data source. A source cannot be enabled until its review is complete.

| Source | Proposed method | Access status | Compliance status | Current decision |
|---|---|---|---|---|
| Freelancer | Official API | Not configured | Pending review | Do not collect yet |
| Upwork | Official OAuth API | Approval required | Restricted | Do not collect yet |
| RemoteOK | Public JSON feed | Available | Terms review pending | Do not collect yet |
| Arbeitnow | Public API | Test approved | Bulk collection pending | Schema test approved; do not bulk collect yet |
| LinkedIn | Automated collection | Not approved | Prohibited for project | Excluded |
| Indeed | Automated collection | Not approved | Unclear/restricted | Excluded |
| Fiverr | Seller/service listings | Not assessed | Separate population | Future supply analysis |

## Approval Checklist

Before enabling a source, record:

- [ ] Official access method identified
- [ ] Authentication requirements documented
- [ ] Terms and usage restrictions reviewed
- [ ] Rate limits documented
- [ ] Permitted storage duration reviewed
- [ ] Publication restrictions reviewed
- [ ] Personal-data fields excluded
- [ ] Test request completed
- [ ] Response schema documented
- [ ] Collector approved for activation

## Publication Policy

The public GitHub repository may contain:

- Collection and transformation code
- Schemas and data contracts
- Aggregated statistics
- Sanitized sample records
- Data-quality results
- Dashboard screenshots

The public repository will not contain:

- API credentials
- Personal contact information
- Full restricted datasets
- Raw job descriptions where redistribution is not confirmed
- Data obtained through prohibited automation
