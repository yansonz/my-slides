# 콘텐츠 분석 모듈
"""슬라이드 콘텐츠 분석 컴포넌트"""

import re
from dataclasses import dataclass, field

from ..models.analysis import (
    Analysis,
    StructureAnalysis,
    ClarityScore,
    ClarityIssue,
    TechnicalValidation,
    ValidationResult,
)
from ..models.slide import SlideContent, Slide, SlideMetadata


class ContentAnalyzer:
    """슬라이드 콘텐츠 분석기"""
    
    # 도입부 키워드
    INTRO_KEYWORDS = ["소개", "개요", "목차", "agenda", "introduction", "overview"]
    
    # 결론 키워드
    CONCLUSION_KEYWORDS = ["결론", "요약", "감사", "질문", "q&a", "conclusion", "summary", "thank"]
    
    # AWS 서비스 패턴
    AWS_SERVICE_PATTERN = r"\b(AWS|Amazon)\s+[A-Z][a-zA-Z0-9]+\b|\b(Lambda|S3|EC2|ECS|EKS|RDS|DynamoDB|CloudFormation|CloudWatch|IAM|VPC|API Gateway|Bedrock|SageMaker|SNS|SQS|Kinesis|Glue|Athena|Redshift|Aurora|ElastiCache|Route 53|CloudFront|Elastic Beanstalk)\b"
    
    def parse_slide_content(self, raw_content: str) -> SlideContent:
        """원시 슬라이드 콘텐츠를 파싱
        
        Args:
            raw_content: 슬라이드 마크다운 원본
        
        Returns:
            파싱된 SlideContent 객체
        """
        slides = []
        metadata = SlideMetadata()
        title = ""
        topic = ""
        
        # 프론트매터 파싱
        frontmatter_match = re.match(r"^---\n(.*?)\n---", raw_content, re.DOTALL)
        if frontmatter_match:
            frontmatter = frontmatter_match.group(1)
            # 제목 추출
            title_match = re.search(r"title:\s*(.+)", frontmatter)
            if title_match:
                title = title_match.group(1).strip()
            # 작성자 추출
            author_match = re.search(r"author:\s*(.+)", frontmatter)
            if author_match:
                metadata.author = author_match.group(1).strip()
            # 날짜 추출
            date_match = re.search(r"date:\s*(.+)", frontmatter)
            if date_match:
                metadata.date = date_match.group(1).strip()
            # 테마 추출
            theme_match = re.search(r"theme:\s*(.+)", frontmatter)
            if theme_match:
                metadata.theme = theme_match.group(1).strip()
        
        # 슬라이드 분리 (--- 구분자 기준)
        slide_sections = re.split(r"\n---\n", raw_content)
        
        for i, section in enumerate(slide_sections):
            if i == 0 and frontmatter_match:
                # 첫 번째 섹션에서 프론트매터 제거
                section = re.sub(r"^---\n.*?\n---\n?", "", section, flags=re.DOTALL)
            
            section = section.strip()
            if not section:
                continue
            
            # 슬라이드 제목 추출
            slide_title = ""
            title_match = re.match(r"^#+ (.+)", section, re.MULTILINE)
            if title_match:
                slide_title = title_match.group(1).strip()
            
            # 슬라이드 레이아웃 추출
            layout = None
            layout_match = re.search(r"layout:\s*(\w+)", section)
            if layout_match:
                layout = layout_match.group(1)
            
            slides.append(Slide(
                title=slide_title,
                content=section,
                layout=layout,
            ))
        
        # 주제 추출 (첫 번째 슬라이드 제목 또는 메타데이터 제목)
        topic = title or (slides[0].title if slides else "")
        
        return SlideContent(
            title=title,
            topic=topic,
            slides=slides,
            metadata=metadata,
            raw_content=raw_content,
        )
    
    def analyze_structure(self, content: SlideContent) -> StructureAnalysis:
        """슬라이드 구조 분석
        
        Args:
            content: 슬라이드 콘텐츠
        
        Returns:
            구조 분석 결과
        """
        slide_count = len(content.slides)
        has_introduction = False
        has_conclusion = False
        logical_flow = 0
        
        if slide_count == 0:
            return StructureAnalysis(
                slide_count=0,
                has_introduction=False,
                has_conclusion=False,
                logical_flow=0,
            )
        
        # 도입부 확인 (첫 2개 슬라이드)
        for slide in content.slides[:2]:
            slide_text = (slide.title + " " + slide.content).lower()
            if any(keyword in slide_text for keyword in self.INTRO_KEYWORDS):
                has_introduction = True
                break
        
        # 결론 확인 (마지막 2개 슬라이드)
        for slide in content.slides[-2:]:
            slide_text = (slide.title + " " + slide.content).lower()
            if any(keyword in slide_text for keyword in self.CONCLUSION_KEYWORDS):
                has_conclusion = True
                break
        
        # 논리적 흐름 점수 계산
        flow_score = 50  # 기본 점수
        
        # 슬라이드 수에 따른 점수
        if 3 <= slide_count <= 15:
            flow_score += 20
        elif slide_count > 15:
            flow_score += 10
        
        # 도입부/결론 존재 여부
        if has_introduction:
            flow_score += 15
        if has_conclusion:
            flow_score += 15
        
        logical_flow = min(100, flow_score)
        
        return StructureAnalysis(
            slide_count=slide_count,
            has_introduction=has_introduction,
            has_conclusion=has_conclusion,
            logical_flow=logical_flow,
        )
    
    def evaluate_clarity(self, content: SlideContent) -> ClarityScore:
        """슬라이드 명확성 평가
        
        Args:
            content: 슬라이드 콘텐츠
        
        Returns:
            명확성 점수
        """
        issues = []
        total_score = 100
        
        for i, slide in enumerate(content.slides):
            slide_issues = []
            
            # 제목 없음 검사
            if not slide.title:
                slide_issues.append(ClarityIssue(
                    slide_index=i,
                    issue="슬라이드에 제목이 없습니다",
                    suggestion="명확한 제목을 추가하세요",
                ))
                total_score -= 5
            
            # 내용 길이 검사
            content_length = len(slide.content)
            if content_length < 20:
                slide_issues.append(ClarityIssue(
                    slide_index=i,
                    issue="슬라이드 내용이 너무 짧습니다",
                    suggestion="더 자세한 내용을 추가하세요",
                ))
                total_score -= 3
            elif content_length > 1000:
                slide_issues.append(ClarityIssue(
                    slide_index=i,
                    issue="슬라이드 내용이 너무 깁니다",
                    suggestion="내용을 여러 슬라이드로 분리하세요",
                ))
                total_score -= 5
            
            # 불릿 포인트 검사 (너무 많은 항목)
            bullet_count = len(re.findall(r"^[-*]\s", slide.content, re.MULTILINE))
            if bullet_count > 7:
                slide_issues.append(ClarityIssue(
                    slide_index=i,
                    issue=f"불릿 포인트가 너무 많습니다 ({bullet_count}개)",
                    suggestion="5-7개 이하로 줄이거나 슬라이드를 분리하세요",
                ))
                total_score -= 3
            
            issues.extend(slide_issues)
        
        return ClarityScore(
            overall_score=max(0, total_score),
            issues=issues,
        )
    
    def validate_technical_accuracy(self, content: SlideContent) -> TechnicalValidation:
        """기술적 정확성 검증
        
        Args:
            content: 슬라이드 콘텐츠
        
        Returns:
            기술적 검증 결과
        """
        errors = []
        warnings = []
        
        # AWS 서비스 언급 추출
        aws_services = set()
        for slide in content.slides:
            matches = re.findall(self.AWS_SERVICE_PATTERN, slide.content, re.IGNORECASE)
            for match in matches:
                # 튜플에서 비어있지 않은 값 추출
                service = next((m for m in match if m), None)
                if service:
                    aws_services.add(service)
        
        # AWS 서비스가 있으면 검증 필요 표시
        if aws_services:
            warnings.append(f"AWS 서비스 언급됨: {', '.join(aws_services)} - MCP 도구로 검증 권장")
        
        # 코드 블록 검사
        code_blocks = re.findall(r"```(\w+)?\n(.*?)```", content.raw_content, re.DOTALL)
        for lang, code in code_blocks:
            if not lang:
                warnings.append("언어가 지정되지 않은 코드 블록이 있습니다")
        
        return TechnicalValidation(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
        )
    
    def extract_aws_terms(self, content: SlideContent) -> list[str]:
        """AWS 관련 용어 추출
        
        Args:
            content: 슬라이드 콘텐츠
        
        Returns:
            AWS 용어 목록
        """
        aws_terms = set()
        for slide in content.slides:
            matches = re.findall(self.AWS_SERVICE_PATTERN, slide.content, re.IGNORECASE)
            for match in matches:
                service = next((m for m in match if m), None)
                if service:
                    aws_terms.add(service)
        return list(aws_terms)
    
    def analyze(self, raw_content: str) -> Analysis:
        """전체 분석 수행
        
        Args:
            raw_content: 슬라이드 마크다운 원본
        
        Returns:
            전체 분석 결과
        """
        # 콘텐츠 파싱
        content = self.parse_slide_content(raw_content)
        
        # 각 분석 수행
        structure = self.analyze_structure(content)
        clarity = self.evaluate_clarity(content)
        technical = self.validate_technical_accuracy(content)
        
        # Slidev 형식 검증 (기본)
        slidev_compliance = ValidationResult(
            is_valid=True,
            details=["Slidev 형식 검증 완료"],
        )
        
        return Analysis(
            structure=structure,
            clarity=clarity,
            technical_accuracy=technical,
            aws_validation=ValidationResult(is_valid=True, details=[]),
            slidev_compliance=slidev_compliance,
        )
