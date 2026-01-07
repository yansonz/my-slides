# 데이터 모델
"""슬라이드 검토 Agent 데이터 모델"""

from .slide import SlideContent, Slide, SlideMetadata
from .analysis import (
    Analysis,
    StructureAnalysis,
    ClarityScore,
    ClarityIssue,
    TechnicalValidation,
    ValidationResult,
)
from .report import ReviewReport, Suggestion

__all__ = [
    "SlideContent",
    "Slide",
    "SlideMetadata",
    "Analysis",
    "StructureAnalysis",
    "ClarityScore",
    "ClarityIssue",
    "TechnicalValidation",
    "ValidationResult",
    "ReviewReport",
    "Suggestion",
]
