# AWS 관련 도구
"""AWS MCP 도구를 활용한 AWS 정보 검색 도구"""

from strands import tool


@tool
def search_aws_docs(query: str, limit: int = 5) -> str:
    """AWS 문서를 검색하여 관련 정보를 반환합니다.
    
    AWS 서비스, 기능, 설정 등에 대한 정보를 검색할 때 사용합니다.
    슬라이드에 포함된 AWS 관련 내용의 정확성을 검증하는 데 활용됩니다.
    
    Args:
        query: 검색할 AWS 관련 쿼리 (예: "Lambda function", "S3 bucket policy")
        limit: 반환할 최대 결과 수 (기본값: 5)
    
    Returns:
        검색 결과 문자열 (제목, URL, 요약 포함)
    """
    # 이 도구는 AWS MCP 서버와 연동하여 실제 검색을 수행합니다.
    # 현재는 플레이스홀더로 구현되어 있으며,
    # 실제 구현 시 AWS Documentation MCP 서버를 호출합니다.
    return f"AWS 문서 검색 결과 (쿼리: {query}, 제한: {limit}개)"


@tool
def get_aws_regional_info(service: str, region: str = "us-west-2") -> str:
    """특정 AWS 서비스의 리전별 가용성 정보를 반환합니다.
    
    AWS 서비스가 특정 리전에서 사용 가능한지 확인할 때 사용합니다.
    슬라이드에서 언급된 AWS 서비스의 리전 가용성을 검증하는 데 활용됩니다.
    
    Args:
        service: AWS 서비스 이름 (예: "Lambda", "Bedrock", "SageMaker")
        region: AWS 리전 코드 (기본값: "us-west-2")
    
    Returns:
        서비스 가용성 정보 문자열
    """
    # 이 도구는 AWS MCP 서버와 연동하여 실제 정보를 조회합니다.
    # 현재는 플레이스홀더로 구현되어 있습니다.
    return f"AWS 서비스 가용성 정보 (서비스: {service}, 리전: {region})"
