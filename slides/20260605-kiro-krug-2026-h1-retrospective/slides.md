---
theme: default
title: Kiro 한국 사용자 모임 2026 상반기 회고
info: |
  ## Kiro 한국 사용자 모임 2026 상반기 회고
  밋업 운영 돌아보기
author: Yan So
date: 2026-06-05
css: unocss
---

<script setup>
import './style.css'
</script>

# Kiro 한국 사용자 모임
## 2026 상반기 회고

05 Jun 2026

<div class="absolute bottom-10">
  <span class="font-700">
    Yan So
  </span>
</div>

---

## 목차
<br>

- Kiro 런칭 타임라인
- 모임 소개
- 2026 상반기 활동
- 운영 이모저모
- 현재 고민과 향후 계획

---

## Kiro 런칭 타임라인
<br>

<div class="text-sm">

| 시기 | 내용 |
|------|------|
| 2025 상반기 | AWS 내부 프로젝트 "Kiro" 개발 중 보도 |
| 2025-07-14 | **Public Preview** 공개 — AWS Agentic IDE |
| 2025-11 | **General Availability(GA)** + Kiro CLI 추가 |
| 2025-12 re:Invent | Powers, Autonomous Agent 등 대규모 기능 발표 |
| 2026 | Amazon Q Developer 신규 가입 종료, Kiro를 차세대 도구로 |
| **2026-01-22** | **Kiro 한국 사용자 모임 첫 밋업** 🎉 |

</div>

---

## 모임 소개
<br>

- **목표**: Kiro 홍보, 노하우 및 사례 공유, 사용자 네트워킹
- **공동 운영**: Yan So + 김현민
  - 관심 있으신 분 연락주세요
- **모임비**: 5,000원 (식사/간식비로 소진)
- **AWSKRUG와 별개**로 유저그룹 등록

---

## 홈페이지
<br>

🏠 홈페이지: <a href="https://kiro.awskr.org" target="_blank">kiro.awskr.org</a>

- 랜딩페이지
- AWSKRUG Slack, Luma 이벤트 페이지 연결 

<img src="https://images.yanbert.com/my-slides/images/20260605-kiro-krug-2026-h1-retrospective/01.webp" class="max-h-64 w-auto mx-auto object-contain">

---

## 이벤트 관리: Luma 사용 중
<br>
🔗 이벤트 등록: <a href="https://luma.com/kiro-krug" target="_blank">luma.com/kiro-krug</a>

<div class="flex gap-4 items-center">
<div>

**좋은 점**
- 관리자 메뉴가 편리함
- 피드백 수집하기 좋음
- 공지(blast) 발송 편리함

</div>
<img src="https://images.yanbert.com/my-slides/images/20260605-kiro-krug-2026-h1-retrospective/2026-06-04_18-00-50.webp" class="h-40 rounded-lg">
</div>

**아쉬운 점**
- 기존 AWSKRUG 대상 홍보 연계 안 됨 → Meetup에 따로 등록 중
- 센터필드 입장 시 Luma QR 사용 시도하는 분이 있음
- 결제기능이 있는데 국내 결제는 안됨

---

## 모임자료 아카이빙
<br>

📦 아카이빙
- 발표자료: <a href="https://github.com/awskrug/kiro-group" target="_blank">github.com/awskrug/kiro-group</a>
- Kiro 이미지: <a href="https://github.com/awskrug/awskrug-digital-assets/tree/master/kiro" target="_blank">github.com/awskrug/awskrug-digital-assets/tree/master/kiro</a> 


<div class="flex gap-4 justify-center items-center">
  <img src="https://images.yanbert.com/my-slides/images/20260605-kiro-krug-2026-h1-retrospective/2026-06-04_18-06-35.webp" class="h-72 object-contain">
  <img src="https://images.yanbert.com/my-slides/images/20260605-kiro-krug-2026-h1-retrospective/2026-06-04_18-07-08.webp" class="h-72 object-contain">
</div>

---

## 2026 상반기 밋업 — 5회 진행
<br>

<div class="text-sm">

| 날짜 | 형태 | 참석자 | 주요 세션 |
|------|------|:------:|----------|
| 01-22 | 밋업 | 32명 | Kiro Powers 소개, AI-Workflow, Kiro 야생 적응기 |
| 02-12 | 밋업 | 39명 | Spec 모드 시행착오, Autonomous 개발, Kiro로 발표준비 |
| 03-19 | 워크샵 | 24명 | Kiro CLI 스펙 기반 개발 실습 |
| 04-23 | 밋업 | 24명 | EKS IP 이슈, IAM 정책 이슈, 아키텍처→개발 (AWS CSE팀) |
| 05-28 | 밋업 | 22명 | Agent 관리 프로그램, AWS 멀티 어카운트 + 침해사고 대응 |

</div>

---

## 01월 첫 밋업 (2026-01-22)
<br>

- **Kiro Powers 소개** — Yan So
- **AI-Workflow를 활용한 개발팀 생산성 올리기** — 권태관(우아한형제들)
- **Kiro 야생 적응기** — 남기웅(브이피피랩)

---

## 02월 밋업 (2026-02-12)
<br>

**메인 세션**
- **프론트엔드 엔지니어 관점 Kiro Spec 모드를 제대로 쓰기 위한 시행착오로 배운 것들** (feat: FSD와 BDD) — 최지연(브로즈)

**라이트닝 토크**
- Spec 기반 Autonomous 개발은 어디까지 가능할까? — 조원상
- Kiro로 Openclaw 호스팅하기 — 김현민
- AI-DLC에 대한 생각 — 윤평호
- Kiro로 발표준비 하기 — Yan So

---

## 03~05월 (2026-03 ~ 05)
<br>

**03월 워크샵**
- Kiro CLI를 활용한 스펙 기반 개발 실습
- 미니세션: Kiro Autonomous Agents 소개와 데모 — 최용호(AWS)

**04월 밋업** — AWS Cloud Support 팀 세션 3개
- EKS IP 부족 이슈 해결, IAM 정책 이슈, 아키텍처로부터 Kiro로 개발하기

**05월 밋업**
- Agent 관리 프로그램 소개 — 서혁범(엑심베이)
- AWS 멀티 어카운트 기술 지원 전략 및 침해사고 대응 고도화 — 허준(메가존)

---

## 운영 이모저모
<br>

- 모임비 5,000원으로 식사/간식 운영
- 호정김밥 가격 상승으로 **모임비 인상 예정**
- AWSKRUG와 별개 유저그룹이지만 협력 관계 유지

<img src="https://images.yanbert.com/my-slides/images/20260605-kiro-krug-2026-h1-retrospective/2026-06-04_18-28-33.webp" class="max-h-80 w-auto mx-auto object-contain">

---

## 현재 고민
<br>

- Kiro 사용자가 많지 않아 **사례, 발표자 찾기가 점점 어려워짐**
- 이를 해결하기 위해 **Kiro 사용자 인터뷰** 시작
  - 우선 매주 1명씩 10명 인터뷰해보자

<img src="https://images.yanbert.com/my-slides/images/20260605-kiro-krug-2026-h1-retrospective/2026-06-04_18-33-07.webp" class="h-90 mx-auto">




---

## 향후 계획
<br>

- 해커톤 진행 예정
- Autonomous Agent GA되면 운동모임+해커톤
- Kiro Power($25) 구독 지원 컨텐츠 참여단
- 소모임 조인트 세션 개최
- 사용자 인터뷰를 통한 커뮤니티 콘텐츠 확보
- 모임비 조정

---

## 감사합니다!
<br>

Kiro 사용자 모임 놀러오세요 👻 