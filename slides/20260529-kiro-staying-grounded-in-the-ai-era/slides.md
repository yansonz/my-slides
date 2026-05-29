---
theme: default
title: Kiro와 AI 시대 속 중심 잡기
info: |
  ## Kiro와 AI 시대 속 중심 잡기
  AI FOMO와 마주하기, Kiro in Action
author: Yan So
date: 2026-05-29
css: unocss
---

<script setup>
import './style.css'
</script>

# Kiro와 AI 시대 속 중심 잡기

29 May 2026

<div class="absolute bottom-10">
  <span class="font-700">
    Yan So
  </span>
</div>

<!--
안녕하세요. 오늘은 AI 시대 속에서 어떻게 중심을 잡을 수 있는지, 그리고 Kiro를 실제로 어떻게 활용하는지 이야기해보겠습니다.
-->

---

## 발표자 소개
<br>

<div class="grid grid-cols-2 gap-8">
<div>

### Yan So (소성운)
<br>

- AWS AI Hero
- AWS한국사용자모임 운영진
  - #kiro 한국 사용자 모임
- (구) 카카오스타일 Head of AI/데이터
- (현) 쉬었음 중년

</div>
<div class="flex flex-col items-center justify-center">

링크드인
<img src="https://images.yanbert.com/my-slides/images/20260124-aws-builders-day/qr_linkedin.webp" class="h-40">

</div>
</div>

---

## 2026.02.25 ~ 2026.05.22 (87일간)

<div class="flex items-center" style="height: calc(100% - 3rem);">
<div class="grid grid-cols-[3fr_7fr] gap-4 w-full" style="height: 340px;">
<div class="flex items-center justify-center h-full">
  <img src="https://images.yanbert.com/my-slides/images/20260529-kiro-staying-grounded-in-the-ai-era/2026-05-29_09-55-31.webp" class="h-full object-contain">
</div>
<div class="grid grid-cols-3 grid-rows-2 gap-2 h-full">
  <img src="https://images.yanbert.com/my-slides/images/20260529-kiro-staying-grounded-in-the-ai-era/0A5B9FE2-07BE-43F2-BDE1-C5C9CE2F2E25_4_5005_c.webp" class="w-full object-cover" style="height: 160px;">
  <img src="https://images.yanbert.com/my-slides/images/20260529-kiro-staying-grounded-in-the-ai-era/0CE054BE-A92F-4E25-946E-A8D8212292B2.webp" class="w-full object-cover" style="height: 160px;">
  <img src="https://images.yanbert.com/my-slides/images/20260529-kiro-staying-grounded-in-the-ai-era/90E36FFB-1FB2-4880-8660-C2E75B75A294_4_5005_c.webp" class="w-full object-cover" style="height: 160px;">
  <img src="https://images.yanbert.com/my-slides/images/20260529-kiro-staying-grounded-in-the-ai-era/A0E61A9C-7D8F-4D38-922B-4FD75EEE22EC.webp" class="w-full object-cover" style="height: 160px;">
  <img src="https://images.yanbert.com/my-slides/images/20260529-kiro-staying-grounded-in-the-ai-era/BF3C65E0-DB20-424A-902E-EAA289EFFEE4_4_5005_c.webp" class="w-full object-cover" style="height: 160px;">
  <img src="https://images.yanbert.com/my-slides/images/20260529-kiro-staying-grounded-in-the-ai-era/F508465D-61B4-45DE-954D-5A070C96C5F9.webp" class="w-full object-cover" style="height: 160px;">
</div>
</div>
</div>

---

## 목차
<br>

### Part 1. AI FOMO와 마주하기

<br>

### Part 2. Kiro in Action
- Kiro 주요 기능
- Kiro로 발표 장표 만들기

---
layout: section
---

# Part 1
## AI FOMO와 마주하기

<!--
첫 번째 파트입니다. AI 시대를 살아가면서 느끼는 FOMO, 즉 뒤처지는 것에 대한 두려움을 어떻게 마주할지 이야기해보겠습니다.
-->

---

## AI 발전 연대기 (2018~2023)
<br>

<div class="text-sm timeline-table">

| 시기    | 이벤트                  | 키워드                              |
|---------|------------------------|-------------------------------------|
| 2018.06 | GPT-1 출시              | 언어 모델의 시작                     |
| 2020.06 | GPT-3 출시              | 초거대 AI, 매개변수(Parameter)       |
| 2022.11 | ChatGPT 출시            | 프롬프트 엔지니어링, 할루시네이션     |
| 2023.03 | GPT-4 + Claude 1 출시  | RAG, 헌법적 AI                      |
| 2023.07 | Claude 2 출시           | 롱 컨텍스트(Long Context Window)    |

</div>

<!--
2018년 GPT-1부터 시작해서 2022년 ChatGPT 출시로 일반 대중에게 AI가 알려지기 시작했습니다. 이 시기에 프롬프트 엔지니어링, 할루시네이션 같은 키워드들이 등장했습니다.
-->

---

## AI 발전 연대기 (2024)
<br>

<div class="text-sm timeline-table">

| 시기    | 이벤트                    | 키워드                              |
|---------|--------------------------|-------------------------------------|
| 2024.03 | Claude 3 출시             | 소버린 AI(Sovereign AI)             |
| 2024.05 | GPT-4o 출시               | 네이티브 멀티모달                    |
| 2024.06 | Claude 3.5 Sonnet 출시   | 아티팩트, 바이브 코딩                |
| 2024.09 | OpenAI o1 출시            | 추론 모델, CoT                      |
| 2024.10 | Claude 3.5 Upgraded      | 컴퓨터 사용(Computer Use)           |

</div>

<!--
2024년부터는 속도가 더 빨라졌습니다. 멀티모달, 바이브 코딩, 추론 모델, 컴퓨터 사용 등 새로운 개념이 쏟아졌습니다. 2025년에는 로컬 자율 에이전트 생태계가 폭발적으로 성장했습니다.
-->

---

## AI 발전 연대기 (2025~2026)
<br>

<div class="text-sm timeline-table">

| 시기    | 이벤트                    | 키워드                                      |
|---------|--------------------------|---------------------------------------------|
| 2025.01 | OpenClaw 바이럴           | 로컬 자율 에이전트 생태계 폭발               |
| 2025.02 | Claude 3.7 Sonnet        | 하이브리드 추론(Extended Thinking)          |
| 2025.11 | Claude Opus 4.5 출시     |                                             |
| 2026.03 | GPT-5.4 출시              | 에이전틱 AI(Agentic AI) 워크플로우          |
| 2026.04 | Hermes Agent 출시         | 자기 학습형(Self-Improving) 패러다임        |
| 2026.04 | GPT-5.5 출시              | 딥 리서치(Deep Research) 자율화             |
| 2026.04 | Claude Opus 4.7 출시     |                                             |
| 2026.05 | Claude Opus 4.8 출시     |                                             |

</div>

<br>

<!--
2026년 현재도 계속 새로운 모델과 개념이 나오고 있습니다. 이 속도를 따라가는 것 자체가 하나의 도전입니다.
-->

---

## 이 속도를 따라갈 수 있을까?
<br>

<div class="grid grid-cols-2 gap-8">
<div>

### 매 새로운 것들
- 새 모델 출시
- 새 프레임워크
- 새 개념과 용어
- 새 도구와 서비스

</div>
<div>

### 우리가 느끼는 것
- 뒤처지는 느낌
- 뭔가 놓치고 있다는 불안
- 어디서부터 시작해야 할지 모름
- 배워도 금방 구식이 되는 느낌

</div>
</div>

<br>

<!--
이 속도를 따라가려다 보면 자연스럽게 FOMO가 생깁니다. 뭔가 놓치고 있다는 불안감, 뒤처지는 느낌. 이게 AI 시대를 살아가는 많은 분들이 공통적으로 느끼는 감정입니다.
-->

---

## 나의 상처
<br>

<div class="grid grid-cols-2 gap-8">
<div>

### 조직 내 R&R 혼란
- AI 담당 조직이 어디인가?
- 개발팀? 데이터팀? 기획팀?
- 모두가 AI를 해야 하는가?
- AX전문가가 필요한가?

</div>
<div>

### 나의 FOMO
- 기술을 선도하지 못한다는 생각
- 그에 비해 학습에 시간을 투자하지 않음
- 변화의 속도가 학습의 속도를 앞지름
- 나의 전문성이 사라지는 느낌

</div>
</div>

---

## The right tool for the job
<br>

<div class="grid grid-cols-2 gap-8 items-center">
<div>

- 포르투갈의 나무 전봇대
- 비용 저렴
- 설치, 운반 쉬움
- 유지보수 단순

</div>
<div>

<img src="https://images.yanbert.com/my-slides/images/20260529-kiro-staying-grounded-in-the-ai-era/C19406F8-0FC3-48D6-B56F-7D789B801D0C_1_105_c.webp" class="h-80 mx-auto">

</div>
</div>

<!--
포르투갈 전봇대 이야기를 들어보셨나요? 현지 환경에 맞는 방법이 따로 있다는 이야기입니다. AI 도구도 마찬가지입니다.
-->

---

## The right tool for the job
<br>

<div class="grid grid-cols-[6fr_4fr] gap-8">
<div>

### AWS 핵심 아키텍처 철학
- 하나의 기술로 모든 문제를 해결하려 하지 말고
- 비즈니스 요구사항과 워크로드의 특성에 딱 맞춘
- 전용(Purpose-built) 서비스를 선택 및 조합
- 데이터레이크를 구현한다면? AWS vs. Google

</div>
<div>

<img src="https://images.yanbert.com/my-slides/images/20260529-kiro-staying-grounded-in-the-ai-era/reInvent20_Keynote_Andy_1.webp" class="w-full object-contain">

</div>
</div>

---

## The right tool for the job
<br>

### 프롬프트 엔지니어링으로 리뷰 검수 자동화 (카카오스타일)
<br>

<div class="grid grid-cols-[7fr_3fr] gap-8 items-center">
<div>

- 복잡한 ML 모델 없이 프롬프트만으로 구현
- 쉽게 시작했지만 과정 중 여러 문제들을 발견
- Human in the Loop의 필요성 확인
- 최신 기술이 아니어도, 현재 문제를 해결하는 것이 중요

</div>
<div>

<img src="https://images.yanbert.com/my-slides/images/20260529-kiro-staying-grounded-in-the-ai-era/gbl214.webp" class="w-full scale-125">

</div>
</div>

<!--
카카오스타일에서 실제로 AI를 활용한 사례를 소개합니다. 복잡한 ML 모델 없이 프롬프트 엔지니어링만으로 리뷰 검수를 자동화했습니다. 이 경험에서 중요한 인사이트를 얻었습니다. AI를 마법이 아닌 툴로 바라보는 관점, 그리고 Human in the Loop의 중요성입니다.
-->

---

## The right tool for the job
<br>

### 요즘 고민중인 것
<br>

- AI코딩툴 무엇을써야하나 고민은 접음 - Kiro에 집중
- OpenClaw나 Hermes 이전에 요즘 메인 작업엔 Amazon Quick을 써보는 중
- 내 워크플로우, 내 팀, 내 문제에 맞는 도구가 최선

<br>

<div class="grid grid-cols-3 gap-4 text-sm">
<div class="border rounded p-3">

**탐색 단계**<br>
새 도구 써보기<br>
실험하기

</div>
<div class="border rounded p-3">

**평가 단계**<br>
내 문제에 맞는가?<br>
팀에 도입 가능한가?

</div>
<div class="border rounded p-3">

**정착 단계**<br>
깊게 파기<br>
생산성 극대화

</div>
</div>

<!--
Claude Code가 좋다고 해서 무조건 써야 하는 건 아닙니다. 저도 OpenClaw는 써보겠지만, 요즘 메인 작업에는 Amazon Q를 써보고 있습니다. 중요한 건 내 상황에 맞는 도구를 찾는 것입니다.
-->

---

## There is no compression algorithm for experience
<br>

<div class="grid grid-cols-[6fr_4fr] gap-8">
<div>

- AI를 이용해 내 업무를 자동화해 보거나, 내가 겪는 문제를 해결해보는 경험
- AI를 비즈니스나 삶에 적용해 보며 겪은 수많은 시행착오을 통한 미세 조정과 축적의 경험
- 길게 보고 작게라도 시작해보기

</div>
<div>

<img src="https://images.yanbert.com/my-slides/images/20260529-kiro-staying-grounded-in-the-ai-era/quote.webp" class="w-full object-contain">

</div>
</div>

<!--
"경험을 압축하는 알고리즘은 없다"는 말이 있습니다. AI가 아무리 발전해도, 당신이 직접 겪고 배운 경험은 대체할 수 없습니다. 두려움의 근원을 들여다보면, 결국 모르는 것에 대한 불안입니다.
-->

---

## 중심 잡기: 내가 주체가 되어야 한다
<br>

<div class="grid grid-cols-2 gap-8">
<div>

### AI 시대의 함정
- 도구에 끌려다니기
- 남이 쓰는 걸 따라 쓰기
- 최신 것만 좇기
- 깊이 없이 넓게만 가기

</div>
<div>

### 중심 잡는 방법
- **내가 주체**가 되어야 함
- 어린아이 같은 호기심으로 해보기
- 길게 보기
- 도구보다 **축적**에 집중

</div>
</div>

<!--
AI 시대에 중심을 잡으려면 내가 주체가 되어야 합니다. 도구에 끌려다니는 게 아니라, 내가 도구를 선택하고 활용하는 것입니다. 어린아이처럼 호기심을 갖고 해보는 것, 그리고 단기적인 유행보다 장기적인 축적에 집중하는 것이 중요합니다.
-->

---

## 중심 잡기: 축적에 집중하기
<br>

### 도구는 바뀌어도 이것은 남는다
<br>

<div class="grid grid-cols-3 gap-4 text-sm">
<div class="border rounded p-3">

**문제 해결 능력**<br>
어떤 문제인지 정의하고<br>
해결책을 찾는 능력

</div>
<div class="border rounded p-3">

**도메인 지식**<br>
내 분야의 깊은 이해<br>
AI 결과를 검증하는 능력

</div>
<div class="border rounded p-3">

**경험과 판단력**<br>
실패에서 배운 것들<br>
상황을 읽는 감각

</div>
</div>

<!--
도구는 계속 바뀝니다. 하지만 문제 해결 능력, 도메인 지식, 경험과 판단력은 남습니다. AI가 틀렸을 때 알아채는 능력, 이게 바로 당신의 경험에서 나옵니다.
-->

---
layout: section
---

# Part 2
## Kiro in Action

<!--
이제 두 번째 파트입니다. Kiro를 실제로 어떻게 활용하는지 보여드리겠습니다.
-->

---

## Kiro란?
<br>

AWS의 AI 에이전트 기반 개발 도구

<br>

- 단순 코딩 보조 → **완전한 협업 파트너**
- 아이디어 → 요구사항 → 태스크 → 실행까지 전 과정 지원
- VS Code 기반 IDE + CLI 환경

<!--
Kiro는 AWS의 AI 에이전트 기반 개발 도구입니다. 단순히 코드를 완성해주는 것을 넘어서, 아이디어부터 실행까지 전 과정을 함께합니다.
-->

---

## Kiro 주요 기능
<br>

<div class="text-sm">

| 기능 | 설명 |
|------|------|
| **Specs** | 요구사항 → 설계 → 태스크 자동 생성 (Spec-Driven Development) |
| **Hooks** | IDE 이벤트 기반 자동화 (파일 저장, 커밋 등) |
| **Steering** | 팀 표준과 컨텍스트를 에이전트에게 자동 주입 |
| **Skills** | 재사용 가능한 작업 패턴 정의 |
| **Powers** | MCP 서버 + Steering + Hooks 번들 패키지 |

</div>

<!--
Kiro의 핵심 기능 다섯 가지입니다. Specs로 구조화된 개발을 하고, Hooks로 자동화하고, Steering으로 팀 표준을 적용하고, Skills와 Powers로 재사용 가능한 패턴을 만듭니다.
-->

---

## Specs: Spec-Driven Development
<br>

<div class="grid grid-cols-2 gap-8">
<div>

### 기존 방식
```
프롬프트 → 코드 생성
(맥락 없음, 일관성 없음)
```

<br>

### Spec 방식
```
아이디어
  → 요구사항(Requirements)
  → 설계(Design)
  → 태스크(Tasks)
  → 구현
```

</div>
<div>

### 왜 좋은가?
- 고가치 결정을 앞당김
- 맥락이 문서로 남음
- 에이전트가 일관되게 실행
- 나중에 왜 그렇게 했는지 알 수 있음

</div>
</div>

<!--
Spec-Driven Development는 단순히 프롬프트를 던지는 것과 다릅니다. 요구사항, 설계, 태스크를 먼저 정의하고, 에이전트가 그 맥락 안에서 일관되게 실행합니다.
-->

---

## Hooks: 자동화의 힘
<br>

### IDE 이벤트에 반응하는 자동화
<br>

```json
{
  "name": "슬라이드 저장 시 발표자 노트 업데이트",
  "when": {
    "type": "fileEdited",
    "patterns": ["**/slides/**/*.md"]
  },
  "then": {
    "type": "askAgent",
    "prompt": "슬라이드 내용이 변경되었습니다. 발표자 노트를 최신 내용에 맞게 업데이트해주세요."
  }
}
```

<!--
Hooks는 IDE 이벤트에 반응하는 자동화입니다. 예를 들어 슬라이드 파일을 저장하면 자동으로 발표자 노트를 업데이트하도록 설정할 수 있습니다.
-->

---

## Steering: 팀 표준 자동 적용
<br>

### 에이전트에게 컨텍스트를 주입하는 방법
<br>

- `.kiro/steering/*.md` 파일로 관리
- **항상 포함**: 팀 코딩 표준, 프로젝트 구조
- **파일 매칭**: 특정 파일 편집 시에만 적용
- **수동**: 필요할 때 `#` 으로 직접 참조

<br>

```markdown
# 슬라이드 패턴 가이드
## 테이블 패턴
슬라이드에 테이블을 추가할 때는 항상 
`<div class="text-sm">` 으로 감싸서 글씨 크기를 줄입니다.
```

<!--
Steering은 에이전트에게 팀 표준을 자동으로 주입하는 기능입니다. 이 발표 슬라이드 프로젝트에도 슬라이드 패턴 가이드를 Steering으로 관리하고 있습니다.
-->

---

## Powers: 도구 생태계
<br>

### MCP 서버 + Steering + Hooks 번들
<br>

<div class="grid grid-cols-2 gap-8">
<div>

### 파트너 Powers
- **Supabase**: 백엔드 연동
- **Figma**: UI 디자인 연동
- **Stripe**: 결제 연동
- **AWS**: 인프라 연동

</div>
<div>

### 직접 만들기
- 사내 API 연동
- 팀 전용 도구 패키지
- 재사용 가능한 워크플로우

</div>
</div>

<!--
Powers는 MCP 서버와 Steering, Hooks를 하나의 패키지로 묶은 것입니다. Supabase, Figma 같은 파트너 Powers를 쓸 수도 있고, 직접 만들 수도 있습니다.
-->

---

## Kiro로 발표장표 만들기
<br>

<div class="text-sm text-gray-400">
🔗 <a href="https://slides.yanbert.com/20260212-kiro-krug-make-slides-with-kiro" target="_blank">https://slides.yanbert.com/20260212-kiro-krug-make-slides-with-kiro</a>
</div>

---

## 정리: AI 시대 속 중심 잡기
<br>

<div class="grid grid-cols-2 gap-8">
<div>

### FOMO에 대처하는 방법
- 모든 걸 따라갈 필요 없다
- 내 문제에 맞는 도구 선택
- 도구보다 경험과 판단력 축적
- 길게 보기

</div>
<div>

### Kiro를 활용하는 방법
- Spec으로 구조화된 개발
- Steering으로 팀 표준 자동화
- Hooks로 반복 작업 제거
- AI는 초안, 판단은 내가

</div>
</div>

<!--
오늘 이야기를 정리하겠습니다. AI FOMO에 대처하는 방법은 모든 걸 따라가려 하지 않고, 내 문제에 맞는 도구를 선택하고, 경험과 판단력을 축적하는 것입니다. Kiro는 그 과정에서 좋은 협업 파트너가 될 수 있습니다.
-->

---

## 감사합니다!
<br>

질문이 있으신가요? 👻

<br>

<div class="text-sm text-gray-400">

- 슬라이드: https://slides.yanbert.com
- Kiro 한국 사용자 모임: https://luma.com/kiro-krug

</div>

<!--
감사합니다. 질문 있으시면 편하게 해주세요.
-->
