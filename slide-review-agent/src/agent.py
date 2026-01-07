# 슬라이드 검토 Agent
"""메인 Agent 클래스"""

import os
from strands import Agent

from .components.agent_initializer import AgentInitializer
from .components.content_analyzer import ContentAnalyzer
from .components.aws_validator import AWSInfoValidator
from .components.report_generator import ReportGenerator
from .components.slide_generator import SlideGenerator
from .components.slidev_validator import SlidevValidator
from .components.script_executor import ScriptExecutor, ExecutionResult
from .components.error_handler import ErrorHandler, ErrorType, ErrorContext
from .tools.aws_tools import search_aws_docs, get_aws_regional_info
from .tools.slide_tools import (
    read_slide_content,
    validate_slide_name,
    create_slide,
    list_slides,
)
from .models.analysis import Analysis
from .models.report import ReviewReport


class SlideReviewAgent:
    """슬라이드 검토 도우미 Agent
    
    Strands SDK를 기반으로 구축된 슬라이드 작성 및 검토 도우미입니다.
    AWS MCP 도구를 활용하여 AWS 관련 정보를 검증하고,
    Slidev 형식의 슬라이드 작성 및 검토를 지원합니다.
    """
    
    def __init__(
        self,
        model_id: str = "global.anthropic.claude-haiku-4-5-20251001-v1:0",
        region_name: str = "us-east-1",
        slides_dir: str = "slides",
        scripts_dir: str = "scripts",
    ):
        """Agent 초기화
        
        Args:
            model_id: Bedrock 모델 ID
            region_name: AWS 리전
            slides_dir: 슬라이드 디렉토리 경로
            scripts_dir: 스크립트 디렉토리 경로
        """
        self.slides_dir = slides_dir
        self.scripts_dir = scripts_dir
        
        # 컴포넌트 초기화
        self._initializer = AgentInitializer(
            model_id=model_id,
            region_name=region_name,
        )
        self._content_analyzer = ContentAnalyzer()
        self._aws_validator = AWSInfoValidator()
        self._report_generator = ReportGenerator()
        self._slide_generator = SlideGenerator()
        self._slidev_validator = SlidevValidator()
        self._script_executor = ScriptExecutor(
            scripts_dir=scripts_dir,
            slides_dir=slides_dir,
        )
        self._error_handler = ErrorHandler()
        
        # 도구 등록
        self._register_tools()
        
        # Agent 초기화
        self._agent = self._initializer.initialize_agent()
    
    def _register_tools(self) -> None:
        """도구 등록"""
        # AWS 도구
        self._initializer.register_tool(search_aws_docs)
        self._initializer.register_tool(get_aws_regional_info)
        
        # 슬라이드 도구
        self._initializer.register_tool(read_slide_content)
        self._initializer.register_tool(validate_slide_name)
        self._initializer.register_tool(create_slide)
        self._initializer.register_tool(list_slides)
    
    def chat(self, message: str) -> str:
        """Agent와 대화
        
        Args:
            message: 사용자 메시지
        
        Returns:
            Agent 응답
        """
        try:
            response = self._agent(message)
            return str(response)
        except Exception as e:
            context = ErrorContext(
                error_type=ErrorType.UNKNOWN_ERROR,
                message=str(e),
                original_error=e,
            )
            result = self._error_handler.handle_error(context)
            return self._error_handler.format_error_message(result)
    
    def analyze_slide(self, slide_path: str) -> Analysis:
        """슬라이드 분석 (프로그래밍 방식)
        
        Args:
            slide_path: 슬라이드 파일 경로
        
        Returns:
            분석 결과
        """
        try:
            with open(slide_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            return self._content_analyzer.analyze(content)
        except Exception as e:
            context = ErrorContext(
                error_type=ErrorType.ANALYSIS_ERROR,
                message=str(e),
                original_error=e,
            )
            self._error_handler.handle_error(context)
            return Analysis()
    
    def generate_report(self, slide_path: str) -> ReviewReport:
        """검토 보고서 생성 (프로그래밍 방식)
        
        Args:
            slide_path: 슬라이드 파일 경로
        
        Returns:
            검토 보고서
        """
        analysis = self.analyze_slide(slide_path)
        return self._report_generator.generate_report(analysis)
    
    def review_slide(self, slide_path: str) -> str:
        """슬라이드 검토 (Agent 활용)
        
        Args:
            slide_path: 슬라이드 파일 경로
        
        Returns:
            검토 결과
        """
        # 슬라이드 폴더명 추출
        slide_name = os.path.basename(os.path.dirname(slide_path))
        
        prompt = f"""다음 슬라이드를 검토해주세요: {slide_path}

1. 먼저 슬라이드 내용을 읽어주세요.
2. 슬라이드 폴더명({slide_name})이 네이밍 컨벤션(yyyymmdd-title)을 따르는지 확인해주세요.
3. 슬라이드 구조, 명확성, 기술적 정확성을 평가해주세요.
4. AWS 관련 내용이 있다면 정확성을 검증해주세요.
5. 강점, 개선 사항, 구체적 제안을 포함한 검토 보고서를 작성해주세요."""
        
        return self.chat(prompt)
    
    def create_new_slide(self, topic: str, title: str = None) -> str:
        """새 슬라이드 생성 (Agent 활용)
        
        Args:
            topic: 슬라이드 주제
            title: 슬라이드 제목 (없으면 주제에서 생성)
        
        Returns:
            생성 결과
        """
        prompt = f"""새로운 슬라이드를 생성해주세요.

주제: {topic}
제목: {title or '주제에서 적절한 제목 생성'}

1. 네이밍 컨벤션(yyyymmdd-title)에 맞는 슬라이드 이름을 생성해주세요.
2. create_slide 도구를 사용하여 슬라이드를 생성해주세요.
3. 생성된 슬라이드에 대한 초기 검토를 수행해주세요."""
        
        return self.chat(prompt)
    
    def create_slide_programmatic(self, slide_name: str) -> ExecutionResult:
        """슬라이드 생성 (프로그래밍 방식)
        
        Args:
            slide_name: 슬라이드 이름
        
        Returns:
            실행 결과
        """
        # 네이밍 컨벤션 검증
        if not self._slidev_validator.validate_naming_convention(slide_name):
            suggested_name = self._slidev_validator.suggest_valid_name(slide_name)
            return ExecutionResult(
                success=False,
                output="",
                error=f"네이밍 컨벤션 위반. 제안: {suggested_name}",
            )
        
        return self._script_executor.execute_create_slide(slide_name)
    
    def list_all_slides(self) -> str:
        """모든 슬라이드 목록 조회 (Agent 활용)
        
        Returns:
            슬라이드 목록
        """
        return self.chat("프로젝트의 모든 슬라이드 목록을 보여주세요. 네이밍 컨벤션 준수 여부도 확인해주세요.")
    
    def get_slides_list(self) -> list[dict]:
        """슬라이드 목록 조회 (프로그래밍 방식)
        
        Returns:
            슬라이드 정보 목록
        """
        slides = []
        
        if not os.path.exists(self.slides_dir):
            return slides
        
        for item in os.listdir(self.slides_dir):
            item_path = os.path.join(self.slides_dir, item)
            if os.path.isdir(item_path):
                slides_md = os.path.join(item_path, "slides.md")
                slides.append({
                    "name": item,
                    "path": item_path,
                    "slides_md": slides_md if os.path.exists(slides_md) else None,
                    "valid_name": self._slidev_validator.validate_naming_convention(item),
                })
        
        return sorted(slides, key=lambda x: x["name"])
    
    def validate_slide_format(self, slide_path: str) -> dict:
        """슬라이드 형식 검증 (프로그래밍 방식)
        
        Args:
            slide_path: 슬라이드 파일 경로
        
        Returns:
            검증 결과
        """
        try:
            with open(slide_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            result = self._slidev_validator.validate_format(content)
            return {
                "is_valid": result.is_valid,
                "details": result.details,
            }
        except Exception as e:
            return {
                "is_valid": False,
                "details": [f"파일 읽기 오류: {str(e)}"],
            }
    
    @property
    def agent(self) -> Agent:
        """Agent 인스턴스 반환"""
        return self._agent
    
    @property
    def tools(self) -> list:
        """등록된 도구 목록 반환"""
        return self._initializer.tools
