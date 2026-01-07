#!/bin/bash

# 모든 슬라이드를 PDF와 PPTX로 내보내기

SLIDES_DIR="slides"
EXPORT_DIR="exports"

# 내보내기 폴더 생성
mkdir -p "$EXPORT_DIR"

echo "모든 슬라이드를 내보내는 중..."
echo ""

for slide_folder in "$SLIDES_DIR"/*; do
  if [ -d "$slide_folder" ]; then
    slide_name=$(basename "$slide_folder")
    
    echo "처리 중: $slide_name"
    
    # PDF 내보내기
    slidev export "$slide_folder/slides.md" \
      --format pdf \
      --output "$EXPORT_DIR/$slide_name.pdf" 2>/dev/null
    
    # PPTX 내보내기
    slidev export "$slide_folder/slides.md" \
      --format pptx \
      --output "$EXPORT_DIR/$slide_name.pptx" 2>/dev/null
    
    echo "  ✓ $slide_name 내보내기 완료"
  fi
done

echo ""
echo "모든 슬라이드가 $EXPORT_DIR 폴더에 저장되었습니다."
