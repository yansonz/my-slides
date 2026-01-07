# 오류 처리 모듈
"""오류 처리 및 복원력 컴포넌트"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Optional, TypeVar

T = TypeVar("T")


class ErrorType(Enum):
    """오류 유형"""
    AWS_MCP_ERROR = "aws_mcp_error"
    SCRIPT_ERROR = "script_error"
    FORMAT_ERROR = "format_error"
    ANALYSIS_ERROR = "analysis_error"
    NETWORK_ERROR = "network_error"
    UNKNOWN_ERROR = "unknown_error"


@dataclass
class ErrorContext:
    """오류 컨텍스트"""
    error_type: ErrorType
    message: str
    original_error: Optional[Exception] = None
    details: dict[str, Any] = field(default_factory=dict)
    recoverable: bool = True


@dataclass
class ErrorResult:
    """오류 처리 결과"""
    handled: bool
    message: str
    fallback_value: Optional[Any] = None
    suggestions: list[str] = field(default_factory=list)


class ErrorHandler:
    """오류 처리기"""
    
    def __init__(self):
        """처리기 초기화"""
        self._handlers: dict[ErrorType, Callable[[ErrorContext], ErrorResult]] = {}
        self._register_default_handlers()
    
    def _register_default_handlers(self) -> None:
        """기본 오류 핸들러 등록"""
        self._handlers[ErrorType.AWS_MCP_ERROR] = self._handle_aws_mcp_error
        self._handlers[ErrorType.SCRIPT_ERROR] = self._handle_script_error
        self._handlers[ErrorType.FORMAT_ERROR] = self._handle_format_error
        self._handlers[ErrorType.ANALYSIS_ERROR] = self._handle_analysis_error
        self._handlers[ErrorType.NETWORK_ERROR] = self._handle_network_error
        self._handlers[ErrorType.UNKNOWN_ERROR] = self._handle_unknown_error
    
    def handle_error(self, context: ErrorContext) -> ErrorResult:
        """오류 처리
        
        Args:
            context: 오류 컨텍스트
        
        Returns:
            오류 처리 결과
        """
        handler = self._handlers.get(context.error_type, self._handle_unknown_error)
        return handler(context)
    
    def _handle_aws_mcp_error(self, context: ErrorContext) -> ErrorResult:
        """AWS MCP 도구 오류 처리"""
        suggestions = [
            "AWS 자격 증명이 올바르게 설정되어 있는지 확인하세요",
            "AWS MCP 서버가 실행 중인지 확인하세요",
            "네트워크 연결 상태를 확인하세요",
        ]
        
        return ErrorResult(
            handled=True,
            message=f"AWS MCP 도구 오류: {context.message}",
            fallback_value=None,
            suggestions=suggestions,
        )
    
    def _handle_script_error(self, context: ErrorContext) -> ErrorResult:
        """스크립트 실행 오류 처리"""
        suggestions = [
            "스크립트 파일이 존재하는지 확인하세요",
            "스크립트 실행 권한이 있는지 확인하세요 (chmod +x)",
            "스크립트 내용에 오류가 없는지 확인하세요",
        ]
        
        return ErrorResult(
            handled=True,
            message=f"스크립트 실행 오류: {context.message}",
            fallback_value=None,
            suggestions=suggestions,
        )
    
    def _handle_format_error(self, context: ErrorContext) -> ErrorResult:
        """형식 검증 오류 처리"""
        suggestions = [
            "Slidev 형식 가이드를 참조하세요",
            "프론트매터가 올바르게 작성되었는지 확인하세요",
            "슬라이드 구분자(---)가 올바르게 사용되었는지 확인하세요",
        ]
        
        return ErrorResult(
            handled=True,
            message=f"형식 오류: {context.message}",
            fallback_value=None,
            suggestions=suggestions,
        )
    
    def _handle_analysis_error(self, context: ErrorContext) -> ErrorResult:
        """콘텐츠 분석 오류 처리"""
        suggestions = [
            "슬라이드 파일이 올바른 형식인지 확인하세요",
            "파일 인코딩이 UTF-8인지 확인하세요",
        ]
        
        # 부분 결과 반환 시도
        partial_result = context.details.get("partial_result")
        
        return ErrorResult(
            handled=True,
            message=f"분석 오류: {context.message}",
            fallback_value=partial_result,
            suggestions=suggestions,
        )
    
    def _handle_network_error(self, context: ErrorContext) -> ErrorResult:
        """네트워크 오류 처리"""
        suggestions = [
            "인터넷 연결 상태를 확인하세요",
            "방화벽 설정을 확인하세요",
            "잠시 후 다시 시도하세요",
        ]
        
        return ErrorResult(
            handled=True,
            message=f"네트워크 오류: {context.message}",
            fallback_value=None,
            suggestions=suggestions,
        )
    
    def _handle_unknown_error(self, context: ErrorContext) -> ErrorResult:
        """알 수 없는 오류 처리"""
        suggestions = [
            "오류 로그를 확인하세요",
            "문제가 지속되면 관리자에게 문의하세요",
        ]
        
        return ErrorResult(
            handled=True,
            message=f"알 수 없는 오류: {context.message}",
            fallback_value=None,
            suggestions=suggestions,
        )
    
    def register_handler(
        self,
        error_type: ErrorType,
        handler: Callable[[ErrorContext], ErrorResult],
    ) -> None:
        """커스텀 오류 핸들러 등록
        
        Args:
            error_type: 오류 유형
            handler: 핸들러 함수
        """
        self._handlers[error_type] = handler
    
    def format_error_message(self, result: ErrorResult) -> str:
        """오류 메시지 포맷
        
        Args:
            result: 오류 처리 결과
        
        Returns:
            포맷된 오류 메시지
        """
        lines = [f"⚠️ {result.message}"]
        
        if result.suggestions:
            lines.append("\n💡 제안:")
            for suggestion in result.suggestions:
                lines.append(f"  - {suggestion}")
        
        if result.fallback_value is not None:
            lines.append("\n📋 부분 결과가 반환되었습니다.")
        
        return "\n".join(lines)


def with_error_handling(
    error_type: ErrorType,
    fallback_value: Optional[T] = None,
) -> Callable:
    """오류 처리 데코레이터
    
    Args:
        error_type: 오류 유형
        fallback_value: 오류 시 반환할 기본값
    
    Returns:
        데코레이터 함수
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        def wrapper(*args, **kwargs) -> T:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                handler = ErrorHandler()
                context = ErrorContext(
                    error_type=error_type,
                    message=str(e),
                    original_error=e,
                    recoverable=True,
                )
                result = handler.handle_error(context)
                
                if result.fallback_value is not None:
                    return result.fallback_value
                elif fallback_value is not None:
                    return fallback_value
                else:
                    raise
        
        return wrapper
    return decorator
