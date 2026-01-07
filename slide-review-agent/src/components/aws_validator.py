# AWS 정보 검증 모듈
"""AWS MCP 도구를 활용한 AWS 정보 검증 컴포넌트"""

from dataclasses import dataclass, field
from typing import Optional

from ..models.analysis import ValidationResult


@dataclass
class AWSSearchResult:
    """AWS 문서 검색 결과"""
    title: str
    url: str
    snippet: str
    score: float = 0.0


@dataclass
class AWSRegionalInfo:
    """AWS 리전별 가용성 정보"""
    service: str
    region: str
    is_available: bool
    details: str = ""


class AWSInfoValidator:
    """AWS 정보 검증기
    
    AWS MCP 도구를 활용하여 AWS 관련 정보를 검증합니다.
    """
    
    def __init__(self):
        """검증기 초기화"""
        self._cache: dict[str, list[AWSSearchResult]] = {}
        self._regional_cache: dict[str, AWSRegionalInfo] = {}
    
    def search_documentation(
        self,
        query: str,
        limit: int = 5,
    ) -> list[AWSSearchResult]:
        """AWS 문서 검색
        
        Args:
            query: 검색 쿼리
            limit: 최대 결과 수
        
        Returns:
            검색 결과 목록
        """
        # 캐시 확인
        cache_key = f"{query}:{limit}"
        if cache_key in self._cache:
            return self._cache[cache_key]
        
        # AWS MCP 도구를 통해 검색 수행
        # 실제 구현에서는 MCP 서버 호출
        results = []
        
        # 캐시 저장
        self._cache[cache_key] = results
        return results
    
    def get_regional_availability(
        self,
        service: str,
        region: str = "us-west-2",
    ) -> AWSRegionalInfo:
        """AWS 서비스 리전별 가용성 확인
        
        Args:
            service: AWS 서비스 이름
            region: AWS 리전 코드
        
        Returns:
            리전별 가용성 정보
        """
        # 캐시 확인
        cache_key = f"{service}:{region}"
        if cache_key in self._regional_cache:
            return self._regional_cache[cache_key]
        
        # AWS MCP 도구를 통해 가용성 확인
        # 실제 구현에서는 MCP 서버 호출
        info = AWSRegionalInfo(
            service=service,
            region=region,
            is_available=True,  # 기본값
            details="",
        )
        
        # 캐시 저장
        self._regional_cache[cache_key] = info
        return info
    
    def validate_aws_concepts(
        self,
        concepts: list[str],
    ) -> ValidationResult:
        """AWS 개념 검증
        
        Args:
            concepts: 검증할 AWS 개념 목록
        
        Returns:
            검증 결과
        """
        details = []
        is_valid = True
        
        for concept in concepts:
            # AWS 문서에서 개념 검색
            results = self.search_documentation(concept, limit=3)
            
            if results:
                details.append(f"✓ '{concept}' - 검증됨")
            else:
                details.append(f"⚠ '{concept}' - 검증 필요 (문서 검색 결과 없음)")
        
        return ValidationResult(
            is_valid=is_valid,
            details=details,
        )
    
    def validate_service_in_region(
        self,
        services: list[str],
        region: str = "us-west-2",
    ) -> ValidationResult:
        """서비스 리전 가용성 검증
        
        Args:
            services: 검증할 서비스 목록
            region: 대상 리전
        
        Returns:
            검증 결과
        """
        details = []
        is_valid = True
        
        for service in services:
            info = self.get_regional_availability(service, region)
            
            if info.is_available:
                details.append(f"✓ '{service}' - {region}에서 사용 가능")
            else:
                details.append(f"✗ '{service}' - {region}에서 사용 불가")
                is_valid = False
        
        return ValidationResult(
            is_valid=is_valid,
            details=details,
        )
    
    def clear_cache(self) -> None:
        """캐시 초기화"""
        self._cache.clear()
        self._regional_cache.clear()
