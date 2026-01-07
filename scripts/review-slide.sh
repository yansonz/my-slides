#!/bin/bash

# 슬라이드 검토 스크립트
# Agent를 통해 슬라이드를 검토합니다.

if [ -z "$1" ]; then
  echo "사용법: ./scripts/review-slide.sh <슬라이드-이름>"
  echo "예: ./scripts/review-slide.sh kubernetes-basics"
  echo "    ./scripts/review-slide.sh 20260124-aws-builders-day"
  exit 1
fi

SLIDE_NAME=$1
SLIDE_PATH="slides/$SLIDE_NAME/slides.md"

# 슬라이드 파일 존재 확인
if [ ! -f "$SLIDE_PATH" ]; then
  echo "오류: 슬라이드 파일을 찾을 수 없습니다 - $SLIDE_PATH"
  exit 1
fi

# Agent를 통한 슬라이드 검토
cd slide-review-agent
.venv/bin/python cli.py review "../$SLIDE_PATH"
