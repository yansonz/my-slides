# 보고서 생성 모듈
"""검토 보고서 생성 컴포넌트"""

from typing import Literal

from ..models.analysis import Analysis
from ..models.report import ReviewReport, Suggestion


class ReportGenerator:
    """검토 보고서 생성기"""
    
    def __init__(self):
        """생성기 초기화"""
        pass
    
    def _identify_strengths(self, analysis: Analysis) -> list[str]:
        """강점 식별
        
        Args:
            analysis: 분석 결과
        
        Returns:
            강점 목록
        """
        strengths = []
        
        # 구조 관련 강점
        if analysis.structure.has_introduction:
            strengths.append("명확한 도입부가 있습니다")
        if analysis.structure.has_conclusion:
            strengths.append("적절한 결론/마무리가 있습니다")
        if 5 <= analysis.structure.slide_count <= 12:
            strengths.append(f"적절한 슬라이드 수 ({analysis.structure.slide_count}개)")
        if analysis.structure.logical_flow >= 80:
            strengths.append("논리적 흐름이 우수합니다")
        
        # 명확성 관련 강점
        if analysis.clarity.overall_score >= 90:
            strengths.append("전반적인 명확성이 매우 우수합니다")
        elif analysis.clarity.overall_score >= 75:
            strengths.append("전반적인 명확성이 양호합니다")
        
        # 기술적 정확성 관련 강점
        if analysis.technical_accuracy.is_valid and not analysis.technical_accuracy.errors:
            strengths.append("기술적 오류가 발견되지 않았습니다")
        
        # Slidev 형식 관련 강점
        if analysis.slidev_compliance.is_valid:
            strengths.append("Slidev 형식을 올바르게 따르고 있습니다")
        
        return strengths if strengths else ["분석 완료"]
    
    def _identify_improvements(self, analysis: Analysis) -> list[str]:
        """개선 사항 식별
        
        Args:
            analysis: 분석 결과
        
        Returns:
            개선 사항 목록
        """
        improvements = []
        
        # 구조 관련 개선 사항
        if not analysis.structure.has_introduction:
            improvements.append("도입부/개요 슬라이드 추가 권장")
        if not analysis.structure.has_conclusion:
            improvements.append("결론/마무리 슬라이드 추가 권장")
        if analysis.structure.slide_count < 3:
            improvements.append("슬라이드 수가 너무 적습니다")
        elif analysis.structure.slide_count > 20:
            improvements.append("슬라이드 수가 너무 많습니다 - 핵심 내용으로 압축 권장")
        if analysis.structure.logical_flow < 60:
            improvements.append("논리적 흐름 개선 필요")
        
        # 명확성 관련 개선 사항
        if analysis.clarity.overall_score < 70:
            improvements.append("전반적인 명확성 개선 필요")
        
        # 명확성 이슈 추가
        for issue in analysis.clarity.issues[:3]:  # 상위 3개만
            improvements.append(f"슬라이드 {issue.slide_index + 1}: {issue.issue}")
        
        # 기술적 정확성 관련 개선 사항
        for error in analysis.technical_accuracy.errors:
            improvements.append(f"기술적 오류: {error}")
        for warning in analysis.technical_accuracy.warnings[:2]:  # 상위 2개만
            improvements.append(f"주의: {warning}")
        
        return improvements
    
    def _generate_suggestions(self, analysis: Analysis) -> list[Suggestion]:
        """구체적 제안 생성
        
        Args:
            analysis: 분석 결과
        
        Returns:
            제안 목록
        """
        suggestions = []
        
        # 구조 관련 제안
        if not analysis.structure.has_introduction:
            suggestions.append(Suggestion(
                priority="high",
                description="도입부 슬라이드 추가",
                reason="청중이 발표 내용을 미리 파악할 수 있도록 도입부가 필요합니다",
                example="## 목차\n\n1. 소개\n2. 주요 내용\n3. 데모\n4. 결론",
            ))
        
        if not analysis.structure.has_conclusion:
            suggestions.append(Suggestion(
                priority="high",
                description="결론 슬라이드 추가",
                reason="발표 내용을 요약하고 마무리하는 슬라이드가 필요합니다",
                example="## 감사합니다!\n\n질문이 있으신가요?\n\n📧 email@example.com",
            ))
        
        # 명확성 관련 제안
        for issue in analysis.clarity.issues:
            priority: Literal["high", "medium", "low"] = "medium"
            if "제목이 없습니다" in issue.issue:
                priority = "high"
            elif "너무 깁니다" in issue.issue:
                priority = "medium"
            else:
                priority = "low"
            
            suggestions.append(Suggestion(
                priority=priority,
                description=f"슬라이드 {issue.slide_index + 1} 개선",
                reason=issue.issue,
                example=issue.suggestion,
            ))
        
        # 기술적 정확성 관련 제안
        for warning in analysis.technical_accuracy.warnings:
            if "AWS" in warning:
                suggestions.append(Suggestion(
                    priority="medium",
                    description="AWS 정보 검증",
                    reason=warning,
                    example="AWS 공식 문서를 참조하여 정확성을 확인하세요",
                ))
        
        # 우선순위별 정렬
        priority_order = {"high": 0, "medium": 1, "low": 2}
        suggestions.sort(key=lambda s: priority_order[s.priority])
        
        return suggestions
    
    def _calculate_overall_score(self, analysis: Analysis) -> int:
        """전체 점수 계산
        
        Args:
            analysis: 분석 결과
        
        Returns:
            전체 점수 (0-100)
        """
        # 가중치 적용
        structure_weight = 0.3
        clarity_weight = 0.4
        technical_weight = 0.2
        compliance_weight = 0.1
        
        # 구조 점수
        structure_score = analysis.structure.logical_flow
        
        # 명확성 점수
        clarity_score = analysis.clarity.overall_score
        
        # 기술적 정확성 점수
        technical_score = 100 if analysis.technical_accuracy.is_valid else 70
        technical_score -= len(analysis.technical_accuracy.errors) * 10
        technical_score -= len(analysis.technical_accuracy.warnings) * 5
        technical_score = max(0, technical_score)
        
        # Slidev 준수 점수
        compliance_score = 100 if analysis.slidev_compliance.is_valid else 50
        
        # 가중 평균
        overall = (
            structure_score * structure_weight +
            clarity_score * clarity_weight +
            technical_score * technical_weight +
            compliance_score * compliance_weight
        )
        
        return int(overall)
    
    def generate_report(self, analysis: Analysis) -> ReviewReport:
        """검토 보고서 생성
        
        Args:
            analysis: 분석 결과
        
        Returns:
            검토 보고서
        """
        return ReviewReport(
            strengths=self._identify_strengths(analysis),
            improvements=self._identify_improvements(analysis),
            suggestions=self._generate_suggestions(analysis),
            overall_score=self._calculate_overall_score(analysis),
        )
    
    def format_report(self, report: ReviewReport) -> str:
        """보고서를 문자열로 포맷
        
        Args:
            report: 검토 보고서
        
        Returns:
            포맷된 보고서 문자열
        """
        lines = []
        
        # 헤더
        lines.append("# 슬라이드 검토 보고서")
        lines.append("")
        lines.append(f"**전체 점수: {report.overall_score}/100**")
        lines.append("")
        
        # 강점
        lines.append("## 강점 (Strengths)")
        for strength in report.strengths:
            lines.append(f"- ✓ {strength}")
        lines.append("")
        
        # 개선 사항
        lines.append("## 개선 사항 (Improvements)")
        if report.improvements:
            for improvement in report.improvements:
                lines.append(f"- ⚠ {improvement}")
        else:
            lines.append("- 특별한 개선 사항이 없습니다")
        lines.append("")
        
        # 구체적 제안
        lines.append("## 구체적 제안 (Suggestions)")
        if report.suggestions:
            for i, suggestion in enumerate(report.suggestions, 1):
                priority_emoji = {"high": "🔴", "medium": "🟡", "low": "🟢"}
                lines.append(f"### {i}. {suggestion.description} {priority_emoji[suggestion.priority]}")
                lines.append(f"**이유:** {suggestion.reason}")
                lines.append(f"**예시:**")
                lines.append(f"```")
                lines.append(suggestion.example)
                lines.append(f"```")
                lines.append("")
        else:
            lines.append("- 추가 제안 사항이 없습니다")
        
        return "\n".join(lines)
