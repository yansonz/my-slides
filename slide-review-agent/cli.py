#!/usr/bin/env python3
# CLI 스크립트
"""슬라이드 검토 도우미 Agent CLI"""

import argparse
import sys
import os

# 프로젝트 루트를 path에 추가
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.agent import SlideReviewAgent


def review_slide(slide_path: str):
    """슬라이드 검토 (Agent 모드)"""
    agent = SlideReviewAgent()
    
    print(f"🔍 슬라이드 검토 중: {slide_path}")
    print("-" * 50)
    result = agent.review_slide(slide_path)
    print(result)


def list_slides():
    """슬라이드 목록 조회"""
    agent = SlideReviewAgent()
    slides = agent.get_slides_list()
    
    print("📋 슬라이드 목록")
    print("-" * 50)
    
    for slide in slides:
        status = "✓" if slide["valid_name"] else "✗"
        print(f"  {status} {slide['name']}")
    
    print(f"\n총 {len(slides)}개 슬라이드")


def validate_slide(slide_name: str):
    """슬라이드 이름 검증"""
    agent = SlideReviewAgent()
    is_valid = agent._slidev_validator.validate_naming_convention(slide_name)
    
    if is_valid:
        print(f"✓ 유효한 슬라이드 이름: {slide_name}")
    else:
        suggested = agent._slidev_validator.suggest_valid_name(slide_name)
        print(f"✗ 유효하지 않은 슬라이드 이름: {slide_name}")
        print(f"  제안: {suggested}")


def create_slide(slide_name: str):
    """슬라이드 생성"""
    agent = SlideReviewAgent()
    result = agent.create_slide_programmatic(slide_name)
    
    if result.success:
        print(f"✓ 슬라이드 생성 완료: {result.slide_path}")
        print(result.output)
    else:
        print(f"✗ 슬라이드 생성 실패: {result.error}")


def chat_mode():
    """대화 모드"""
    agent = SlideReviewAgent()
    
    print("💬 슬라이드 검토 도우미 Agent")
    print("종료하려면 'exit' 또는 'quit'를 입력하세요.")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\n> ").strip()
            
            if user_input.lower() in ["exit", "quit", "q"]:
                print("👋 안녕히 가세요!")
                break
            
            if not user_input:
                continue
            
            response = agent.chat(user_input)
            print(f"\n{response}")
        
        except KeyboardInterrupt:
            print("\n👋 안녕히 가세요!")
            break


def main():
    parser = argparse.ArgumentParser(
        description="슬라이드 검토 도우미 Agent CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예시:
  # 슬라이드 검토
  python cli.py review slides/kubernetes-basics/slides.md
  
  # 슬라이드 목록 조회
  python cli.py list
  
  # 슬라이드 이름 검증
  python cli.py validate my-presentation
  
  # 슬라이드 생성
  python cli.py create 20260107-docker-basics
  
  # 대화 모드
  python cli.py chat
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="명령어")
    
    # review 명령어
    review_parser = subparsers.add_parser("review", help="슬라이드 검토")
    review_parser.add_argument("path", help="슬라이드 파일 경로")
    
    # list 명령어
    subparsers.add_parser("list", help="슬라이드 목록 조회")
    
    # validate 명령어
    validate_parser = subparsers.add_parser("validate", help="슬라이드 이름 검증")
    validate_parser.add_argument("name", help="슬라이드 이름")
    
    # create 명령어
    create_parser = subparsers.add_parser("create", help="슬라이드 생성")
    create_parser.add_argument("name", help="슬라이드 이름 (yyyymmdd-title 형식)")
    
    # chat 명령어
    subparsers.add_parser("chat", help="대화 모드")
    
    args = parser.parse_args()
    
    if args.command == "review":
        review_slide(args.path)
    elif args.command == "list":
        list_slides()
    elif args.command == "validate":
        validate_slide(args.name)
    elif args.command == "create":
        create_slide(args.name)
    elif args.command == "chat":
        chat_mode()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
