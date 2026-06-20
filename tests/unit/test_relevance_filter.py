"""Tests for the explainable Data and AI relevance filter."""

from market_intelligence.validation.relevance import classify_job_relevance


def test_data_analyst_title_is_accepted() -> None:
    result = classify_job_relevance(
        title="Data Analyst",
        description="Prepare recurring commercial reports for senior management.",
    )

    assert result.decision == "accepted"
    assert result.score >= 3
    assert "data analyst" in result.title_matches


def test_power_bi_dashboard_job_is_accepted() -> None:
    result = classify_job_relevance(
        title="Build an executive reporting solution",
        description=(
            "Create a Power BI sales dashboard using SQL, Python, and stakeholder requirements."
        ),
    )

    assert result.decision == "accepted"
    assert "power bi" in result.description_matches
    assert "sql" in result.description_matches


def test_excel_only_job_needs_review() -> None:
    result = classify_job_relevance(
        title="Office reporting assistant",
        description="Improve Excel spreadsheets and produce monthly reports.",
    )

    assert result.decision == "needs_review"
    assert result.score == 2
    assert "excel" in result.supporting_matches
    assert "reporting" in result.supporting_matches


def test_unrelated_artist_manager_job_is_rejected() -> None:
    result = classify_job_relevance(
        title="Artist Manager / Influencer Manager",
        description=(
            "Manage artist relationships, influencer campaigns, "
            "brand communication, and marketing activity."
        ),
    )

    assert result.decision == "rejected"
    assert result.score == 0


def test_relevance_result_includes_explanation() -> None:
    result = classify_job_relevance(
        title="SQL consultant",
        description="Support database reporting.",
    )

    assert result.decision == "accepted"
    assert result.reason
    assert "sql" in result.title_matches
