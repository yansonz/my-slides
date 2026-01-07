# 스크립트 실행 모듈
"""프로젝트 스크립트 실행 컴포넌트"""

import os
import subprocess
from dataclasses import dataclass
from typing import Optional


@dataclass
class ExecutionResult:
    """스크립트 실행 결과"""
    success: bool
    output: str
    error: Optional[str] = None
    slide_path: Optional[str] = None


class ScriptExecutor:
    """스크립트 실행기"""
    
    def __init__(
        self,
        scripts_dir: str = "scripts",
        slides_dir: str = "slides",
        timeout: int = 60,
    ):
        """실행기 초기화
        
        Args:
            scripts_dir: 스크립트 디렉토리 경로
            slides_dir: 슬라이드 디렉토리 경로
            timeout: 실행 타임아웃 (초)
        """
        self.scripts_dir = scripts_dir
        self.slides_dir = slides_dir
        self.timeout = timeout
    
    def execute_create_slide(self, slide_name: str) -> ExecutionResult:
        """슬라이드 생성 스크립트 실행
        
        Args:
            slide_name: 생성할 슬라이드 이름
        
        Returns:
            실행 결과
        """
        script_path = os.path.join(self.scripts_dir, "create-slide.sh")
        
        # 스크립트 존재 확인
        if not os.path.exists(script_path):
            return ExecutionResult(
                success=False,
                output="",
                error=f"스크립트를 찾을 수 없습니다: {script_path}",
            )
        
        try:
            # 스크립트 실행
            result = subprocess.run(
                [script_path, slide_name],
                capture_output=True,
                text=True,
                timeout=self.timeout,
                cwd=os.getcwd(),
            )
            
            slide_path = os.path.join(self.slides_dir, slide_name)
            
            if result.returncode == 0:
                return ExecutionResult(
                    success=True,
                    output=result.stdout,
                    slide_path=slide_path,
                )
            else:
                return ExecutionResult(
                    success=False,
                    output=result.stdout,
                    error=result.stderr or "스크립트 실행 실패",
                )
        
        except subprocess.TimeoutExpired:
            return ExecutionResult(
                success=False,
                output="",
                error=f"스크립트 실행 시간 초과 ({self.timeout}초)",
            )
        except PermissionError:
            return ExecutionResult(
                success=False,
                output="",
                error=f"스크립트 실행 권한이 없습니다: {script_path}",
            )
        except Exception as e:
            return ExecutionResult(
                success=False,
                output="",
                error=f"스크립트 실행 중 오류: {str(e)}",
            )
    
    def execute_export_all(self) -> ExecutionResult:
        """전체 슬라이드 내보내기 스크립트 실행
        
        Returns:
            실행 결과
        """
        script_path = os.path.join(self.scripts_dir, "export-all.sh")
        
        # 스크립트 존재 확인
        if not os.path.exists(script_path):
            return ExecutionResult(
                success=False,
                output="",
                error=f"스크립트를 찾을 수 없습니다: {script_path}",
            )
        
        try:
            # 스크립트 실행
            result = subprocess.run(
                [script_path],
                capture_output=True,
                text=True,
                timeout=self.timeout * 5,  # 내보내기는 더 오래 걸릴 수 있음
                cwd=os.getcwd(),
            )
            
            if result.returncode == 0:
                return ExecutionResult(
                    success=True,
                    output=result.stdout,
                )
            else:
                return ExecutionResult(
                    success=False,
                    output=result.stdout,
                    error=result.stderr or "내보내기 실패",
                )
        
        except subprocess.TimeoutExpired:
            return ExecutionResult(
                success=False,
                output="",
                error=f"내보내기 시간 초과 ({self.timeout * 5}초)",
            )
        except Exception as e:
            return ExecutionResult(
                success=False,
                output="",
                error=f"내보내기 중 오류: {str(e)}",
            )
    
    def handle_script_error(self, result: ExecutionResult) -> str:
        """스크립트 오류 처리
        
        Args:
            result: 실행 결과
        
        Returns:
            사용자 친화적 오류 메시지
        """
        if result.success:
            return "스크립트가 성공적으로 실행되었습니다."
        
        error_messages = []
        
        if result.error:
            # 오류 유형별 메시지
            if "찾을 수 없습니다" in result.error:
                error_messages.append("스크립트 파일이 존재하지 않습니다.")
                error_messages.append("scripts/ 디렉토리에 스크립트가 있는지 확인하세요.")
            elif "권한" in result.error:
                error_messages.append("스크립트 실행 권한이 없습니다.")
                error_messages.append("chmod +x scripts/*.sh 명령으로 권한을 부여하세요.")
            elif "시간 초과" in result.error:
                error_messages.append("스크립트 실행 시간이 초과되었습니다.")
                error_messages.append("네트워크 연결이나 시스템 상태를 확인하세요.")
            else:
                error_messages.append(f"오류: {result.error}")
        
        if result.output:
            error_messages.append(f"출력: {result.output}")
        
        return "\n".join(error_messages)
    
    def check_scripts_available(self) -> dict[str, bool]:
        """사용 가능한 스크립트 확인
        
        Returns:
            스크립트별 사용 가능 여부
        """
        scripts = {
            "create-slide.sh": False,
            "export-all.sh": False,
        }
        
        for script_name in scripts:
            script_path = os.path.join(self.scripts_dir, script_name)
            scripts[script_name] = os.path.exists(script_path) and os.access(script_path, os.X_OK)
        
        return scripts
