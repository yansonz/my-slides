---
theme: default
title: Kiro로 발표 준비하기
info: |
  ## Kiro로 발표 준비하기
  리서치, 장표 생성, 리뷰, 발표자노트 생성
author: Yan So
date: 2026-02-12
css: unocss
---

<script setup>
import './style.css'
</script>

# Kiro로 발표 준비하기

12 Feb 2026

<div class="absolute bottom-10">
  <span class="font-700">
    Yan So
  </span>
</div>

---

## 목차
<br>

- 발표 준비 과정과 페인포인트
- 왜 Slidev인가?
- Slidev + Kiro 조합
- 발표 준비 전략
- 데모

---

## 발표 준비 과정
<br>

```
리서치 → 슬라이드 만들기 → 발표자노트 작성 → 발표 연습
```

<br>

- 각 단계마다 시간이 걸리고, 반복 작업이 많음
- AI 코딩 도구로 이 과정을 얼마나 줄일 수 있을까?

---

## 슬라이드 만들기 과정의 페인포인트
<br>

- 슬라이드 디자인에 신경 쓰지 않지만 행사마다 템플릿이나 작성 가이드가 있는 경우가 있음
- 텍스트뿐만 아니라 전체적인 슬라이드의 포맷팅과 일관성 유지 해야 함
- 내용 변경 시 재작성해야 함
- 적절한 이미지 삽입과 링크 관리
- AWS 서비스 이름, 기술 용어와 내용 검증
- 발표 시간에 맞는 장표 장수와 구성은?
- 등등의 이유로 시작하기 귀찮고 미룸

---

## 발표자노트의 페인포인트
<br>

- 구어체로 자연스럽게 작성해야 함
- 슬라이드 내용과 싱크 맞추기
- 내용 변경되면 노트도 다시 작성

<br>

> 💡 이 반복 작업들을 Kiro가 도와줄 수 있다면?

---

## Slidev란?
<br>

개발자용 Markdown 기반 슬라이드 프레임워크 (오픈소스)

- PPT, Keynote 대신 Markdown으로 발표 자료 작성
- Vue, UnoCSS, Vite 기반 웹 렌더링
- 코드 하이라이팅, 라이브 코딩, 녹화 등 개발자 친화 기능

<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://sli.dev" target="_blank">sli.dev</a>
</div>

---

## 왜 Slidev인가?
<br>

생성형 AI로 최종 사용할 슬라이드를 one-shot으로 생성하는 것은 한계가 있음

프롬프트로 의도한 방향으로 재작업하기가 어려움

<br>

- Slidev: Markdown → 슬라이드 렌더링
- LLM 모델: 내 생각 → Markdown으로 변환하기 쉬움
- 실행 결과가 매번 같아야 하는 부분을 코드로 제어 가능 (레이아웃, 이미지, 테이블 등)

<br>

> Markdown 기반이라 AI와 궁합이 좋다

---

## Slidev + Kiro 조합
<br>

<div class="text-sm">

| 역할 | 도구 | 설명 |
|------|------|------|
| 내 생각 → Markdown | AI 모델 | 구조화된 텍스트 생성 |
| Markdown → 슬라이드 | Slidev | 코드 기반 렌더링 |
| End-to-End 관리 | Kiro | 프로젝트 전체 워크플로우 |

</div>

<br>

- Steering으로 슬라이드 패턴 가이드 적용
- Hooks로 변경 시 자동 문서 업데이트
- Powers로 AWS 내용 검증

---

## Kiro가 도와주는 것들
<br>

<div class="text-sm">

| 작업 | Kiro 기능 | 설명 |
|------|----------|------|
| 리서치 | Web Tool, Powers | Web Search, AWS Documentation MCP |
| 장표 생성 | LLM 모델 | 메모 → 슬라이드 초안 자동 생성 |
| 포맷 일관성 | Steering | 슬라이드 패턴 가이드 자동 적용 |
| 내용 검증 | Powers, Sub Agent | AWS 서비스명, 기술 용어 확인 |
| 발표자노트 | LLM 모델 | 슬라이드 기반 구어체 스크립트 생성 |
| 이미지 관리 | Steering | S3 + CloudFront 이미지 서버 연동 |
| 스크립트 자동 업데이트 | Hook | 슬라이드 내용 변경 시 발표자 스크립트 자동 반영 |

</div>

---

## 이미지 & 호스팅
<br>

<div class="grid grid-cols-[6fr_4fr] gap-4">
<div>

- GitHub Pages로 슬라이드 호스팅 (무료!)
- https://slides.yanbert.com 에 아카이빙
- 이미지 전용 S3 + CloudFront 서버 구축
  - https://images.yanbert.com

<br>

> 슬라이드도 코드처럼 버전 관리하고 배포한다

</div>
<div>

<img src="https://images.yanbert.com/my-slides/images/20260212-kiro-krug-make-slides-with-kiro/image-server-architecture.webp" class="w-full h-100 object-contain">

</div>
</div>

---

## 발표 준비 전략
<br>

AI로 시작의 두려움, 귀찮음을 이겨내고 일단 전체 슬라이드 초안을 만든다

<br>

1. 메모로 핵심 내용 정리
2. Kiro에게 슬라이드 초안 생성 요청
3. 리뷰하면서 내 것처럼 고쳐나간다
4. 발표자노트 생성 요청
5. 연습하면서 최종 다듬기

<br>

> 핵심: AI는 초안 생성기, 최종 판단은 내가 한다

---

## 데모
<br>

💻 메모에서 슬라이드까지, Kiro로 만드는 과정

---

## 감사합니다!

질문이 있으신가요? 👻
