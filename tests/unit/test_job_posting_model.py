"""Tests for the job-posting data contract."""

from decimal import Decimal

import pytest
from pydantic import ValidationError

from market_intelligence.models.job_posting import RawJobPosting

VALID_JOB = {
    "platform": "freelancer",
    "source_job_id": "job-1001",
    "source_url": "https://example.com/jobs/job-1001",
    "market_segment": "freelance",
    "title": "Build a Power BI Sales Dashboard",
    "description": (
        "The client requires an interactive Power BI dashboard for sales and financial analysis."
    ),
    "engagement_type": "fixed",
    "experience_level": "intermediate",
    "currency_code": "USD",
    "budget_min": "300",
    "budget_max": "600",
    "client_country": "United States",
    "language_code": "en",
}


def test_valid_job_posting_is_accepted() -> None:
    job = RawJobPosting(**VALID_JOB)

    assert job.platform == "freelancer"
    assert job.budget_min == Decimal("300")
    assert job.budget_max == Decimal("600")


def test_reversed_budget_range_is_rejected() -> None:
    invalid_job = {
        **VALID_JOB,
        "budget_min": "800",
        "budget_max": "500",
    }

    with pytest.raises(
        ValidationError,
        match="budget_min cannot exceed budget_max",
    ):
        RawJobPosting(**invalid_job)


def test_invalid_currency_code_is_rejected() -> None:
    invalid_job = {
        **VALID_JOB,
        "currency_code": "US Dollars",
    }

    with pytest.raises(ValidationError):
        RawJobPosting(**invalid_job)


def test_negative_budget_is_rejected() -> None:
    invalid_job = {
        **VALID_JOB,
        "budget_min": "-50",
    }

    with pytest.raises(ValidationError):
        RawJobPosting(**invalid_job)


def test_unexpected_fields_are_rejected() -> None:
    invalid_job = {
        **VALID_JOB,
        "private_client_email": "client@example.com",
    }

    with pytest.raises(ValidationError):
        RawJobPosting(**invalid_job)
