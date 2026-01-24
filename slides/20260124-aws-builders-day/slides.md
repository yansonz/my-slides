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

<!--
안녕하세요, AWS Hero Yan So입니다. 오늘은 re:Invent 2025에서 발표된 신규 AI 서비스와 트렌드를 살펴보겠습니다.
-->

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

<!--
저는 AWS 한국사용자모임에서 Kiro와 Data 소모임을 운영하고 있습니다. 궁금하신 분들은 링크드인으로 연락 주세요.
-->

---

## 오늘의 Agenda
<br>

1. Amazon Bedrock AgentCore - 에이전트 플랫폼
2. Amazon Nova 2 모델 패밀리
3. Amazon Nova Act - 브라우저 자동화 에이전트
4. Amazon Nova Forge - 커스텀 프론티어 모델
5. Kiro - AI 에이전트 기반 개발 도구
6. 기타 AI 서비스 업데이트

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

<!--
오늘 다룰 내용입니다. AgentCore, Nova 2 모델 패밀리, Nova Act, Nova Forge, Kiro, 그리고 기타 업데이트 순으로 진행합니다. 특히 AgentCore와 Nova 2, Kiro에 집중해서 설명드리겠습니다.
-->

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

<!--
에이전트는 강력하지만 예측 불가능합니다. 동적으로 목표를 달성하는 유연성이 장점이지만, 의도치 않은 행동을 할 수 있죠. 민감 데이터에 접근하거나 비즈니스 규칙을 오해할 수 있습니다. 핵심 질문은 '자유를 주면서도 안전하게 제어하는 방법'입니다.
-->

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

<!--
AgentCore는 5개 계층으로 에이전트를 안전하게 관리합니다. 격리, 통제, 검증의 3단계 접근법입니다. Runtime으로 격리하고, Gateway와 Policy로 통제하고, Identity로 신원 관리, Observability로 추적, Evaluations로 검증합니다.
-->

---

## AgentCore Runtime
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/AIM3330_01.webp" class="h-90 mx-auto">
<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://www.youtube.com/watch?v=ymwpOYMg1ng" target="_blank">AIM3330 - Keep Your Agents Out of Trouble with Amazon Bedrock AgentCore</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

<!--
[그림 설명] 왼쪽에서 사용자 요청이 들어오면, 각 요청마다 독립된 microVM 박스가 생성됩니다. 박스 안에 에이전트 코드, 메모리, 파일시스템이 완전히 분리되어 있고, 박스 간에는 화살표가 없습니다 - 즉 서로 통신 불가. 세션 종료 시 박스 전체가 삭제되는 모습을 보여줍니다. 핵심은 '완전 격리'입니다.
-->

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

<!--
각 세션이 자체 메모리, 파일시스템, CPU를 갖습니다. 세션 종료 시 모든 것이 제거되는 클린룸 환경이라 적대적 공격이 있어도 데이터 유출이나 세션 간 교차 발화가 불가능합니다. (커머스 경험 최악의 상황: 남의정보가 보이는거.. CS챗봇 예)
-->

---

## AgentCore Gateway
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/AIM3330_02.webp" class="h-90 mx-auto">
<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://www.youtube.com/watch?v=ymwpOYMg1ng" target="_blank">AIM3330 - Keep Your Agents Out of Trouble with Amazon Bedrock AgentCore</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

<!--
[그림 설명] 에이전트와 외부 도구(API, Lambda, MCP 서버) 사이에 Gateway가 중간 관문 역할을 합니다. 에이전트의 모든 도구 호출이 Gateway를 거쳐야 하고, Gateway에서 '이 에이전트는 이 도구만 사용 가능'이라고 필터링합니다. 마치 공항 보안검색대처럼 모든 요청을 검사하는 구조입니다.
-->

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

> 예: 환불권한이 없는 챗봇에게는 환불 도구를 제공하지 않음

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

<!--
최소 권한 원칙을 적용해서 에이전트별로 필요한 도구만 제공합니다. 예를 들어 환불 권한이 없는 챗봇에게는 환불 도구 자체를 제공하지 않습니다. Lambda 인터셉터는 도구 호출 전후에 커스텀 로직을 끼워넣는 기능입니다. 예를 들어 '주문 취소' 도구를 호출하기 전에 Lambda가 먼저 실행되어 "이 주문이 24시간 이내인지 확인"하고, 24시간이 지났으면 에이전트에게 "취소 불가"라고 알려줍니다. 호출 후에도 Lambda가 실행되어 "취소 완료 로그를 Slack에 전송" 같은 후처리를 할 수 있습니다. 핵심은 에이전트 코드를 수정하지 않고도 비즈니스 규칙을 외부에서 적용할 수 있다는 점입니다.
-->

---

## AgentCore Policy
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/AIM3330_06.webp" class="h-90 mx-auto">
<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://www.youtube.com/watch?v=ymwpOYMg1ng" target="_blank">AIM3330 - Keep Your Agents Out of Trouble with Amazon Bedrock AgentCore</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

<!--
[그림 설명] 그림에서 자연어 정책("senior-adjuster나 manager 역할만 보험 보장 범위를 수정할 수 있다")이 Cedar 코드로 변환되는 흐름을 보여줍니다. Gateway가 도구 호출을 받으면 Policy 엔진에 질의하고, 역할이 맞지 않으면 즉시 거부합니다. 모든 결정이 로그로 남아서 감사(audit) 추적이 가능합니다.

Cedar는 AWS가 만든 오픈소스 정책 언어입니다. Amazon Verified Permissions에서도 사용되는 검증된 기술이죠. 특징은 '결정론적'이라는 점입니다. 같은 입력에 항상 같은 결과를 반환하고, 정책 평가 속도가 밀리초 단위로 빠릅니다. LLM처럼 확률적으로 판단하는 게 아니라 규칙 기반으로 정확하게 허용/거부를 결정합니다. 
-->

---

## AgentCore Policy
<br>

### Cedar 기반 결정론적 행동 제어
<br>

<div class="grid grid-cols-2 gap-8 w-full">
<div>

### 정책 작성
- 자연어 → Cedar 정책 자동 변환
- "환불 금액 10만원 미만만 자동 승인"

```text
permit(principal, 
  action == Action::"refund", 
  resource) 
when { resource.amount < 100000 };
```

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

<!--
정책작성자가 자연어로 정책을 작성하면 Cedar 정책으로 자동 변환됩니다. 예를 들어 '환불 금액 10만원 미만만 자동 승인'이라고 작성하면, Cedar로는 'permit(principal, action == Action::"refund", resource) when { resource.amount < 100000 };' 형태가 됩니다. Gateway가 모든 도구 호출을 인터셉트해서 실시간으로 허용/거부를 결정하고, 에이전트는 사용 불가 도구를 아예 보지 못해서 환각이나 루프를 방지합니다.
-->

---

## AgentCore Identity
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/AIM3330_03.webp" class="h-90 mx-auto">
<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://www.youtube.com/watch?v=ymwpOYMg1ng" target="_blank">AIM3330 - Keep Your Agents Out of Trouble with Amazon Bedrock AgentCore</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

<!--
[그림 설명] 사용자 A, B, C가 각각 에이전트에게 작업을 요청하면, Identity 서비스가 각 사용자의 토큰을 관리합니다. 에이전트는 '사용자 A 대신 작업 중'이라는 토큰만 받고, 실제 자격증명(비밀번호, API키)에는 접근 못합니다. 사용자별로 권한이 분리되어 A의 작업이 B의 데이터에 접근 불가합니다.
-->

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

<!--
에이전트에게 신원을 부여하고, 인바운드/아웃바운드 인증을 관리합니다. 에이전트는 자격 증명에 직접 접근하지 못하고, 대신 작업하는 사용자의 토큰만 사용합니다.
-->

---

## AgentCore Observability
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/AIM3330_04.webp" class="h-90 mx-auto">
<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://www.youtube.com/watch?v=ymwpOYMg1ng" target="_blank">AIM3330 - Keep Your Agents Out of Trouble with Amazon Bedrock AgentCore</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

<!--
[그림 설명] 에이전트의 모든 활동(LLM 호출, 도구 사용, 정책 결정)이 타임라인으로 기록됩니다. CloudWatch 대시보드에서 토큰 사용량 그래프, 도구별 성공/실패율 차트, 정책 허용/거부 비율 파이차트를 볼 수 있습니다. 문제 발생 시 특정 세션의 전체 흐름을 추적해서 디버깅 가능합니다.
-->

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

<!--
도구 호출, LLM 호출, 토큰 사용량, 실패율 등을 CloudWatch로 모니터링할 수 있고, 미리 만들어진 대시보드도 제공됩니다. 다만 무엇이 옳고 그른지는 Evaluation이 담당합니다.
-->

---

## AgentCore Evaluations
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/AIM3330_05.webp" class="h-90 mx-auto">
<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://www.youtube.com/watch?v=ymwpOYMg1ng" target="_blank">AIM3330 - Keep Your Agents Out of Trouble with Amazon Bedrock AgentCore</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

<!--
[그림 설명] 에이전트 세션이 끝나면 Evaluations가 전체 대화와 행동을 분석합니다. LLM이 심판 역할을 해서 '정확성 85점, 유해성 0점, 도움 정도 90점' 같은 점수를 매깁니다. 도구 호출은 성공했지만 실제로 사용자 목표를 달성했는지, 유해한 응답은 없었는지를 검증하는 최종 관문입니다.
-->

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

<!--
정확성, 유해성, 도구 선택 정확도 등 13가지 사전 구축 평가자가 있고, LLM as Judge 방식으로 자동 채점합니다. 도구 호출이 성공했다고 에이전트가 유용했거나 목표를 달성한 건 아니니까요.
-->

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

<!--
엔터프라이즈급 기능을 하나씩 살펴보겠습니다. 8시간 실행 윈도우는 업계 최장입니다. 복잡한 데이터 분석이나 대규모 코드 리팩토링처럼 오래 걸리는 작업도 중단 없이 처리할 수 있습니다. 세션 격리는 앞서 설명드린 Firecracker microVM 기반이고, VPC 지원으로 프라이빗 네트워크 내에서 안전하게 운영 가능합니다. A2A 프로토콜은 에이전트 간 통신 표준으로, 여러 에이전트가 협업하는 멀티 에이전트 시스템 구축에 필수입니다. MCP 서버 연결로 외부 도구와 쉽게 통합하고, OAuth 네이티브 통합으로 Google, Slack 등 서드파티 서비스 인증도 간편합니다.
-->

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

<!--
프레임워크 독립적이라는 점이 AgentCore의 큰 장점입니다. 이미 LangGraph나 CrewAI로 에이전트를 만들어 두셨다면, 코드 수정 없이 AgentCore 위에서 실행할 수 있습니다. AWS Strands도 지원하고, 어떤 LLM이든 호환됩니다. Bedrock 모델뿐 아니라 OpenAI, Anthropic API도 사용 가능합니다. HTTP API와 WebSocket 실시간 스트리밍을 지원해서 응답을 기다리지 않고 바로바로 출력할 수 있고, 100MB 페이로드 처리로 이미지나 비디오 같은 멀티모달 입력도 문제없습니다.
-->

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

<!--
[그림 설명] 전체 흐름을 한눈에 보여드립니다. 사용자 요청 → Runtime(격리된 실행환경) → Gateway(도구 접근 관문) → Policy(정책 검사) → Identity(권한 확인) → 외부 도구 실행. 모든 과정이 Observability로 기록되고, 최종적으로 Evaluations가 품질을 검증합니다. 5개 계층이 겹겹이 에이전트를 감싸는 '양파 구조'라고 생각하시면 됩니다.
-->

---

## 추천세션
<br>

<div class="grid grid-cols-10 gap-4 w-full">
<div class="col-span-6">

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/AIM3330.webp" class="h-80 mx-auto">

</div>
<div class="col-span-4 text-sm">

### 세션 개요
- AgentCore의 5가지 핵심 서비스 심층 분석
- Runtime, Gateway, Policy, Identity, Observability, Evaluations 아키텍처
- 실제 데모와 코드 예제
- 에이전트 안전 설계 베스트 프랙티스

</div>
</div>

<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://www.youtube.com/watch?v=ymwpOYMg1ng" target="_blank">AIM3330 - Keep Your Agents Out of Trouble with Amazon Bedrock AgentCore</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

<!--
AgentCore에 대해 더 알고 싶으시면 이 세션을 추천드립니다. AIM3330입니다. 오늘 제가 설명드린 5가지 서비스의 아키텍처와 실제 데모, 코드 예제까지 상세하게 다룹니다.
-->

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

<!--
Nova 2는 차세대 파운데이션 모델입니다. Lite, Pro, Sonic, Omni 4가지가 있습니다. Nova 2를 고려해야 하는 현실적인 이유는 압도적인 가성비입니다. GPT-5나 Claude 4.5 대비 훨씬 저렴하면서 1M 토큰과 멀티모달을 지원합니다.
-->

---

## Amazon Nova 2 모델 패밀리
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/AIM3324_01.webp" class="h-90 mx-auto">
<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://www.youtube.com/watch?v=-nMiqOgQbHc&t=1s" target="_blank">AIM3324 - Amazon Nova 2 Omni: A new frontier in multimodal AI</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

<!--
[그림 설명] Nova 2 모델 패밀리의 전체 라인업을 보여줍니다. 왼쪽부터 Nova 2 Lite(텍스트/이미지/비디오 입력, 텍스트 출력), Nova 2 Pro(복잡한 에이전틱 태스크), Nova 2 Sonic(음성-음성 실시간 대화), Nova 2 Omni(멀티모달 입출력 + 이미지 생성)가 있습니다. 각 모델이 어떤 입력을 받고 어떤 출력을 내는지 아이콘으로 표시되어 있습니다. 용도에 따라 적합한 모델을 선택하시면 됩니다.
-->

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

<!--
가격표를 보시면 Nova 2 Lite가 입력 0.15달러, 출력 1.25달러로 동급 최저가입니다. Claude 4.5 Sonnet이 3달러/15달러인 것과 비교하면 10배 이상 저렴합니다. 비용이 중요한 프로덕션 환경에서 큰 장점입니다.
-->

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

<!--
Nova 2 Lite는 Extended Thinking으로 단계별 추론이 가능하고, 100만 토큰 컨텍스트를 지원합니다. 고객 서비스 챗봇, 문서 처리 자동화, 소프트웨어 엔지니어링 등에 활용할 수 있습니다.
-->

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

<!--
[그림 설명] Ko-AgentBench는 한국어 환경에서 에이전트 성능을 측정하는 벤치마크입니다. 표에서 Nova 2 Lite가 GPT-4o, Claude 3.5 Sonnet과 비교해서 어떤 성능을 보이는지 확인할 수 있습니다. 특히 도구 사용(Tool Use), 계획 수립(Planning), 추론(Reasoning) 영역에서의 점수를 비교해 보세요. 가격 대비 성능을 고려하면 Nova 2 Lite가 한국어 에이전트 구축에 매력적인 선택지입니다.
-->

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

<!--
Nova 2 Sonic은 Speech-to-Speech 모델입니다. 30개 이상 언어로 자연스러운 실시간 음성 대화가 가능하고, Amazon Connect와 통합됩니다. 전화 음성 입력도 지원합니다.
-->

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

<!--
Nova Act는 브라우저 UI 자동화 에이전트입니다. SDK 형태로 제공되고, 자연어와 Python 코드로 워크플로우를 정의합니다. 90% 이상의 태스크 신뢰성을 보여줍니다. 다만 아직 한국 리전은 지원하지 않습니다.
-->

---


## Amazon Nova Act 데모
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/demo.webp" class="h-90 mx-auto">

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

<!--
[그림 설명] Nova Act가 실제로 브라우저를 조작하는 화면입니다. 왼쪽에는 Python 코드로 작성된 워크플로우가 있고, 오른쪽에는 실제 브라우저 화면이 보입니다. 에이전트가 "아마존에서 무선 마우스 검색해서 가격순 정렬 후 첫 번째 상품 장바구니에 담기" 같은 자연어 명령을 받으면, 자동으로 클릭, 입력, 스크롤 등의 동작을 수행합니다. 빨간 점이 현재 에이전트가 보고 있는 위치를 표시합니다.
-->

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

<!--
QA 테스트 자동화, 웹 데이터 추출, 폼 자동 입력, 예약/구매 자동화 등에 활용할 수 있습니다.
-->

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

<!--
왜 Nova Forge가 필요한지 먼저 설명드리겠습니다. 기존 방식들의 한계가 있습니다. RAG는 검색 기반이라 지식이 모델에 내재화되지 않고, 매번 검색해야 합니다. LoRA 파인튜닝은 기존 역량 위에 약간의 조정만 가능하고 근본적인 변화는 어렵습니다. 계속된 사전 학습(Continued Pre-training)은 새로운 지식을 넣으면 기존 지식을 잊어버리는 '치명적 망각' 문제가 있습니다. 자체 모델을 처음부터 구축하려면 수천억 원과 수년의 시간이 필요하죠. Nova Forge는 이 모든 한계를 해결합니다.
-->

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

<!--
Nova Forge의 핵심 차별점입니다. 첫째, 단계별 체크포인트 접근 - 일반적으로 모델 학습은 Pre-training이 끝난 후에만 접근 가능한데, Nova Forge는 학습 중간 단계(Mid-training)에도 접근할 수 있습니다. 학습률이 아직 높은 상태에서 시작하면 새로운 지식을 더 잘 흡수합니다. 둘째, 치명적 망각 방지 - AWS가 큐레이션한 고품질 데이터와 고객 데이터를 적절히 혼합해서 기초 역량(수학, 코딩, 언어 이해)을 유지하면서 도메인 특화가 가능합니다. 셋째, 자체 환경 연동 RL - 자체 시뮬레이터나 API와 연동해서 강화학습을 할 수 있어서, 실제 비즈니스 환경에 최적화된 에이전트를 만들 수 있습니다.
-->

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

<!--
4단계 학습 파이프라인입니다. 1단계 Pre-training은 대량의 비정형 텍스트로 언어의 기초를 학습합니다. 의료 분야라면 논문, 교과서, 임상 기록 등이 해당됩니다. 2단계 Mid-training은 특정 분야 이해를 강화하는 단계로, Nova 데이터와 혼합해서 치명적 망각을 방지합니다. 3단계 SFT(Supervised Fine-Tuning)는 '이렇게 질문하면 이렇게 답해라'는 패턴을 학습시킵니다. 4단계 RL은 실제 환경에서 보상 신호를 받아 행동을 정제합니다. 보유 데이터 양과 종류에 따라 어느 단계부터 시작할지 선택할 수 있습니다.
-->

---

## Nova Forge 가격

<br>

<div class="flex flex-col items-center gap-4">

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/nova-forge-price.webp" class="h-50 mx-auto">

<span class="text-8xl">🤦‍♂️</span>

</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

<!--
[그림 설명] Nova Forge 가격표입니다. Pre-training부터 시작하면 수백만 달러, Mid-training은 수십만 달러, SFT/RL만 하면 수만 달러 수준입니다. 일반 스타트업이나 중소기업이 접근하기엔 부담스러운 가격이고, 대기업이나 특수 도메인(의료, 법률, 금융)에서 자체 프론티어 모델이 꼭 필요한 경우에 고려할 수 있습니다. 그래서 이모지가... 네, 이해하시죠?
-->

---

## 추천워크샵
<br>

<div class="grid grid-cols-10 gap-4 w-full">
<div class="col-span-6">

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/workshop1.webp" class="h-80 mx-auto">

</div>
<div class="col-span-4 text-sm">

### 워크샵 개요
- Nova 2 Omni 멀티모달 기능 실습
- 이미지/비디오 분석 및 생성
- 텍스트-이미지 크로스모달 활용
- Bedrock API 통합 예제
- GitHub에서 바로 실습 가능

</div>
</div>

<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://github.com/aws-samples/sample-building-intelligent-multimodal-applications-with-Nova" target="_blank">Building Intelligent Multimodal Applications with Amazon Nova2 Omni</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

<!--
Nova 2 Omni를 직접 체험해보고 싶으시면 이 워크샵을 추천드립니다. GitHub에 공개되어 있어서 바로 클론해서 실습할 수 있습니다. 이미지/비디오 분석, 이미지 생성, 크로스모달 활용 등 Nova 2 Omni의 핵심 기능을 직접 경험해볼 수 있습니다.
-->

---

## Kiro - AI 에이전트 기반 개발 도구
<br>

### 소프트웨어 개발의 패러다임 전환
- 단순 코딩 보조 → 완전한 협업 파트너
- 아이디어 구상 → 요구사항 → 태스크 → 실행까지 전 과정 지원
- 개발자 생산성 5~20배 향상 가능

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

<!--
Kiro는 AWS의 AI 에이전트 기반 개발 도구입니다. 단순 코딩 보조가 아니라 완전한 협업 파트너로, 아이디어부터 실행까지 전 과정을 지원합니다.
-->

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

<!--
Spec-Driven Development로 고가치 전략적 결정을 앞당기고, 에이전트가 실행을 담당합니다. 프롬프트에서 요구사항, 설계, 코드까지 자동 생성됩니다.
-->

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

<!--
IDE와 CLI 환경을 지원하고, Agent Hooks로 백그라운드 자동화, Custom Agents로 특화 에이전트를 만들 수 있습니다. Claude Sonnet 4.5와 Opus 4.5 모델을 지원합니다.
-->

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

<!--
Kiro Powers는 MCP 서버와 스티어링 파일을 패키지로 번들링해서 도메인별 맥락을 제공합니다. Figma, Supabase, Stripe, Datadog 등 파트너 Powers가 있습니다.
-->

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

<!--
Frontier Agents는 자율 에이전트의 새로운 등급입니다. 목표만 주면 스스로 달성하고, 다중 동시 작업이 가능합니다. Autonomous, Security, DevOps 세 가지가 있습니다.
-->

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

<!--
실제로 AWS 내부에서 Bedrock 추론 엔진을 재구축할 때 Kiro를 사용했습니다. 30명이 12~18개월 걸릴 작업을 6명이 76일 만에 완료했습니다. 주간 커밋도 2회에서 40회 이상으로 늘었습니다.
-->

---

## 추천세션
<br>

<div class="grid grid-cols-10 gap-4 w-full">
<div class="col-span-6">

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/INV205.webp" class="h-80 mx-auto">

</div>
<div class="col-span-4 text-sm">

### 세션 개요
- Kiro의 Spec-Driven Development 철학
- Frontier Agents 아키텍처 심층 분석
- AWS 내부 Bedrock 재구축 사례
- 개발자 생산성 5~20배 향상 비결
- 실제 데모와 라이브 코딩

</div>
</div>

<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://www.youtube.com/watch?v=A8BYnqiHfeA" target="_blank">INV205 - Reinventing software development with AI agents</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

<!--
Kiro에 대해 더 알고 싶으시면 INV205 세션을 추천드립니다. Spec-Driven Development 철학부터 Frontier Agents 아키텍처, AWS 내부 사례까지 상세하게 다룹니다. 실제 데모도 포함되어 있어서 Kiro가 어떻게 동작하는지 직접 확인할 수 있습니다.
-->

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

<!--
Kiro 한국 사용자 모임도 운영 중입니다. QR 코드로 참여하실 수 있습니다.
-->

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

<!--
그 외에도 Bedrock에 OpenAI GPT OSS 모델 지원, Q 개발자 생산성 향상, AWS Transform 코드 모더나이제이션, Security Agent 등 다양한 업데이트가 있었습니다.
-->

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

<!--
Swami Sivasubramanian VP가 AI/ML 키노트에서 강조한 핵심 메시지입니다. "2025년은 AI 에이전트를 현실로 만드는 해"라고 선언했죠. 세 가지 핵심 트렌드를 정리하면: 첫째, 에이전틱 AI - 단순히 텍스트를 생성하는 것을 넘어 실제로 작업을 수행하고 결정을 내리는 자율 에이전트 시대. 둘째, 멀티모달의 일상화 - 텍스트, 이미지, 비디오, 음성을 자유롭게 넘나드는 모델. 셋째, 커스터마이징의 민주화 - Nova Forge처럼 기업이 자체 프론티어 모델을 구축할 수 있는 시대가 열렸습니다. AWS는 이 모든 것을 지원하는 인프라와 서비스를 제공하고 있습니다.
-->

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

<!--
올해 re:Invent 현장 사진입니다. 라스베가스의 열기를 느끼실 수 있죠.
-->

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

<!--
2018년부터 매년 참석하는 이유는 글로벌 트렌드를 직접 체감하고, 집중 학습하고, 네트워킹하고, 한 해를 마무리하는 리프레시 기간이기 때문입니다.
-->

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

<!--
내년 re:Invent에 가고 싶으시면 일정을 비워두시고, AWS 커뮤니티에 참여하세요. 한국사용자모임, Community Builder, AUSG, Cloud Clubs 등 다양한 프로그램이 있습니다.
-->

---

## QnA
<br>

<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/qr_qna.webp" class="h-60">

<div class="absolute inset-0 -z-1 bg-[url(https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/bg2.webp)] bg-cover bg-center"></div>

<!--
질문 있으시면 QR 코드로 남겨주시거나 직접 질문해 주세요. 감사합니다.
-->