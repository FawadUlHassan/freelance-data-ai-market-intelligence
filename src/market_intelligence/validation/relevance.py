"""Explainable relevance classification for Data and AI job opportunities."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, Field

Decision = Literal["accepted", "needs_review", "rejected"]


class RelevanceResult(BaseModel):
    """Result of explainable job relevance classification."""

    decision: Decision
    score: int = Field(ge=0)
    title_matches: list[str]
    description_matches: list[str]
    supporting_matches: list[str]
    reason: str


def _normalize_text(value: str) -> str:
    """Normalize text for phrase matching."""

    normalized = value.lower()
    normalized = re.sub(r"[_/\\-]+", " ", normalized)
    return re.sub(r"\s+", " ", normalized).strip()


def _find_terms(text: str, terms: list[str]) -> list[str]:
    """Return configured terms found as complete words or phrases."""

    matches: list[str] = []

    for term in terms:
        pattern = rf"(?<!\w){re.escape(term)}(?!\w)"

        if re.search(pattern, text):
            matches.append(term)

    return matches


def classify_job_relevance(
    title: str,
    description: str,
    taxonomy_path: Path = Path("config/relevance_taxonomy.yml"),
) -> RelevanceResult:
    """Classify a job against the project Data and AI relevance taxonomy."""

    taxonomy = yaml.safe_load(taxonomy_path.read_text(encoding="utf-8"))

    configuration = taxonomy["classification"]
    high_signal_terms = taxonomy["high_signal_terms"]
    supporting_terms = taxonomy["supporting_terms"]

    normalized_title = _normalize_text(title)
    normalized_description = _normalize_text(description)
    combined_text = f"{normalized_title} {normalized_description}"

    title_matches = _find_terms(normalized_title, high_signal_terms)
    description_matches = _find_terms(normalized_description, high_signal_terms)
    supporting_matches = _find_terms(combined_text, supporting_terms)

    score = 3 * len(title_matches) + 2 * len(description_matches) + len(supporting_matches)

    if score >= configuration["accepted_score_threshold"]:
        decision: Decision = "accepted"
        reason = "Clear Data/AI relevance based on high-signal evidence."
    elif score >= configuration["review_score_threshold"]:
        decision = "needs_review"
        reason = "Potential relevance found, but evidence is insufficient for automatic acceptance."
    else:
        decision = "rejected"
        reason = "No configured Data/AI relevance evidence was found."

    return RelevanceResult(
        decision=decision,
        score=score,
        title_matches=title_matches,
        description_matches=description_matches,
        supporting_matches=supporting_matches,
        reason=reason,
    )
