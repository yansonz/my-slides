---
theme: default
title: Slidev 템플릿 가이드
info: |
  ## Slidev 템플릿 가이드
  다양한 레이아웃과 문법 예시
author: Your Name
date: 2026-01-07
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Slidev 템플릿 가이드

다양한 레이아웃과 문법 예시

<div class="abs-br m-6 flex gap-2">
  <a href="https://sli.dev" target="_blank" class="text-xl slidev-icon-btn">
    📖 Slidev 문서
  </a>
</div>

---

# 📝 코드: layout: intro

```md
---
layout: intro
---

# 발표 제목

발표자 소개에 적합한 레이아웃

<div class="absolute bottom-10">
  <span class="font-700">
    발표자 이름 / 소속
  </span>
</div>
```

---
layout: intro
---

# ✅ 결과: layout: intro

발표자 소개에 적합한 레이아웃

<div class="absolute bottom-10">
  <span class="font-700">
    발표자 이름 / 소속
  </span>
</div>

---

# 📝 코드: layout: two-cols

```md
---
layout: two-cols
---

# 제목

왼쪽 컬럼 내용
- 포인트 1
- 포인트 2

::right::

오른쪽 컬럼 내용
- 항목 A
- 항목 B
```

---
layout: two-cols
---

# ✅ 결과: two-cols

왼쪽 컬럼 내용
- 포인트 1
- 포인트 2

::right::

오른쪽 컬럼 내용
- 항목 A
- 항목 B

---

# 📝 코드: layout: image-right

```md
---
layout: image-right
image: https://cover.sli.dev
---

# 제목

오른쪽에 이미지가 배치되는 레이아웃

- 텍스트는 왼쪽에
- 이미지는 오른쪽에
- 제품 소개에 적합
```

---
layout: image-right
image: https://cover.sli.dev
---

# ✅ 결과: image-right

오른쪽에 이미지가 배치되는 레이아웃

- 텍스트는 왼쪽에
- 이미지는 오른쪽에
- 제품 소개에 적합

---

# 📝 코드: layout: image-left

```md
---
layout: image-left
image: https://cover.sli.dev
---

# 제목

왼쪽에 이미지가 배치되는 레이아웃

- 이미지는 왼쪽에
- 텍스트는 오른쪽에
```

---
layout: image-left
image: https://cover.sli.dev
---

# ✅ 결과: image-left

왼쪽에 이미지가 배치되는 레이아웃

- 이미지는 왼쪽에
- 텍스트는 오른쪽에

---

# 📝 코드: layout: center

```md
---
layout: center
class: text-center
---

# 중앙 정렬 제목

강조하고 싶은 내용에 적합
```

---
layout: center
class: text-center
---

# ✅ 결과: center

강조하고 싶은 내용에 적합

---

# 📝 코드: layout: quote

```md
---
layout: quote
---

# "인용구 내용"

인용구를 강조할 때 사용합니다.

— 출처
```

---
layout: quote
---

# ✅ 결과: quote

"인용구 내용"

인용구를 강조할 때 사용합니다.

— 출처

---

# 📝 코드: layout: fact

```md
---
layout: fact
---

# 100%
숫자나 핵심 사실을 강조
```

---
layout: fact
---

# ✅ 결과: fact

100%

숫자나 핵심 사실을 강조

---

# 📝 코드: layout: statement

```md
---
layout: statement
---

# 핵심 메시지

중요한 문장을 강조할 때 사용
```

---
layout: statement
---

# ✅ 결과: statement

핵심 메시지

중요한 문장을 강조할 때 사용

---

# 📝 코드: 코드 하이라이팅

````md
```ts {2,3|5|all}
function hello() {
  // 2-3번 줄 하이라이트
  console.log('Hello')
  
  // 5번 줄 하이라이트
  return 'World'
}
```
````

클릭할 때마다 하이라이트 위치가 변경됩니다.

---

# ✅ 결과: 코드 하이라이팅

```ts {2,3|5|all}
function hello() {
  // 2-3번 줄 하이라이트
  console.log('Hello')
  
  // 5번 줄 하이라이트
  return 'World'
}
```

---

# 📝 코드: v-clicks 애니메이션

```md
<v-clicks>

- 첫 번째 항목
- 두 번째 항목
- 세 번째 항목

</v-clicks>
```

클릭할 때마다 항목이 하나씩 나타납니다.

---

# ✅ 결과: v-clicks 애니메이션

<v-clicks>

- 첫 번째 항목
- 두 번째 항목
- 세 번째 항목

</v-clicks>

---

# 📝 코드: 인라인 v-click

```md
항목 1 <v-click>→ 항목 2</v-click> <v-click>→ 항목 3</v-click>

<v-click>

최종 결과가 여기에 표시됩니다.

</v-click>
```

---

# ✅ 결과: 인라인 v-click

항목 1 <v-click>→ 항목 2</v-click> <v-click>→ 항목 3</v-click>

<v-click>

최종 결과가 여기에 표시됩니다.

</v-click>

---

# 📝 코드: 테이블

```md
| 기능 | 설명 | 예시 |
|------|------|------|
| 레이아웃 | 슬라이드 배치 | `layout: two-cols` |
| 클릭 | 애니메이션 | `<v-click>` |
| 코드 | 하이라이팅 | `{2,3\|5}` |
```

---

# ✅ 결과: 테이블

| 기능 | 설명 | 예시 |
|------|------|------|
| 레이아웃 | 슬라이드 배치 | `layout: two-cols` |
| 클릭 | 애니메이션 | `<v-click>` |
| 코드 | 하이라이팅 | `{2,3\|5}` |

---

# 📝 코드: 그리드 레이아웃

```html
<div class="grid grid-cols-2 gap-4">
<div>

### 왼쪽 섹션
- 항목 1
- 항목 2

</div>
<div>

### 오른쪽 섹션
- 항목 A
- 항목 B

</div>
</div>
```

---

# ✅ 결과: 그리드 레이아웃

<div class="grid grid-cols-2 gap-4">
<div>

### 왼쪽 섹션
- 항목 1
- 항목 2

</div>
<div>

### 오른쪽 섹션
- 항목 A
- 항목 B

</div>
</div>

---

# 📝 코드: 아이콘 사용

```html
<div class="grid grid-cols-4 gap-4 text-4xl">
  <div>🚀</div>
  <div>💡</div>
  <div>⚡</div>
  <div>🔥</div>
</div>
```

---

# ✅ 결과: 아이콘 사용

<div class="grid grid-cols-4 gap-4 text-4xl">
  <div>🚀</div>
  <div>💡</div>
  <div>⚡</div>
  <div>🔥</div>
</div>

---

# 📝 코드: 이미지 삽입

```md
로컬: ![alt](/image.png)
URL: ![alt](https://example.com/image.png)
크기 조절: <img src="/image.png" class="h-40" />
```

---

# ✅ 결과: 이미지 삽입

<img src="https://cover.sli.dev" class="h-50 rounded" />

---

# 📝 코드: Arrow 컴포넌트

```html
<div class="relative h-40">
  <div class="absolute left-10 top-10">시작</div>
  <div class="absolute right-10 top-10">끝</div>
  <Arrow x1="80" y1="90" x2="400" y2="90" />
</div>
```

---

# ✅ 결과: Arrow 컴포넌트

<div class="relative h-30">
  <div class="absolute left-10 top-5">시작</div>
  <div class="absolute right-20 top-5">끝</div>
  <Arrow x1="80" y1="60" x2="400" y2="60" />
</div>

---

# 📝 코드: 발표자 노트

```md
슬라이드 내용

<!-- 
발표자 노트는 여기에 작성합니다.
발표자 모드에서만 보입니다.
http://localhost:3030/presenter
-->
```

---

# ✅ 결과: 발표자 노트

발표자 모드(Presenter Mode)에서 아래 노트를 확인할 수 있습니다.

`http://localhost:3030/presenter` 접속

<!-- 
이것은 발표자 노트입니다.
발표자 모드에서만 보입니다.
- 추가 설명 포인트
- 시간 안내
-->

---
layout: end
---

# 감사합니다!

질문이 있으신가요?

[📧 이메일](mailto:email@example.com) · [🐙 GitHub](https://github.com)
