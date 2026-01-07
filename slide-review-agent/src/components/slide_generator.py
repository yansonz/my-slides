# 슬라이드 생성 모듈
"""Slidev 형식 슬라이드 생성 컴포넌트"""

from datetime import datetime
from typing import Optional


class SlideGenerator:
    """슬라이드 생성기"""
    
    # 기본 Slidev 템플릿
    DEFAULT_TEMPLATE = """---
theme: default
title: {title}
info: |
  ## {title}
  기술 발표 슬라이드
author: {author}
date: {date}
---

# {title}

{subtitle}

---

## 목차

1. 소개
2. 주요 내용
3. 데모
4. 결론

---

## 소개

{intro_content}

---

## 주요 내용

- 포인트 1
- 포인트 2
- 포인트 3

---

## 데모

실습 또는 데모 내용

---

## 결론

- 핵심 요약 1
- 핵심 요약 2
- 핵심 요약 3

---

## 감사합니다!

질문이 있으신가요?
"""
    
    def __init__(self, author: str = "Your Name"):
        """생성기 초기화
        
        Args:
            author: 기본 작성자 이름
        """
        self.author = author
    
    def generate_template(
        self,
        topic: str,
        title: Optional[str] = None,
        subtitle: str = "",
        intro_content: str = "내용을 여기에 작성하세요.",
    ) -> str:
        """Slidev 템플릿 생성
        
        Args:
            topic: 슬라이드 주제
            title: 슬라이드 제목 (없으면 주제 사용)
            subtitle: 부제목
            intro_content: 소개 내용
        
        Returns:
            Slidev 형식 템플릿 문자열
        """
        title = title or topic
        date = datetime.now().strftime("%Y-%m-%d")
        
        return self.DEFAULT_TEMPLATE.format(
            title=title,
            subtitle=subtitle or topic,
            author=self.author,
            date=date,
            intro_content=intro_content,
        )
    
    def generate_content(
        self,
        topic: str,
        aws_context: str = "",
        sections: Optional[list[str]] = None,
    ) -> str:
        """AWS 정보 기반 콘텐츠 생성
        
        Args:
            topic: 슬라이드 주제
            aws_context: AWS 관련 컨텍스트 정보
            sections: 섹션 목록
        
        Returns:
            생성된 슬라이드 콘텐츠
        """
        date = datetime.now().strftime("%Y-%m-%d")
        sections = sections or ["소개", "주요 내용", "데모", "결론"]
        
        lines = []
        
        # 프론트매터
        lines.append("---")
        lines.append("theme: default")
        lines.append(f"title: {topic}")
        lines.append("info: |")
        lines.append(f"  ## {topic}")
        lines.append("  기술 발표 슬라이드")
        lines.append(f"author: {self.author}")
        lines.append(f"date: {date}")
        lines.append("---")
        lines.append("")
        
        # 타이틀 슬라이드
        lines.append(f"# {topic}")
        lines.append("")
        lines.append("기술 발표")
        lines.append("")
        lines.append("---")
        lines.append("")
        
        # 목차
        lines.append("## 목차")
        lines.append("")
        for i, section in enumerate(sections, 1):
            lines.append(f"{i}. {section}")
        lines.append("")
        lines.append("---")
        lines.append("")
        
        # 각 섹션
        for section in sections:
            lines.append(f"## {section}")
            lines.append("")
            
            # AWS 컨텍스트가 있으면 포함
            if aws_context and section == "소개":
                lines.append(aws_context)
            else:
                lines.append("내용을 여기에 작성하세요.")
            
            lines.append("")
            lines.append("---")
            lines.append("")
        
        # 마무리 슬라이드
        lines.append("## 감사합니다!")
        lines.append("")
        lines.append("질문이 있으신가요?")
        
        return "\n".join(lines)
    
    def improve_slide(
        self,
        content: str,
        improvements: list[str],
    ) -> str:
        """슬라이드 개선
        
        Args:
            content: 원본 슬라이드 콘텐츠
            improvements: 개선 사항 목록
        
        Returns:
            개선된 슬라이드 콘텐츠
        """
        # 기본적으로 원본 반환 (실제 개선은 Agent가 수행)
        # 이 메서드는 프로그래밍적 개선을 위한 플레이스홀더
        improved = content
        
        # 개선 사항 주석 추가
        if improvements:
            comment = "\n<!--\n개선 사항:\n"
            for improvement in improvements:
                comment += f"- {improvement}\n"
            comment += "-->\n"
            
            # 프론트매터 뒤에 주석 추가
            if "---" in improved:
                parts = improved.split("---", 2)
                if len(parts) >= 3:
                    improved = f"---{parts[1]}---{comment}{parts[2]}"
        
        return improved
    
    def generate_slide_name(self, topic: str) -> str:
        """네이밍 컨벤션에 맞는 슬라이드 이름 생성
        
        Args:
            topic: 슬라이드 주제
        
        Returns:
            {yyyymmdd}-{title} 형식의 슬라이드 이름
        """
        import re
        
        date = datetime.now().strftime("%Y%m%d")
        
        # 주제를 슬러그로 변환
        slug = topic.lower()
        slug = re.sub(r"[^a-z0-9가-힣\s-]", "", slug)
        slug = re.sub(r"\s+", "-", slug)
        slug = re.sub(r"-+", "-", slug)
        slug = slug.strip("-")
        
        # 한글이 포함된 경우 영문으로 변환 시도 (간단한 매핑)
        korean_to_english = {
            "소개": "intro",
            "기초": "basics",
            "고급": "advanced",
            "실습": "hands-on",
            "데모": "demo",
        }
        
        for korean, english in korean_to_english.items():
            slug = slug.replace(korean, english)
        
        # 한글 제거 (영문만 남기기)
        slug = re.sub(r"[가-힣]", "", slug)
        slug = re.sub(r"-+", "-", slug)
        slug = slug.strip("-")
        
        if not slug:
            slug = "presentation"
        
        return f"{date}-{slug}"
