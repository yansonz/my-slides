# 컴포넌트 테스트
"""슬라이드 검토 Agent 컴포넌트 테스트"""

import pytest
from src.components.content_analyzer import ContentAnalyzer
from src.components.report_generator import ReportGenerator
from src.components.slide_generator import SlideGenerator
from src.components.slidev_validator import SlidevValidator
from src.components.error_handler import ErrorHandler, ErrorType, ErrorContext


# 테스트용 슬라이드 콘텐츠
SAMPLE_SLIDE_CONTENT = """---
theme: default
title: Docker 기초
author: Test Author
date: 2026-01-07
---

# Docker 기초

컨테이너 기술 소개

---

## 목차

1. Docker란?
2. 컨테이너 vs VM
3. 기본 명령어

---

## Docker란?

Docker는 컨테이너 기반 가상화 플랫폼입니다.

- 경량화된 가상화
- 빠른 배포
- 일관된 환경

---

## 감사합니다!

질문이 있으신가요?
"""


class TestContentAnalyzer:
    """ContentAnalyzer 테스트"""
    
    def test_parse_slide_content(self):
        """슬라이드 콘텐츠 파싱 테스트"""
        analyzer = ContentAnalyzer()
        content = analyzer.parse_slide_content(SAMPLE_SLIDE_CONTENT)
        
        assert content.title == "Docker 기초"
        assert content.metadata.author == "Test Author"
        assert content.metadata.theme == "default"
        assert len(content.slides) > 0
    
    def test_analyze_structure(self):
        """구조 분석 테스트"""
        analyzer = ContentAnalyzer()
        content = analyzer.parse_slide_content(SAMPLE_SLIDE_CONTENT)
        structure = analyzer.analyze_structure(content)
        
        assert structure.slide_count > 0
        assert structure.has_introduction  # 목차가 있음
        assert structure.has_conclusion  # 감사합니다가 있음
        assert structure.logical_flow >= 50
    
    def test_evaluate_clarity(self):
        """명확성 평가 테스트"""
        analyzer = ContentAnalyzer()
        content = analyzer.parse_slide_content(SAMPLE_SLIDE_CONTENT)
        clarity = analyzer.evaluate_clarity(content)
        
        assert clarity.overall_score >= 0
        assert clarity.overall_score <= 100
    
    def test_analyze(self):
        """전체 분석 테스트"""
        analyzer = ContentAnalyzer()
        analysis = analyzer.analyze(SAMPLE_SLIDE_CONTENT)
        
        assert analysis.structure is not None
        assert analysis.clarity is not None
        assert analysis.technical_accuracy is not None


class TestReportGenerator:
    """ReportGenerator 테스트"""
    
    def test_generate_report(self):
        """보고서 생성 테스트"""
        analyzer = ContentAnalyzer()
        generator = ReportGenerator()
        
        analysis = analyzer.analyze(SAMPLE_SLIDE_CONTENT)
        report = generator.generate_report(analysis)
        
        # Property 1: 보고서 구조 일관성
        assert report.strengths is not None
        assert report.improvements is not None
        assert report.suggestions is not None
        assert isinstance(report.strengths, list)
        assert isinstance(report.improvements, list)
        assert isinstance(report.suggestions, list)
    
    def test_format_report(self):
        """보고서 포맷 테스트"""
        analyzer = ContentAnalyzer()
        generator = ReportGenerator()
        
        analysis = analyzer.analyze(SAMPLE_SLIDE_CONTENT)
        report = generator.generate_report(analysis)
        formatted = generator.format_report(report)
        
        assert "강점" in formatted or "Strengths" in formatted
        assert "개선" in formatted or "Improvements" in formatted
        assert "제안" in formatted or "Suggestions" in formatted


class TestSlideGenerator:
    """SlideGenerator 테스트"""
    
    def test_generate_template(self):
        """템플릿 생성 테스트"""
        generator = SlideGenerator()
        template = generator.generate_template("Docker 기초")
        
        # Property 3: Slidev 형식 보존
        assert "---" in template
        assert "theme:" in template
        assert "title:" in template
    
    def test_generate_slide_name(self):
        """슬라이드 이름 생성 테스트"""
        generator = SlideGenerator()
        name = generator.generate_slide_name("Docker 기초")
        
        # Property 4: 네이밍 컨벤션 준수
        assert len(name) > 8
        assert name[8] == "-"
        assert name[:8].isdigit()


class TestSlidevValidator:
    """SlidevValidator 테스트"""
    
    def test_validate_format(self):
        """형식 검증 테스트"""
        validator = SlidevValidator()
        result = validator.validate_format(SAMPLE_SLIDE_CONTENT)
        
        assert result.is_valid
        assert len(result.details) > 0
    
    def test_validate_naming_convention_valid(self):
        """유효한 네이밍 컨벤션 테스트"""
        validator = SlidevValidator()
        
        assert validator.validate_naming_convention("20260107-docker-basics")
        assert validator.validate_naming_convention("20251231-my-presentation")
    
    def test_validate_naming_convention_invalid(self):
        """유효하지 않은 네이밍 컨벤션 테스트"""
        validator = SlidevValidator()
        
        assert not validator.validate_naming_convention("docker-basics")
        assert not validator.validate_naming_convention("my-presentation")
        assert not validator.validate_naming_convention("2026010-docker")  # 날짜 7자리
    
    def test_suggest_valid_name(self):
        """유효한 이름 제안 테스트"""
        validator = SlidevValidator()
        suggested = validator.suggest_valid_name("my-presentation")
        
        # Property 4: 네이밍 컨벤션 준수
        assert validator.validate_naming_convention(suggested)


class TestErrorHandler:
    """ErrorHandler 테스트"""
    
    def test_handle_aws_mcp_error(self):
        """AWS MCP 오류 처리 테스트"""
        handler = ErrorHandler()
        context = ErrorContext(
            error_type=ErrorType.AWS_MCP_ERROR,
            message="Connection failed",
        )
        result = handler.handle_error(context)
        
        # Property 8: 오류 처리 복원력
        assert result.handled
        assert result.message is not None
        assert len(result.suggestions) > 0
    
    def test_handle_script_error(self):
        """스크립트 오류 처리 테스트"""
        handler = ErrorHandler()
        context = ErrorContext(
            error_type=ErrorType.SCRIPT_ERROR,
            message="Script not found",
        )
        result = handler.handle_error(context)
        
        assert result.handled
        assert "스크립트" in result.message
    
    def test_format_error_message(self):
        """오류 메시지 포맷 테스트"""
        handler = ErrorHandler()
        context = ErrorContext(
            error_type=ErrorType.FORMAT_ERROR,
            message="Invalid format",
        )
        result = handler.handle_error(context)
        formatted = handler.format_error_message(result)
        
        assert "⚠️" in formatted
        assert "제안" in formatted or "💡" in formatted
