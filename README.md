# 기술 발표 슬라이드 관리 프로젝트

Slidev를 사용한 기술 발표 슬라이드 관리 시스템입니다.

## 프로젝트 구조

```
slides/
├── kubernetes-basics/          # 각 발표별 독립 폴더
│   ├── slides.md              # 슬라이드 콘텐츠
│   ├── slidev.config.ts       # 슬라이드 설정
│   ├── public/                # 이미지, 동영상 등 리소스
│   └── components/            # 커스텀 컴포넌트
├── docker-advanced/
│   ├── slides.md
│   ├── slidev.config.ts
│   └── ...
└── ...
```

## 설치

```bash
npm install
```

## 사용 방법

### 1. 초기 설정

```bash
# 의존성 설치
npm install
```

### 2. 로컬 개발 서버 실행

```bash
# 특정 슬라이드 실행 (slides.md 파일 경로 지정)
npm run dev -- slides/kubernetes-basics/slides.md
```

**접속 주소:**
- 슬라이드 보기: http://localhost:3030/
- 발표자 모드: http://localhost:3030/presenter/
- 슬라이드 개요: http://localhost:3030/overview/
- 내보내기: http://localhost:3030/export/

슬라이드 파일을 수정하면 자동으로 새로고침됩니다.

### 3. 새 슬라이드 생성

```bash
# 자동 생성 스크립트 사용
./scripts/create-slide.sh my-presentation

# 그 후 실행
npm run dev -- slides/my-presentation/slides.md
```

### 4. 내보내기

```bash
# PDF 내보내기
npm run export:pdf -- slides/kubernetes-basics/slides.md

# PPTX 내보내기
npm run export:pptx -- slides/kubernetes-basics/slides.md

# 모든 슬라이드 한번에 내보내기
./scripts/export-all.sh
```

### 5. 슬라이드 검토 (AI Agent)

```bash
# AI Agent를 통한 슬라이드 검토
./scripts/review-slide.sh kubernetes-basics
./scripts/review-slide.sh 20260124-aws-builders-day
```

Agent가 슬라이드를 분석하여 다음을 제공합니다:
- 구조, 명확성, 기술적 정확성 평가
- 네이밍 컨벤션 준수 여부 확인
- 강점, 개선 사항, 구체적 제안

> **참고:** Agent 사용을 위해 AWS Bedrock 자격 증명이 필요합니다.

### 6. 정적 사이트 빌드

```bash
# 특정 슬라이드 빌드
npm run build -- slides/kubernetes-basics/slides.md
```

## 스크립트

| 스크립트 | 설명 |
|---------|------|
| `./scripts/create-slide.sh <이름>` | 새 슬라이드 생성 |
| `./scripts/review-slide.sh <이름>` | AI Agent로 슬라이드 검토 |
| `./scripts/export-all.sh` | 모든 슬라이드 내보내기 |

## 슬라이드 관리

- 각 슬라이드는 `slides/` 폴더 내 독립적인 폴더로 관리됩니다
- 각 폴더는 자체 `slidev.config.ts`를 가져 독립적으로 커스터마이징 가능합니다
- GitHub에 커밋하여 버전 관리합니다

## 배포

### GitHub Pages 자동 배포

`main` 브랜치에 푸시하면 GitHub Actions가 자동으로 모든 슬라이드를 빌드하고 배포합니다.

**설정 방법:**
1. GitHub repo → Settings → Pages
2. Source: "GitHub Actions" 선택

**배포 URL:**
- 인덱스: `https://username.github.io/repo-name/`
- 개별 슬라이드: `https://username.github.io/repo-name/슬라이드명/`

**수동 배포:**
Actions 탭에서 "Deploy Slides to GitHub Pages" 워크플로우를 수동 실행할 수 있습니다.

### 로컬 빌드

```bash
# 특정 슬라이드 빌드
npm run build -- slides/kubernetes-basics/slides.md
```

### 웹 배포

빌드된 정적 파일을 Vercel, Netlify 등에 배포할 수 있습니다.

## 참고

- [Slidev 공식 문서](https://sli.dev)
- [Slidev 테마](https://sli.dev/themes/gallery.html)
