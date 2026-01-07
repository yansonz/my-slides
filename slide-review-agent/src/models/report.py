# 보고서 데이터 모델
"""검토 보고서 관련 데이터 모델"""

from dataclasses import dataclass, field
from typing import Literal


@dataclass
class Suggestion:
    """개선 제안"""
    priority: Literal["high", "medium", "low"]
    description: str
    reason: str
    example: str


@dataclass
class ReviewReport:
    """검토 보고서"""
    strengths: list[str] = field(default_factory=list)
    improvements: list[str] = field(default_factory=list)
    suggestions: list[Suggestion] = field(default_factory=list)
    overall_score: int = 0  # 0-100
