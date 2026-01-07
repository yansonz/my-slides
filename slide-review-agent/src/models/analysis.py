# 분석 데이터 모델
"""슬라이드 분석 관련 데이터 모델"""

from dataclasses import dataclass, field


@dataclass
class StructureAnalysis:
    """슬라이드 구조 분석 결과"""
    slide_count: int = 0
    has_introduction: bool = False
    has_conclusion: bool = False
    logical_flow: int = 0  # 0-100


@dataclass
class ClarityIssue:
    """명확성 문제"""
    slide_index: int
    issue: str
    suggestion: str


@dataclass
class ClarityScore:
    """명확성 점수"""
    overall_score: int = 0  # 0-100
    issues: list[ClarityIssue] = field(default_factory=list)


@dataclass
class TechnicalValidation:
    """기술적 검증 결과"""
    is_valid: bool = True
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


@dataclass
class ValidationResult:
    """검증 결과"""
    is_valid: bool = True
    details: list[str] = field(default_factory=list)


@dataclass
class Analysis:
    """전체 분석 결과"""
    structure: StructureAnalysis = field(default_factory=StructureAnalysis)
    clarity: ClarityScore = field(default_factory=ClarityScore)
    technical_accuracy: TechnicalValidation = field(default_factory=TechnicalValidation)
    aws_validation: ValidationResult = field(default_factory=ValidationResult)
    slidev_compliance: ValidationResult = field(default_factory=ValidationResult)
