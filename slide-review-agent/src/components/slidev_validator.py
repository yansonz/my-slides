# Slidev 형식 검증 모듈
"""Slidev 형식 준수 여부 검증 컴포넌트"""

import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from ..models.analysis import ValidationResult


@dataclass
class ConsistencyReport:
    """스타일 일관성 보고서"""
    is_consistent: bool
    issues: list[str] = field(default_factory=list)
    suggestions: list[str] = field(default_factory=list)


class SlidevValidator:
    """Slidev 형식 검증기"""
    
    # 네이밍 컨벤션 패턴: yyyymmdd-title
    NAMING_PATTERN = r"^\d{8}-[a-z0-9-]+$"
    
    # 필수 프론트매터 필드
    REQUIRED_FRONTMATTER = ["theme", "title"]
    
    # 권장 프론트매터 필드
    RECOMMENDED_FRONTMATTER = ["author", "date", "info"]
    
    def validate_format(self, content: str) -> ValidationResult:
        """Slidev 형식 검증
        
        Args:
            content: 슬라이드 마크다운 콘텐츠
        
        Returns:
            검증 결과
        """
        details = []
        is_valid = True
        
        # 프론트매터 존재 확인
        if not content.startswith("---"):
            details.append("✗ 프론트매터가 없습니다 (--- 로 시작해야 함)")
            is_valid = False
        else:
            # 프론트매터 파싱
            frontmatter_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
            if frontmatter_match:
                frontmatter = frontmatter_match.group(1)
                
                # 필수 필드 확인
                for field in self.REQUIRED_FRONTMATTER:
                    if f"{field}:" not in frontmatter:
                        details.append(f"✗ 필수 필드 누락: {field}")
                        is_valid = False
                    else:
                        details.append(f"✓ 필수 필드 존재: {field}")
                
                # 권장 필드 확인
                for field in self.RECOMMENDED_FRONTMATTER:
                    if f"{field}:" not in frontmatter:
                        details.append(f"⚠ 권장 필드 누락: {field}")
                    else:
                        details.append(f"✓ 권장 필드 존재: {field}")
            else:
                details.append("✗ 프론트매터 형식이 올바르지 않습니다")
                is_valid = False
        
        # 슬라이드 구분자 확인
        slide_separators = re.findall(r"\n---\n", content)
        if len(slide_separators) < 1:
            details.append("⚠ 슬라이드 구분자(---)가 부족합니다")
        else:
            details.append(f"✓ 슬라이드 구분자 {len(slide_separators)}개 발견")
        
        # 마크다운 헤더 확인
        headers = re.findall(r"^#+\s+.+$", content, re.MULTILINE)
        if headers:
            details.append(f"✓ 마크다운 헤더 {len(headers)}개 발견")
        else:
            details.append("⚠ 마크다운 헤더가 없습니다")
        
        return ValidationResult(
            is_valid=is_valid,
            details=details,
        )
    
    def check_consistency(
        self,
        content: str,
        existing_slides: list[str],
    ) -> ConsistencyReport:
        """스타일 일관성 확인
        
        Args:
            content: 검사할 슬라이드 콘텐츠
            existing_slides: 기존 슬라이드 콘텐츠 목록
        
        Returns:
            일관성 보고서
        """
        issues = []
        suggestions = []
        is_consistent = True
        
        if not existing_slides:
            return ConsistencyReport(
                is_consistent=True,
                issues=[],
                suggestions=["기존 슬라이드가 없어 일관성 검사를 건너뜁니다"],
            )
        
        # 현재 슬라이드 테마 추출
        current_theme = self._extract_theme(content)
        
        # 기존 슬라이드 테마 추출
        existing_themes = set()
        for slide in existing_slides:
            theme = self._extract_theme(slide)
            if theme:
                existing_themes.add(theme)
        
        # 테마 일관성 확인
        if existing_themes and current_theme:
            if current_theme not in existing_themes:
                issues.append(f"테마 불일치: 현재 '{current_theme}', 기존 {existing_themes}")
                suggestions.append(f"기존 슬라이드와 동일한 테마 사용 권장: {list(existing_themes)[0]}")
                is_consistent = False
        
        # 헤더 스타일 일관성 확인
        current_header_style = self._analyze_header_style(content)
        for slide in existing_slides:
            existing_style = self._analyze_header_style(slide)
            if current_header_style != existing_style:
                issues.append("헤더 스타일이 기존 슬라이드와 다릅니다")
                is_consistent = False
                break
        
        return ConsistencyReport(
            is_consistent=is_consistent,
            issues=issues,
            suggestions=suggestions,
        )
    
    def validate_naming_convention(self, slide_name: str) -> bool:
        """네이밍 컨벤션 검증
        
        Args:
            slide_name: 슬라이드 폴더명
        
        Returns:
            유효 여부
        """
        if not re.match(self.NAMING_PATTERN, slide_name):
            return False
        
        # 날짜 유효성 검사
        date_str = slide_name[:8]
        try:
            datetime.strptime(date_str, "%Y%m%d")
            return True
        except ValueError:
            return False
    
    def suggest_valid_name(self, invalid_name: str) -> str:
        """유효한 이름 제안
        
        Args:
            invalid_name: 유효하지 않은 슬라이드 이름
        
        Returns:
            제안된 유효한 이름
        """
        today = datetime.now().strftime("%Y%m%d")
        
        # 기존 이름에서 영문/숫자/하이픈만 추출
        clean_name = re.sub(r"[^a-z0-9-]", "-", invalid_name.lower())
        clean_name = re.sub(r"-+", "-", clean_name).strip("-")
        
        if not clean_name:
            clean_name = "presentation"
        
        return f"{today}-{clean_name}"
    
    def _extract_theme(self, content: str) -> Optional[str]:
        """테마 추출
        
        Args:
            content: 슬라이드 콘텐츠
        
        Returns:
            테마 이름 또는 None
        """
        match = re.search(r"theme:\s*(\w+)", content)
        return match.group(1) if match else None
    
    def _analyze_header_style(self, content: str) -> str:
        """헤더 스타일 분석
        
        Args:
            content: 슬라이드 콘텐츠
        
        Returns:
            헤더 스타일 설명
        """
        # 가장 많이 사용된 헤더 레벨 확인
        h1_count = len(re.findall(r"^# ", content, re.MULTILINE))
        h2_count = len(re.findall(r"^## ", content, re.MULTILINE))
        h3_count = len(re.findall(r"^### ", content, re.MULTILINE))
        
        if h2_count >= h1_count and h2_count >= h3_count:
            return "h2-primary"
        elif h1_count >= h2_count and h1_count >= h3_count:
            return "h1-primary"
        else:
            return "h3-primary"
