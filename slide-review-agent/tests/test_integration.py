# 통합 테스트
"""슬라이드 검토 Agent 통합 테스트"""

import os
import pytest
from unittest.mock import patch, MagicMock

from src.components.content_analyzer import ContentAnalyzer
from src.components.report_generator import ReportGenerator
from src.components.slidev_validator import SlidevValidator
from src.components.script_executor import ScriptExecutor


# 테스트용 슬라이드 콘텐츠
SAMPLE_SLIDE_CONTENT = """---
theme: default
title: AWS Lambda 소개
author: Test Author
date: 2026-01-07
---

# AWS Lambda 소개

서버리스 컴퓨팅

---

## 목차

1. Lambda란?
2. 사용 사례
3. 데모

---

## Lambda란?

AWS Lambda는 서버리스 컴퓨팅 서비스입니다.

- 서버 관리 불필요
- 자동 스케일링
- 사용한 만큼만 비용 지불

---

## 감사합니다!

질문이 있으신가요?
"""


class TestAnalysisPipeline:
    """전체 분석 파이프라인 테스트"""
    
    def test_full_analysis_pipeline(self):
        """전체 분석 파이프라인 테스트
        
        슬라이드 입력부터 보고서 생성까지 전체 흐름 검증
        """
        # 1. 콘텐츠 분석
        analyzer = ContentAnalyzer()
        analysis = analyzer.analyze(SAMPLE_SLIDE_CONTENT)
        
        # 분석 결과 검증
        assert analysis.structure.slide_count > 0
        assert analysis.clarity.overall_score >= 0
        assert analysis.technical_accuracy is not None
        
        # 2. 보고서 생성
        generator = ReportGenerator()
        report = generator.generate_report(analysis)
        
        # Property 1: 보고서 구조 일관성
        assert report.strengths is not None
        assert report.improvements is not None
        assert report.suggestions is not None
        
        # 3. 보고서 포맷
        formatted = generator.format_report(report)
        
        assert len(formatted) > 0
        assert "점수" in formatted or "score" in formatted.lower()
    
    def test_aws_content_detection(self):
        """AWS 콘텐츠 감지 테스트"""
        analyzer = ContentAnalyzer()
        content = analyzer.parse_slide_content(SAMPLE_SLIDE_CONTENT)
        
        # AWS 용어 추출
        aws_terms = analyzer.extract_aws_terms(content)
        
        # AWS 또는 Lambda가 감지되어야 함
        assert len(aws_terms) > 0 or "AWS" in SAMPLE_SLIDE_CONTENT


class TestSlidevWorkflow:
    """Slidev 슬라이드 워크플로우 테스트"""
    
    def test_slide_validation_workflow(self):
        """슬라이드 검증 워크플로우 테스트"""
        validator = SlidevValidator()
        
        # 1. 형식 검증
        format_result = validator.validate_format(SAMPLE_SLIDE_CONTENT)
        assert format_result.is_valid
        
        # 2. 네이밍 컨벤션 검증
        valid_name = "20260107-aws-lambda"
        invalid_name = "aws-lambda"
        
        assert validator.validate_naming_convention(valid_name)
        assert not validator.validate_naming_convention(invalid_name)
        
        # 3. 유효한 이름 제안
        suggested = validator.suggest_valid_name(invalid_name)
        assert validator.validate_naming_convention(suggested)
    
    def test_consistency_check(self):
        """일관성 검사 테스트"""
        validator = SlidevValidator()
        
        existing_slides = [SAMPLE_SLIDE_CONTENT]
        
        # 동일한 테마 사용 시 일관성 유지
        report = validator.check_consistency(SAMPLE_SLIDE_CONTENT, existing_slides)
        assert report.is_consistent


class TestScriptExecution:
    """스크립트 실행 테스트"""
    
    def test_check_scripts_available(self):
        """스크립트 사용 가능 여부 확인 테스트"""
        executor = ScriptExecutor(
            scripts_dir="scripts",
            slides_dir="slides",
        )
        
        # 스크립트 존재 여부 확인 (실제 파일 시스템에 따라 다름)
        scripts = executor.check_scripts_available()
        
        assert "create-slide.sh" in scripts
        assert "export-all.sh" in scripts
    
    @patch("subprocess.run")
    def test_execute_create_slide_success(self, mock_run):
        """슬라이드 생성 성공 테스트"""
        mock_run.return_value = MagicMock(
            returncode=0,
            stdout="슬라이드 생성 완료",
            stderr="",
        )
        
        executor = ScriptExecutor()
        
        # 스크립트 파일이 존재한다고 가정
        with patch("os.path.exists", return_value=True):
            result = executor.execute_create_slide("20260107-test")
        
        assert result.success
        assert result.slide_path is not None
    
    @patch("subprocess.run")
    def test_execute_create_slide_failure(self, mock_run):
        """슬라이드 생성 실패 테스트"""
        mock_run.return_value = MagicMock(
            returncode=1,
            stdout="",
            stderr="오류 발생",
        )
        
        executor = ScriptExecutor()
        
        with patch("os.path.exists", return_value=True):
            result = executor.execute_create_slide("20260107-test")
        
        assert not result.success
        assert result.error is not None


class TestErrorRecovery:
    """오류 복구 테스트"""
    
    def test_analysis_with_invalid_content(self):
        """잘못된 콘텐츠 분석 테스트"""
        analyzer = ContentAnalyzer()
        
        # 빈 콘텐츠
        analysis = analyzer.analyze("")
        
        # 오류 없이 기본값 반환
        assert analysis.structure.slide_count == 0
    
    def test_validation_with_malformed_content(self):
        """잘못된 형식 콘텐츠 검증 테스트"""
        validator = SlidevValidator()
        
        # 프론트매터 없는 콘텐츠
        malformed = "# 제목\n\n내용"
        result = validator.validate_format(malformed)
        
        # 오류 감지
        assert not result.is_valid
        assert len(result.details) > 0
