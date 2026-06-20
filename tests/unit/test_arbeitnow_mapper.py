"""Tests for Arbeitnow job-record mapping."""

from datetime import datetime, timezone

from market_intelligence.collectors.arbeitnow import map_arbeitnow_job

ARBEITNOW_RECORD = {
    "slug": "data-analyst-berlin-1001",
    "title": "Data Analyst",
    "company_name": "Example Company",
    "location": "Berlin",
    "remote": True,
    "tags": ["Data", "SQL", "Python"],
    "job_types": ["Full Time"],
    "created_at": 1781940646,
    "url": "https://www.arbeitnow.com/jobs/example/data-analyst-berlin-1001",
    "description": (
        "The company requires a data analyst with SQL, Python, "
        "dashboarding, and stakeholder communication skills."
    ),
}


def test_arbeitnow_record_maps_to_project_contract() -> None:
    job = map_arbeitnow_job(ARBEITNOW_RECORD)

    assert job.platform == "arbeitnow"
    assert job.source_job_id == "data-analyst-berlin-1001"
    assert job.market_segment == "remote_work"
    assert job.is_remote is True
    assert job.client_country is None
    assert job.posted_at == datetime.fromtimestamp(
        1781940646,
        tz=timezone.utc,
    )
    assert job.raw_payload["company_name"] == "Example Company"
