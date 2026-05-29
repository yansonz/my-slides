# 이미지 업로드 가이드

## 이미지 서버 정보
- URL: https://images.yanbert.com
- S3 버킷: imageserverstack-imagebucket97210811-4mnbljzlj0ia
- 리전: ap-northeast-2

## 경로 규칙

이 프로젝트의 이미지 경로는 다음 패턴을 따릅니다:

```
https://images.yanbert.com/my-slides/images/{슬라이드폴더명}/{파일명}.webp
```

예시:
- `https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg1.webp`
- `https://images.yanbert.com/my-slides/images/20260529-kiro-staying-grounded-in-the-ai-era/image.webp`

## 업로드 절차

1. **webp 변환** (jpeg/png 등 다른 포맷인 경우)
   ```bash
   cwebp <원본파일> -o <파일명>.webp
   ```

2. **S3 업로드**
   ```bash
   aws s3 cp <파일명>.webp s3://imageserverstack-imagebucket97210811-4mnbljzlj0ia/my-slides/images/{슬라이드폴더명}/
   ```

3. **슬라이드에 삽입**
   ```markdown
   <img src="https://images.yanbert.com/my-slides/images/{슬라이드폴더명}/{파일명}.webp" class="h-90 mx-auto">
   ```

## 규칙
- 이미지는 반드시 webp 포맷으로 변환 후 업로드
- key(하위 폴더)는 슬라이드 폴더명 사용 (예: `20260529-kiro-staying-grounded-in-the-ai-era`)
- 업로드 전 최종 경로를 사용자에게 확인
- 슬라이드 내 이미지 경로는 항상 절대 URL 사용 (로컬 `/images/` 경로 대신)
