"""Data contracts for freelance and remote-work job postings."""

from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, model_validator

MarketSegment = Literal["freelance", "remote_work", "employment"]
EngagementType = Literal["fixed", "hourly", "salary", "unknown"]
ExperienceLevel = Literal["entry", "intermediate", "expert", "unknown"]


class RawJobPosting(BaseModel):
    """Validated representation of a job posting received from a source."""

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )

    platform: str = Field(min_length=2, max_length=50)
    source_job_id: str = Field(min_length=1, max_length=200)
    source_url: HttpUrl

    market_segment: MarketSegment

    collected_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    posted_at: datetime | None = None

    title: str = Field(min_length=3, max_length=500)
    description: str = Field(min_length=20)

    engagement_type: EngagementType = "unknown"
    experience_level: ExperienceLevel = "unknown"
    is_remote: bool | None = None

    currency_code: str | None = Field(
        default=None,
        pattern=r"^[A-Z]{3}$",
    )

    budget_min: Decimal | None = Field(default=None, ge=0)
    budget_max: Decimal | None = Field(default=None, ge=0)

    hourly_rate_min: Decimal | None = Field(default=None, ge=0)
    hourly_rate_max: Decimal | None = Field(default=None, ge=0)

    client_country: str | None = Field(default=None, max_length=100)
    language_code: str | None = Field(
        default=None,
        pattern=r"^[a-z]{2}$",
    )

    raw_payload: dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def validate_commercial_ranges(self) -> RawJobPosting:
        """Ensure minimum commercial values do not exceed maximum values."""

        if (
            self.budget_min is not None
            and self.budget_max is not None
            and self.budget_min > self.budget_max
        ):
            raise ValueError("budget_min cannot exceed budget_max")

        if (
            self.hourly_rate_min is not None
            and self.hourly_rate_max is not None
            and self.hourly_rate_min > self.hourly_rate_max
        ):
            raise ValueError("hourly_rate_min cannot exceed hourly_rate_max")

        return self
