---
theme: default
title: 제1회 Kiro 한국 사용자 모임
info: |
  ## 발표 제목
  제1회 Kiro 한국 사용자 모임
author: Yan So
date: 2026-01-22
css: unocss
---

<script setup>
import './style.css'
</script>

# Kiro 한국 사용자 모임

22 Jan 2026

<div class="absolute bottom-10">
  <span class="font-700">
    Yan So
  </span>
</div>

---
layout: fact
---

# 첫 번째 모임에 <br> 와주셔서 <br> 감사합니다👻

---

## 출석체크
<br>

<img src="https://images.yanbert.com/my-slides/images/20260122-kiro-krug/05.webp" class="h-85 mx-auto">

<div class="text-center">
https://checkin.awskr.org/kiro/0122ZZV
</div>

---

## 운영자 소개
<br> 

- Yan So / AWS한국사용자모임 - #data
- 윤평호 / AWS한국사용자모임 - #container
- 김현민 / AWS한국사용자모임 - #gametech

---

## 목차
<br>

- Kiro Powers 소개
- 라이트닝 토크

---

## 어떤 AI코딩툴을 사용하고 계신가요?
<br>

Kiro, Claude Code, Codex, Cursor 등등 사용하시는 AI코딩툴을 알려주세요
<br>
<br>

<img src="https://images.yanbert.com/my-slides/images/20260122-kiro-krug/03.webp" class="h-70 mx-auto mt-4">

---

## QnA는 여기에 남겨주세요
<br>

동일 링크 입니다.
<br>
<br>

<img src="https://images.yanbert.com/my-slides/images/20260122-kiro-krug/03.webp" class="h-70 mx-auto mt-4">

---

## Kiro Powers
<br>

### AI 에이전트에 전문 지식을 부여하는 기능
<br>

- MCP 서버 + Steering 파일 + Hooks를 하나로 패키징
- 키워드 기반 동적 로딩 (컨텍스트 윈도우 절약)
- Figma, Stripe, Supabase, Datadog 등 파트너 Powers 제공
- 커스텀 Power 직접 제작 가능

---

## Kiro Powers
<br>

<img src="https://images.yanbert.com/my-slides/images/20260122-kiro-krug/04.webp" class="h-105 object-contain">

---

## 왜 Powers가 필요한가?
<br>

### 기존 MCP의 문제점 (예시)
- 5개 MCP 서버 연결 -> 100+ 도구 정의 로드
- 첫 프롬프트 전에 50,000+ 토큰 소비 (컨텍스트의 40%)
- 컨텍스트 과부하 -> 응답 속도 저하, 품질 하락

--- 

## 왜 Powers가 필요한가?
<br>

### Powers의 해결책
- 동적 로딩: "database" 언급 시 Supabase Power만 활성화
- 작업 전환 시 자동 비활성화 → 컨텍스트 효율화

---

## Power의 구조
<br>

```
my-power/
├── POWER.md          # 진입점 - 키워드, 도구 사용법
├── mcp.json          # MCP 서버 설정
└── steering/         # 워크플로우별 가이드
    ├── setup.md
    └── best-practices.md
```

<br>

- POWER.md: 에이전트 온보딩 매뉴얼
- 키워드 매칭으로 자동 활성화
- 워크플로우별 steering 파일 동적 로드

---

## Power 예시: Strands Agents
<br>

### Strands Agents SDK Power
- AI 에이전트 개발을 위한 오픈소스 SDK
- Amazon bedrock, Anthropic, OpenAI, Gemini, Llama 모델 지원

<br>

### 키워드 활성화
```
"strands", "agent", "bedrock agent", "ai agent"
```

→ 관련 키워드 언급 시 자동으로 Power 활성화

<div class="text-sm text-gray-400">
🔗 <a href="https://github.com/kirodotdev/powers/tree/main/strands" target="_blank">github.com/kirodotdev/powers/tree/main/strands</a>
</div>

---

## Strands Power 활용 예시
<br>

```python
# "strands agent 만들어줘" 라고 요청하면
# Strands Power가 자동 활성화되어 가이드 제공

from strands import Agent
from strands.models import BedrockModel

model = BedrockModel(model_id="anthropic.claude-3-5-sonnet")
agent = Agent(model=model)

response = agent("서울 날씨 알려줘")
```

<br>

- MCP 도구 + Best Practices steering 자동 로드
- 모델별 설정, 도구 연동 가이드 제공

---

## 실제로 해봅시다!
<br>

💻 strands agent를 만드는 데모

---

## Kiro Powers vs Claude Skills
<br>

<div class="text-sm">

| 구분 | Kiro Powers | Claude Skills |
|------|-------------|---------------|
| 구성 | MCP + Steering + Hooks 번들 | SKILL.md + 스크립트 |
| 활성화 | 키워드 기반 동적 로딩 | 메타데이터 매칭 시 로드 |
| 외부 연동 | MCP 서버로 API/DB 연결 | MCP 별도 설정 필요 |
| 토큰 효율 | 작업 전환 시 자동 언로드 | Progressive Disclosure |
| 플랫폼 | Kiro IDE (향후 확장 예정) | Claude.ai, Claude Code |

</div>

<br>

> 💡 Powers = Skills + MCP + 동적 로딩의 통합 패키지

---

## 활성화 방식 비교
<br>

<div class="text-sm">

| 단계 | Kiro Powers | Claude Skills |
|------|-------------|---------------|
| 초기 | 0 토큰 (미활성화) | ~100 토큰 (메타데이터) |
| 트리거 | 키워드 매칭 ("database") | 요청-Skill 관련성 판단 |
| 로드 | MCP 도구 + Steering 전체 | 전체 지침 (<5K 토큰) |
| 실행 | 필요시 스크립트/파일 로드 | 필요시 번들 파일 로드 |

</div>

<br>

- Powers: "database" → Supabase 활성화 → "deploy" → Netlify로 전환
- Skills: 메타데이터 스캔 → 관련 Skill 판단 → 점진적 로드

---

## 외부 연동 비교
<br>

### Kiro Powers
- MCP 서버가 기본 포함
- GitHub, Stripe, Supabase 등 즉시 연결
- 별도 설정 없이 외부 API 호출

<br>

### Claude Skills  
- Skill 자체는 샌드박스 내 실행
- 외부 연동 시 MCP 별도 구성 필요
- Skills + MCP 조합으로 확장 가능

---

## 토큰 효율 비교
<br>

### Kiro Powers
- 작업 A → Power A 활성화 (MCP 도구 로드)
- 작업 B → Power A 비활성화 + Power B 활성화 (컨텍스트 자동 정리)

<br>

### Claude Skills
- 작업 A → Skill A 로드 (~100 → <5K 토큰)
- 작업 B → Skill B 추가 로드 (기존 Skill 유지 경향)

<br>

> Powers는 **자동 언로드**, Skills는 **점진적 로드**에 강점

---

## Custom Power 도 만들어 봅시다!
<br>

💻 Kiro Power를 만드는 Power로 n8n Power 만들어보기 데모

---

## 라이트닝 토크
<br>

5-10분 정도 자유롭게 나오셔서 이야기할 수 있습니다.
- ​권태관(우아한형제들) AI-Workflow를 활용한 개발팀 생산성 올리기
- ​남기웅 (브이피피랩) Kiro 야생 적응기
- ...

---

## 감사합니다!

다음 모임은 2/12(목) 예정입니다👻

<div class="flex gap-4 justify-center items-center mt-8">
  <img src="https://images.yanbert.com/my-slides/images/20260122-kiro-krug/01.webp" class="h-90">
  <img src="https://images.yanbert.com/my-slides/images/20260122-kiro-krug/02.webp" class="h-50">
</div>



