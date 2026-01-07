#!/bin/bash

# 새로운 슬라이드 생성 스크립트

if [ -z "$1" ]; then
  echo "사용법: ./scripts/create-slide.sh <슬라이드-이름>"
  echo "예: ./scripts/create-slide.sh my-presentation"
  exit 1
fi

SLIDE_NAME=$1
SLIDE_DIR="slides/$SLIDE_NAME"

# 폴더 생성
mkdir -p "$SLIDE_DIR/public"
mkdir -p "$SLIDE_DIR/components"

# slides.md 생성
cat > "$SLIDE_DIR/slides.md" << 'EOF'
---
theme: default
title: 발표 제목
info: |
  ## 발표 제목
  기술 발표 슬라이드
author: Your Name
date: 2026-01-07
---

# 발표 제목

부제목

---

## 슬라이드 1

내용을 여기에 작성하세요.

---

## 슬라이드 2

- 포인트 1
- 포인트 2
- 포인트 3

---

## 감사합니다!

질문이 있으신가요?
EOF

# slidev.config.ts 생성
cat > "$SLIDE_DIR/slidev.config.ts" << 'EOF'
import { defineConfig } from '@slidev/cli'

export default defineConfig({
  title: '발표 제목',
  theme: 'default',
  fonts: {
    sans: 'Roboto',
    serif: 'Roboto Slab',
    mono: 'Fira Code',
  },
  export: {
    format: 'pdf',
    timeout: 30000,
    dark: false,
    withClicks: false,
  },
})
EOF

echo "✓ 슬라이드 생성 완료: $SLIDE_DIR"
echo ""
echo "다음 명령어로 슬라이드를 실행할 수 있습니다:"
echo "  npm run dev -- $SLIDE_DIR"
