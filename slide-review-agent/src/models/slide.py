# 슬라이드 데이터 모델
"""슬라이드 콘텐츠 관련 데이터 모델"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SlideMetadata:
    """슬라이드 메타데이터"""
    author: str = ""
    date: str = ""
    theme: str = "default"


@dataclass
class Slide:
    """개별 슬라이드"""
    title: str
    content: str
    notes: Optional[str] = None
    layout: Optional[str] = None


@dataclass
class SlideContent:
    """슬라이드 콘텐츠 전체"""
    title: str
    topic: str
    slides: list[Slide] = field(default_factory=list)
    metadata: SlideMetadata = field(default_factory=SlideMetadata)
    raw_content: str = ""
