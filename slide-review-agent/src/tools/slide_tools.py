# 슬라이드 관련 도구
"""슬라이드 파일 조작 및 검증 도구"""

import os
import re
import subprocess
from datetime import datetime
from strands import tool


@tool
def read_slide_content(slide_path: str) -> str:
    """슬라이드 파일의 내용을 읽어 반환합니다.
    
    Slidev 형식의 슬라이드 마크다운 파일을 읽습니다.
    슬라이드 검토 및 분석에 사용됩니다.
    
    Args:
        slide_path: 슬라이드 파일 경로 (예: "slides/my-presentation/slides.md")
    
    Returns:
        슬라이드 파일 내용 문자열
    """
    try:
        with open(slide_path, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return f"오류: 파일을 찾을 수 없습니다 - {slide_path}"
    except Exception as e:
        return f"오류: 파일 읽기 실패 - {str(e)}"


@tool
def validate_slide_name(slide_name: str) -> str:
    """슬라이드 폴더명이 네이밍 컨벤션을 따르는지 검증합니다.
    
    슬라이드 폴더명은 {yyyymmdd}-{title} 형식을 따라야 합니다.
    예: 20260107-docker-basics
    
    Args:
        slide_name: 검증할 슬라이드 폴더명
    
    Returns:
        검증 결과 문자열 (유효/무효 및 제안)
    """
    # 네이밍 컨벤션 패턴: yyyymmdd-title
    pattern = r"^\d{8}-[a-z0-9-]+$"
    
    if re.match(pattern, slide_name):
        # 날짜 유효성 검사
        date_str = slide_name[:8]
        try:
            datetime.strptime(date_str, "%Y%m%d")
            return f"✓ 유효한 슬라이드 이름입니다: {slide_name}"
        except ValueError:
            return f"✗ 날짜 형식이 올바르지 않습니다: {date_str}. YYYYMMDD 형식을 사용하세요."
    else:
        # 제안 생성
        today = datetime.now().strftime("%Y%m%d")
        # 기존 이름에서 영문/숫자/하이픈만 추출
        clean_name = re.sub(r"[^a-z0-9-]", "-", slide_name.lower())
        clean_name = re.sub(r"-+", "-", clean_name).strip("-")
        suggested_name = f"{today}-{clean_name}" if clean_name else f"{today}-presentation"
        
        return f"✗ 네이밍 컨벤션을 따르지 않습니다.\n현재: {slide_name}\n제안: {suggested_name}\n형식: {{yyyymmdd}}-{{title}}"


@tool
def create_slide(slide_name: str, scripts_path: str = "scripts/create-slide.sh") -> str:
    """새로운 슬라이드를 생성합니다.
    
    프로젝트의 create-slide.sh 스크립트를 사용하여 슬라이드를 생성합니다.
    슬라이드 이름은 네이밍 컨벤션을 따라야 합니다.
    
    Args:
        slide_name: 생성할 슬라이드 이름 (예: "20260107-docker-basics")
        scripts_path: 슬라이드 생성 스크립트 경로
    
    Returns:
        생성 결과 문자열
    """
    # 네이밍 컨벤션 검증
    validation = validate_slide_name.__wrapped__(slide_name)
    if "✗" in validation:
        return f"슬라이드 생성 실패:\n{validation}"
    
    try:
        # 스크립트 실행
        result = subprocess.run(
            [scripts_path, slide_name],
            capture_output=True,
            text=True,
            timeout=30,
        )
        
        if result.returncode == 0:
            return f"✓ 슬라이드 생성 완료: slides/{slide_name}\n{result.stdout}"
        else:
            return f"✗ 슬라이드 생성 실패:\n{result.stderr}"
    except FileNotFoundError:
        return f"✗ 스크립트를 찾을 수 없습니다: {scripts_path}"
    except subprocess.TimeoutExpired:
        return "✗ 스크립트 실행 시간 초과"
    except Exception as e:
        return f"✗ 슬라이드 생성 중 오류 발생: {str(e)}"


@tool
def list_slides(slides_dir: str = "slides") -> str:
    """프로젝트의 모든 슬라이드 목록을 반환합니다.
    
    slides 디렉토리 내의 모든 슬라이드 폴더를 나열합니다.
    각 슬라이드의 네이밍 컨벤션 준수 여부도 표시합니다.
    
    Args:
        slides_dir: 슬라이드 디렉토리 경로 (기본값: "slides")
    
    Returns:
        슬라이드 목록 문자열
    """
    try:
        if not os.path.exists(slides_dir):
            return f"슬라이드 디렉토리가 없습니다: {slides_dir}"
        
        slides = []
        for item in os.listdir(slides_dir):
            item_path = os.path.join(slides_dir, item)
            if os.path.isdir(item_path):
                # 네이밍 컨벤션 검증
                validation = validate_slide_name.__wrapped__(item)
                status = "✓" if "✓" in validation else "✗"
                slides.append(f"  {status} {item}")
        
        if not slides:
            return "슬라이드가 없습니다."
        
        return f"슬라이드 목록 ({len(slides)}개):\n" + "\n".join(sorted(slides))
    except Exception as e:
        return f"오류: 슬라이드 목록 조회 실패 - {str(e)}"
