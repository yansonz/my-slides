# Agent 초기화 모듈
"""Strands SDK를 사용한 Agent 초기화"""

from strands import Agent, tool
from strands.models import BedrockModel


# 시스템 프롬프트 정의
SYSTEM_PROMPT = """당신은 Slidev 슬라이드 작성 및 검토를 도와주는 전문 AI 어시스턴트입니다.

## 역할
- 슬라이드 콘텐츠 분석 및 검토
- AWS 관련 기술 정보 검증
- 슬라이드 구조, 명확성, 기술적 정확성 평가
- 개선 제안 및 구체적인 예시 제공

## 슬라이드 검토 기준
1. 구조: 도입부, 본문, 결론이 명확한가?
2. 명확성: 각 슬라이드의 메시지가 명확한가?
3. 기술적 정확성: AWS 서비스 및 기술 용어가 정확한가?
4. 일관성: Slidev 형식과 프로젝트 스타일을 따르는가?

## 네이밍 컨벤션
슬라이드 폴더명은 {yyyymmdd}-{title} 형식을 따라야 합니다.
예: 20260107-docker-basics

## 응답 형식
검토 결과는 다음 섹션을 포함해야 합니다:
- 강점 (Strengths)
- 개선 사항 (Improvements)
- 구체적 제안 (Suggestions)
"""


class AgentInitializer:
    """Agent 초기화 클래스"""
    
    def __init__(
        self,
        model_id: str = "global.anthropic.claude-haiku-4-5-20251001-v1:0",
        region_name: str = "us-east-1",
        temperature: float = 0.3,
        max_tokens: int = 4096,
    ):
        """Agent 초기화
        
        Args:
            model_id: Bedrock 모델 ID
            region_name: AWS 리전
            temperature: 모델 온도 (낮을수록 일관된 응답)
            max_tokens: 최대 토큰 수
        """
        self.model_id = model_id
        self.region_name = region_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        self._agent = None
        self._tools = []
    
    def load_system_prompt(self) -> str:
        """시스템 프롬프트 로드
        
        Returns:
            시스템 프롬프트 문자열
        """
        return SYSTEM_PROMPT
    
    def register_tool(self, tool_func) -> None:
        """도구 등록
        
        Args:
            tool_func: 등록할 도구 함수
        """
        self._tools.append(tool_func)
    
    def initialize_agent(self) -> Agent:
        """Agent 초기화 및 반환
        
        Returns:
            초기화된 Agent 인스턴스
        """
        # Bedrock 모델 설정
        model = BedrockModel(
            model_id=self.model_id,
            region_name=self.region_name,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        
        # Agent 생성
        self._agent = Agent(
            model=model,
            tools=self._tools,
            system_prompt=self.load_system_prompt(),
        )
        
        return self._agent
    
    @property
    def agent(self) -> Agent:
        """Agent 인스턴스 반환
        
        Returns:
            Agent 인스턴스 (없으면 초기화 후 반환)
        """
        if self._agent is None:
            return self.initialize_agent()
        return self._agent
    
    @property
    def tools(self) -> list:
        """등록된 도구 목록 반환
        
        Returns:
            도구 목록
        """
        return self._tools
