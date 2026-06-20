"""Mapper for Arbeitnow API job records."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from market_intelligence.models.job_posting import RawJobPosting


def map_arbeitnow_job(record: dict[str, Any]) -> RawJobPosting:
    """Convert one Arbeitnow API record into the project data contract."""

    created_at = record.get("created_at")

    posted_at = (
        datetime.fromtimestamp(created_at, tz=timezone.utc)
        if isinstance(created_at, int | float)
        else None
    )

    return RawJobPosting(
        platform="arbeitnow",
        source_job_id=record["slug"],
        source_url=record["url"],
        market_segment="remote_work",
        posted_at=posted_at,
        title=record["title"],
        description=record["description"],
        is_remote=record.get("remote"),
        raw_payload=record,
    )
