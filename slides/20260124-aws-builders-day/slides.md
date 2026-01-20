---
theme: default
title: 2026 신규 AI서비스와 트렌드 살펴보기
info: |
  AWS Builders Day 2026 발표자로 참가
  https://event-us.kr/awskrug/event/118695
author: Yan So
date: 2026-01-24
background: https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg1.webp
---

## 2026 AWS 신규 AI서비스와 트렌드 살펴보기
AWS re:Invent 2025 reCap

<div class="absolute bottom-10 right-10 text-right">
  <span class="font-700">
    Yan So<br>
    AWS Hero
  </span>
</div>

---

## 발표자 소개
<br>

### Yan So
<br>

<div class="grid grid-cols-10 gap-8">
<div class="col-span-4">

- AWS Hero
- AWS한국사용자모임 운영진
  - #kiro #data
- 링크드인
<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/qr_linkedin.webp" class="h-40">

</div>
<div class="col-span-6 flex items-center justify-center">
<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/profile.webp">
</div>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## 오늘의 Agenda
<br>

1. Amazon Bedrock AgentCore - 에이전트 플랫폼
2. Amazon Nova 2 모델 패밀리
3. Amazon Nova Act - 브라우저 자동화 에이전트
4. Amazon Nova Forge - 커스텀 프론티어 모델
5. 기타 AI 서비스 업데이트

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## AI 에이전트의 안전 문제
<br>

### 왜 에이전트 안전이 중요한가?
<br>

<div class="grid grid-cols-2 gap-8 w-full">
<div>

### 에이전트의 강력함
- 동적으로 목표 달성 방법 탐색
- 높은 적응성과 유연성
- 복잡한 워크플로우 자동화

</div>
<div>

### 예측 불가능한 위험
- 런타임 동작의 비결정성
- 의도 범위를 벗어난 행동 시도
- 민감 데이터 접근/수정
- 비즈니스 규칙 오해

</div>
</div>

<br>

> 핵심 질문: 자유를 부여하면서도 의도된 경계 내에서 안전하게 행동하도록 보장하는 방법은?

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## AgentCore 다층적 안전 프레임워크
<br>

### 격리(Contain) → 통제(Control) → 검증(Verify)
| 계층 | 서비스 | 역할 |
|-----|-------|------|
| 1 | **Runtime** | 실행 환경 격리 (Firecracker microVM) |
| 2 | **Gateway + Policy** | 도구 접근 제어 및 정책 강제 |
| 3 | **Identity** | 신원 관리 및 권한 전파 |
| 4 | **Observability** | 활동 추적 및 디버깅 |
| 5 | **Evaluations** | 수행 결과 검증 |

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## AgentCore Runtime
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/AIM3330_01.webp" class="h-90 mx-auto">
<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://www.youtube.com/watch?v=ymwpOYMg1ng" target="_blank">AIM3330 - Keep Your Agents Out of Trouble with Amazon Bedrock AgentCore</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## AgentCore Runtime
<br>

### Firecracker microVM 기반 강력한 격리
<br>

<div class="grid grid-cols-2 gap-8 w-full">
<div>

### 세션별 완전 격리
- 자체 메모리, 파일시스템, CPU
- 다른 세션과 공유 없음
- 경계 넘나들기 불가능

</div>
<div>

### 클린룸 환경
- 세션 종료 시 모든 것 제거
- 잔여 데이터/컨텍스트 없음
- 교차 발화(cross-firing) 방지

</div>
</div>

<br>

> 적대적 공격이 있더라도 데이터 접근이나 세션간 원치 않는 교차 발화 불가능

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## AgentCore Gateway
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/AIM3330_02.webp" class="h-90 mx-auto">
<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://www.youtube.com/watch?v=ymwpOYMg1ng" target="_blank">AIM3330 - Keep Your Agents Out of Trouble with Amazon Bedrock AgentCore</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## AgentCore Gateway
<br>

### MCP 규격 완전 호환되는 도구 게이트웨이
<br>

<div class="grid grid-cols-2 gap-8 w-full">
<div>

### 도구 큐레이션
- 최소 권한 원칙 적용
- API, Lambda, MCP 타겟 지원
- 에이전트별 도구 세트 정의

</div>
<div>

### 세분화된 접근 제어
- Lambda 인터셉터 (전/후 처리)
- 비즈니스 로직 규칙 적용
- 에이전트 코드 외부에서 통제

</div>
</div>

<br>

> 예: 환불을 주지 않아야 하는 챗봇에게는 환불 도구를 제공하지 않음

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## AgentCore Policy
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/AIM3330_06.webp" class="h-90 mx-auto">
<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://www.youtube.com/watch?v=ymwpOYMg1ng" target="_blank">AIM3330 - Keep Your Agents Out of Trouble with Amazon Bedrock AgentCore</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## AgentCore Policy
<br>

### Cedar 기반 결정론적 행동 제어
<br>

<div class="grid grid-cols-2 gap-8 w-full">
<div>

### 정책 작성
- 자연어 → Cedar 정책 자동 변환
- "보장 금액 $500만 미만만 허용"
- "finance 부서만 위험 모델링 가능"

</div>
<div>

### 정책 적용
- Gateway가 모든 도구 호출 인터셉트
- 실시간 허용/거부 결정
- 모든 결정 Observability에 로깅

</div>
</div>

<br>

> 에이전트는 사용 불가 도구를 보지 못함 -> 환각/루프 방지

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## AgentCore Identity
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/AIM3330_03.webp" class="h-90 mx-auto">
<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://www.youtube.com/watch?v=ymwpOYMg1ng" target="_blank">AIM3330 - Keep Your Agents Out of Trouble with Amazon Bedrock AgentCore</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## AgentCore Identity
<br>

### 에이전트 신원(Identity) 전파와 권한 제어
<br>

<div class="grid grid-cols-20 gap-8 w-full">
<div class="col-span-9">

### 세 가지 목적
- 에이전트에게 신원 부여
- 인바운드 인증 (자체 IDP 연동)
- 아웃바운드 인증 관리

</div>
<div class="col-span-11">

### 자격 증명 관리
- 토큰 관리 및 자격 증명 교환
- 에이전트는 자격 증명에 직접 접근 불가
- 대신 작업하는 신원의 토큰만 사용

</div>
</div>

<br>

> 여러 사용자 대신 작업 시 교차 간섭 방지

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## AgentCore Observability
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/AIM3330_04.webp" class="h-90 mx-auto">
<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://www.youtube.com/watch?v=ymwpOYMg1ng" target="_blank">AIM3330 - Keep Your Agents Out of Trouble with Amazon Bedrock AgentCore</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## AgentCore Observability
<br>

### 에이전트 활동 추적 및 디버깅
<br>

<div class="grid grid-cols-2 gap-8 w-full">
<div>

### 추적 정보
- 모든 세션 추적 (도구/LLM 호출)
- CloudWatch 로그 쿼리
- 토큰 사용량, 도구 실패율

</div>
<div>

### 미리 만들어진 대시보드
- 4xx, 5xx 오류 모니터링
- 정책 허용/거부 분포
- 시간별 성능 추이

</div>
</div>

<br>

> 무엇이 일어나는지는 알 수 있지만, 무엇이 옳고 그른지는 Evaluation이 담당

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## AgentCore Evaluations
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/AIM3330_05.webp" class="h-90 mx-auto">
<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://www.youtube.com/watch?v=ymwpOYMg1ng" target="_blank">AIM3330 - Keep Your Agents Out of Trouble with Amazon Bedrock AgentCore</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## AgentCore Evaluations
<br>

### 에이전트 수행 결과 검증
<br>

<div class="grid grid-cols-2 gap-8 w-full">
<div>

### 13가지 사전 구축 평가자
- 정확성 (Correctness)
- 도움 정도 (Helpfulness)
- 유해성 (Harmfulness)
- 도구 선택 정확도

</div>
<div>

### LLM as Judge
- 세션 추적 기반 자동 채점
- 사용자 정의 평가자 작성 가능
- 온라인/오프라인 평가 지원

</div>
</div>

<br>

> 도구 호출 성공 ≠ 에이전트가 유용했거나 목표 달성

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## AgentCore 주요 특징
<br>

### 엔터프라이즈급 기능
<br>

- 8시간 실행 윈도우 (업계 최장)
- 세션 격리 (microVM)
- VPC 지원
- Agent-to-Agent (A2A) 프로토콜 지원
- Model Context Protocol (MCP) 서버 연결
- OAuth 서비스 네이티브 통합

<br>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## AgentCore 주요 특징
<br>

### 프레임워크 독립적
<br>

- LangGraph, Strands, CrewAI 등 오픈소스 프레임워크 지원
- 어떤 LLM과도 호환
- HTTP API + WebSocket 실시간 스트리밍
- 100MB 페이로드 처리 (멀티모달)

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## AgentCore 다이어그램
<br>

<div class="grid grid-cols-10 gap-4 w-full">
<div class="col-span-7">

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/AIM3330_07.webp" class="h-90 mx-auto">

</div>
<div class="col-span-3 flex items-center justify-center">

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/diagram1.webp" class="h-100 mx-auto">

</div>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## 추천세션
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/AIM3330.webp" class="h-90 mx-auto">
<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://www.youtube.com/watch?v=ymwpOYMg1ng" target="_blank">AIM3330 - Keep Your Agents Out of Trouble with Amazon Bedrock AgentCore</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## Amazon Nova 2 모델 패밀리
<br>

### 차세대 파운데이션 모델

- Nova 2 Lite: 일상 업무를 위한 빠르고 비용 효율적인 추론 모델
- Nova 2 Pro (Preview): 복잡한 에이전틱 태스크를 위한 고급 모델
- Nova 2 Sonic: 대화형 AI를 위한 음성-음성 모델
- Nova 2 Omni: 멀티모달 추론 + 이미지 생성 올인원 모델

<br>

### Nova2를 고려해야하는 현실적인 이유
- 경쟁 모델 (GPT5, Cluade4.5 시리즈) 대비 압도적 가성비
- 1M 토큰 지원, 멀티모달

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## Amazon Nova 2 모델 패밀리
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/AIM3324_01.webp" class="h-90 mx-auto">
<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://www.youtube.com/watch?v=-nMiqOgQbHc&t=1s" target="_blank">AIM3324 - Amazon Nova 2 Omni: A new frontier in multimodal AI</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## Amazon Nova 2 모델 패밀리
<br>

<div class="text-sm">

| 등급 | 모델명 | 입력비용 (1M 기준) | 출력비용 (1M 기준) | 비고 |
|-----|-------|-----------------|------------------|------|
| 최상위 (Flagship) | Nova 2 Pro | $1.25 | $11.00 | GPT-5와 유사한 수준 |
| | Claude 4.5 Opus | $5.00 | $25.00 | 최고가, 정밀 추론 특화 |
| | GPT-5 (Standard) | $1.25 | $10.00 | 가장 균형 잡힌 고성능 |
| 중급 (Balanced) | Nova 2 Lite | $0.15 | $1.25 | 동급 최저가 (압도적 가성비) |
| | Claude 4.5 Sonnet | $3.00 | $15.00 | 코딩 및 에이전트 인기 모델 |
| 경량 (Lite/Mini) | Nova 2 Micro | $0.035 | $0.14 | 실시간 초저가 처리용 |
| | Claude 4.5 Haiku | $1.00 | $5.00 | - |
| | GPT-5 Mini | $0.25 | $2.00 | - |

</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## Nova 2 Lite 주요 특징
<br>

<div class="grid grid-cols-10 gap-8 w-full">
<div class="col-span-6">

### 기능
- Extended Thinking (단계별 추론)
- 100만 토큰 컨텍스트 윈도우
- 텍스트, 이미지, 비디오, 문서 입력 지원
- 내장 도구
  - Code Interpreter
  - Web Grounding

</div>
<div class="col-span-4">

### 활용 사례
- 고객 서비스 챗봇
- 문서 처리 자동화
- 비즈니스 프로세스 자동화
- 소프트웨어 엔지니어링

</div>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## Nova 2 Lite 주요 특징
<br>

### Ko-AgentBench (한국어 환경) 결과
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/table1.webp" class="h-75 mx-auto">
<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://blog.wisen.co.kr/reinvent-2025-%ED%95%9C%EA%B5%AD%EC%96%B4-%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8-%EB%B2%A4%EC%B9%98%EB%A7%88%ED%81%AC%EB%A1%9C-aws-nova-2-lite-%EC%84%B1%EB%8A%A5-%EC%8B%AC%EC%B8%B5-%EB%B6%84%EC%84%9D" target="_blank"> 한국어 에이전트 벤치마크로 Amazon Nova 2 Lite 성능 심층 분석</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## Nova 2 Sonic - 음성 AI
<br>

### 차세대 Speech-to-Speech 모델

- 자연스러운 실시간 음성 대화
- 30개 이상 언어 지원
- 자연스러운 턴테이킹 및 중단 처리
- 8KHz 전화 음성 입력 지원
- 텍스트 <-> 음성 크로스모달 전환 지원

<br>

> Amazon Connect와 통합하여 30개 이상 언어로 자연스러운 대화 제공

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## Amazon Nova Act
<br>

### 브라우저 UI 자동화 에이전트

- SDK 형태로 제공
- Nova 2 Lite 기반 커스텀 모델
- 자연어 + Python 코드로 워크플로우 정의
- 90% 이상의 태스크 신뢰성
- Strands Agents 프레임워크 통합

<br>

> 한국 지역 지원 안함

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---


## Amazon Nova Act 데모
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/demo.webp" class="h-90 mx-auto">

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## Nova Act 활용 사례
<br>

<div class="grid grid-cols-2 gap-8 w-full">
<div>

### QA 테스트 자동화
- 동적 UI 테스트 케이스 실행
- 복잡한 시나리오 자동 탐색
<br><br>

### 데이터 추출
- 웹 소스에서 정보 수집/통합
- 검색 결과 탐색 및 필드 추출

</div>
<div>

### 폼 자동 입력
- 반복적인 양식 작성 자동화
- 분산된 시스템 간 데이터 입력
<br><br>
### 예약/구매 자동화
- 쇼핑, 예약, 부킹 워크플로우
- 대규모 자율 처리

</div>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## Amazon Nova Forge
<br>

### 나만의 프론티어 모델 구축
<br>

<div class="grid grid-cols-2 gap-8 w-full">
<div>

### Nova Forge란?
- 기업 고유 IP를 활용한 프론티어 모델 구축 서비스
- 모델 개발 비용 절감 및 시간 단축
- RAG/파인튜닝의 한계를 넘어선 접근

</div>
<div>

### 기존 접근 방식의 한계
- **RAG**: IP가 모델에 내재화되지 않음
- **LoRA 파인튜닝**: 기능 향상에 한계
- **계속된 사전 학습**: 치명적 망각 위험
- **자체 모델 구축**: 비용과 시간 막대

</div>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## Nova Forge 핵심 이점
<br>

<div class="grid grid-cols-2 gap-8 w-full">
<div>

### 단계별 체크포인트 접근
- Pre-training, Mid-training, Post-training 모든 단계 접근
- 보유 데이터 종류/양에 따라 적절한 시작점 선택
- 학습률이 높은 상태에서 시작 가능

<br>

### 치명적 망각 방지
- Nova 큐레이션 데이터와 고객 데이터 혼합
- 기초 역량 유지하면서 도메인 특화
</div>
<div>

### 자체 환경 연동 RL
- 자체 엔드포인트/오케스트레이터 연동
- 다단계 에이전트 학습 지원
- 독점 시뮬레이션 환경 활용

<br><br>

### SageMaker Hyperpart 레시피
- ML 전문가 아니어도 쉬운 훈련
- Nova 데이터 혼합 비율 최적화
- 스마트 기본값 제공
</div>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## Nova Forge 학습 단계
<br>

### 4단계 커스터마이징
<br>

| 단계 | 설명 | 데이터 유형 |
|-----|------|-----------|
| **1. Pre-training** | 도메인 기초 지식 학습 | 대량 비정형 데이터 |
| **2. Mid-training** | 특정 분야 이해 강화 | 독점 데이터 + Nova 데이터 |
| **3. SFT** | 응답 패턴 학습 (복종 훈련) | 명령어-응답 쌍 |
| **4. RL** | 실제 환경에서 행동 정제 | 보상 신호 기반 |

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## Nova Forge 가격

<br>

<div class="flex flex-col items-center gap-4">

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/nova-forge-price.webp" class="h-50 mx-auto">

<span class="text-8xl">🤦‍♂️</span>

</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## 추천워크샵
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/workshop1.webp" class="h-90 mx-auto">
<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://github.com/aws-samples/sample-building-intelligent-multimodal-applications-with-Nova" target="_blank">Building Intelligent Multimodal Applications with Amazon Nova2 Omni</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## 기타 AI 서비스 업데이트
<br>

<div class="grid grid-cols-2 gap-8 w-full">
<div>

### Amazon Bedrock
- OpenAI GPT OSS 모델 지원
- Guardrails 코딩 유스케이스 지원
- 10개 추가 언어 음성 분석

<br>

### Amazon Q
- 개발자 생산성 향상
- 코드 변환 자동화

</div>
<div>

### AWS Transform
- AI 기반 코드 모더나이제이션
- 메인프레임 Reimagine 기능
- Windows 풀스택 모더나이제이션

<br>

### AWS Security Agent
- 애플리케이션 보안 사전 대응
- GuardDuty 확장 위협 탐지

</div>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## Kiro - AI 에이전트 기반 개발 도구
<br>

### 소프트웨어 개발의 패러다임 전환
- 단순 코딩 보조 → 완전한 협업 파트너
- 아이디어 구상 → 요구사항 → 태스크 → 실행까지 전 과정 지원
- 개발자 생산성 5~20배 향상 가능

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## Kiro - Spec-Driven Development
<br>

### 스펙 기반 개발이란?
<br>

<div class="grid grid-cols-2 gap-8 w-full">
<div>

### 기존 방식의 문제
- 전략적 결정이 나중에 내려짐
- 맥락 손실 (왜 그렇게 했는지 잊음)
- 유지보수 어려움

</div>
<div>

### Spec-Driven 방식
- 고가치 전략적 결정을 앞당김
- 구조화된 요구사항/설계 문서화
- 에이전트가 실행 담당

</div>
</div>

<br>

> 프롬프트 → 요구사항 → 설계 → 코드/테스트/문서 자동 생성

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## Kiro - 주요 기능
<br>

<div class="grid grid-cols-2 gap-8 w-full">
<div>

### 개발 환경
- IDE (VS Code 기반)
- CLI (터미널 환경)
- 멀티모달 입력 (이미지, 다이어그램)

<br>

### 에이전트 기능
- Agent Hooks (백그라운드 자동화)
- Custom Agents (특화 에이전트)
- Kiro Powers (도구 연동 시스템)

</div>
<div>

### 모델 지원
- Claude Sonnet 4.5
- Claude Opus 4.5
- 품질/속도/비용 선택 가능

<br>

### 협업
- 스티어링 파일 (팀 표준)
- MCP 서버 연동
- 14,000+ Discord 커뮤니티

</div>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## Kiro Powers
<br>

### 에이전트에게 특화 기능 제공

- MCP 서버 + 스티어링 파일 + 훅을 패키지로 번들링
- 도메인별 맥락과 도구를 동적 로드
- 토큰 사용 효율화

<br>

### 파트너 Powers
- **Figma**: UI 디자인 연동
- **Supabase**: 백엔드 연동
- **Stripe**: 결제 연동
- **Datadog**: 모니터링 연동

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## Kiro Frontier Agents
<br>

### 자율 에이전트의 새로운 등급
<br>

<div class="grid grid-cols-2 gap-8 w-full">
<div>

### 특징
- **자율성**: 목표만 주면 스스로 달성
- **대규모 확장**: 다중 동시 작업
- **지속 학습**: 코드 리뷰로 계속 개선
- **비세션 기반**: 항상 맥락 유지

</div>
<div>

### 3가지 Frontier Agent
- **Kiro Autonomous**: 소프트웨어 개발
- **Security Agent**: 보안 스캔/침투 테스트
- **DevOps Agent**: 사고 대응/예방

</div>
</div>

<br>
<div class="text-sm text-gray-400">
🔗 <a href="https://youtu.be/q3Sb9PemsSo?si=ak9m4fKDYXeb1znD&t=6072" target="_blank">AWS re:Invent 2025 - Keynote with CEO Matt Garman (1:14:12~)</a>
</div>


<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## Kiro - AWS 내부 사례
<br>

### Amazon Bedrock 추론 엔진 재구축
<br>

<div class="text-sm">

| 항목 | 기존 예상 | Kiro 사용 |
|-----|---------|----------|
| 인원 | 30명 | 6명 |
| 기간 | 12~18개월 | 76일 |
| 주간 커밋 | 2회/인 | 40회+/인 |

</div>

<br>

### 성공 비결
1. 작업 기반 → 목표 기반 지시로 전환
2. 동시 AI 작업 확장 (커스텀 에이전트 군단)
3. 단순 코딩 외 전체 SDLC(Software Development Life Cycle)로 AI 활용 확장

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## 추천세션
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/INV205.webp" class="h-90 mx-auto">
<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://www.youtube.com/watch?v=A8BYnqiHfeA" target="_blank">INV205 - Reinventing software development with AI agents</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## Kiro 한국 사용자 모임
<br>

<div class="grid grid-cols-10 gap-8 w-full">
<div class="col-span-7">

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/kiro-welcome.webp" class="h-80 mx-auto">

</div>
<div class="col-span-3 flex items-center justify-center">

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/qr_kiro.webp" class="h-60 mx-auto">

</div>
</div>

<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://kiro.awskr.org" target="_blank">Kiro 한국 사용자 모임</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## 2025 AI 트렌드 요약
<br>

<div class="grid grid-cols-2 gap-8 w-full">
<div>

### 에이전틱 AI 시대
- 단순 생성 → 자율 실행
- 멀티 에이전트 협업
- 프로덕션 레벨 신뢰성

</div>
<div>

### 커스터마이징 심화
- 파인튜닝을 넘어 프리트레이닝까지
- 도메인 특화 모델 구축
- 데이터 주권 확보

</div>
</div>

<br>

> "AI 에이전트를 현실로 만드는 해" - Swami Sivasubramanian

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## AWS re:Invent 2025
<br>

<div class="grid grid-cols-12 grid-rows-2 gap-1 h-115 -mt-8 -mx-12">
  <img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/lv1.webp" class="col-span-2 row-span-2 w-full h-full object-cover">
  <img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/lv2.webp" class="col-span-4 w-full h-full object-cover">
  <img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/lv4.webp" class="col-span-4 w-full h-full object-cover">
  <img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/lv3.webp" class="col-span-2 row-span-2 w-full h-full object-cover">
  <img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/lv5.webp" class="col-span-4 w-full h-full object-cover">
  <img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/lv6.webp" class="col-span-2 w-full h-full object-cover">
  <img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/lv7.webp" class="col-span-2 w-full h-full object-cover">
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## AWS re:Invent 참가 의미
<br>

### 2018년부터 매년 참석 이유?
<br>

- 글로벌 기술 트렌드 현황과 미래를 엿볼 수 있음 (키노트)
- 관심 주제 집중 학습 기간 (세션)
- 사용하는 제품 회사와의 만남 (엑스포)
- 개발자 네트워킹 (AWS라는 공통 주제)
- 열심히 달려온 한해를 마무리하는 리프레시 기간 (라스베가스)

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## AWS re:Invent 2026 가는 방법
<br>

- 일정을 비워둔다 (2026/11/30 - 12/4)
- AWS 커뮤니티에 참여한다.
  - [AWS한국사용자모임](https://www.awskr.org)
  - [AWS Community Builder](https://builder.aws.com/post/36vuBgJCWKhXNi9tAEhLp4ADn2x_p/welcome-to-the-community-reinvent-recaps-space)
  (신규신청마감됨 ~1/21)
  - [AUSG](https://ausg.me/)
  - [AWS Cloud Clubs](https://builder.aws.com/community/cloud-clubs)
  - AWS Summit Seoul (5월), AWS Community Day (11월)
  - 관심있는 소모임 참석, 발표, 운영 등 활발한 활동
- 프로그램별 여러 혜택과 기회 제공

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

---

## QnA
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/qr_qna.webp" class="h-60">

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>