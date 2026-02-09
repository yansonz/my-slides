#!/bin/bash

# 새로운 슬라이드 생성 스크립트

if [ -z "$1" ]; then
  echo "사용법: ./scripts/create-slide.sh <슬라이드-이름>"
  echo "예: ./scripts/create-slide.sh my-presentation"
  exit 1
fi

SLIDE_NAME=$1
SLIDE_DIR="slides/$SLIDE_NAME"

# 폴더명에서 날짜 추출 (YYYYMMDD 형식이 있으면 사용, 없으면 오늘 날짜)
if [[ "$SLIDE_NAME" =~ ^([0-9]{4})([0-9]{2})([0-9]{2}) ]]; then
  YEAR="${BASH_REMATCH[1]}"
  MONTH="${BASH_REMATCH[2]}"
  DAY="${BASH_REMATCH[3]}"
else
  YEAR=$(date +%Y)
  MONTH=$(date +%m)
  DAY=$(date +%d)
fi

# 슬라이드 표시용 날짜 포맷 (DD Mon YYYY)
DISPLAY_DATE="$DAY $(date -j -f '%m' "$MONTH" '+%b' 2>/dev/null || date -d "${YEAR}-${MONTH}-01" '+%b' 2>/dev/null) $YEAR"
ISO_DATE="${YEAR}-${MONTH}-${DAY}"

# 폴더 생성
mkdir -p "$SLIDE_DIR/public"
mkdir -p "$SLIDE_DIR/components"

# slides.md 생성
cat > "$SLIDE_DIR/slides.md" << EOF
---
theme: default
title: 발표 제목
info: |
  ## 발표 제목
  기술 발표 슬라이드
author: Yan So
date: ${ISO_DATE}
css: unocss
---

<script setup>
import './style.css'
</script>

# 발표 제목

${DISPLAY_DATE}

<div class="absolute bottom-10">
  <span class="font-700">
    Yan So
  </span>
</div>

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

# style.css 생성
cat > "$SLIDE_DIR/style.css" << 'EOF'
.slidev-layout h1 {
  font-size: 3rem;
  font-weight: 700;
}

.slidev-layout h2 {
  font-size: 2.5rem;
  font-weight: 600;
}

.slidev-layout h3 {
  font-size: 2rem;
  font-weight: 500;
}

/* 일반 텍스트 - 슬라이드 전체 기본 폰트 크기 */
.slidev-layout {
  font-size: 1.5rem;
}
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
echo "  npm run dev -- $SLIDE_DIR/slides.md"
