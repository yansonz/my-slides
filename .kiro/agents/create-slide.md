# 슬라이드 생성 Skill

## 목적
이 프로젝트에서 새로운 Slidev 발표 슬라이드를 생성하는 방법을 안내합니다.

## 절차

### 1. 스크립트 실행
프로젝트 루트에서 실행합니다.

```bash
./scripts/create-slide.sh <슬라이드-이름>
```

폴더명은 날짜-설명 형식을 따릅니다:

```
YYYYMMDD-<짧은-설명>
```

예시:
- `20260603-aws-summit-korea`
- `20260603-kiro-demo`
- `20261201-re-invent-recap`

### 2. slides.md에 제목만 업데이트
스크립트가 생성한 기본 파일을 그대로 두고, frontmatter의 `title`과 첫 슬라이드 제목(`# 발표 제목`)만 실제 발표 제목으로 바꿉니다.

`slidev.config.ts`의 `title`도 동일하게 수정합니다.

### 3. 로컬 개발 서버 실행 안내
슬라이드 확인은 터미널에서 직접 실행하세요:

```bash
npm run dev -- slides/<슬라이드-이름>/slides.md
```

> ⚠️ 장시간 실행 명령이므로 Kiro가 직접 실행하지 않고 사용자에게 안내만 합니다.

## 생성되는 파일 구조

```
slides/<슬라이드-이름>/
├── slides.md          # 메인 슬라이드 파일
├── style.css          # 슬라이드 스타일
├── slidev.config.ts   # Slidev 설정
├── public/            # 정적 파일 (로컬 개발 전용)
└── components/        # Vue 커스텀 컴포넌트
```

## 주의사항

- 기본 슬라이드 생성이 목적이므로 내용을 채우지 않습니다. 제목만 반영합니다.
- 스크립트는 프로젝트 루트(`/Users/yanso/Projects/my-slides`)에서 실행합니다.
- `public/` 폴더는 로컬 개발 전용입니다. 배포 시 이미지는 이미지 서버(images.yanbert.com)를 사용합니다.
