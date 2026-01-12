<!------------------------------------------------------------------------------------
   슬라이드 작성 시 참고할 패턴 가이드
   
   inclusion: fileMatch
   fileMatchPattern: '**/slides/**/*.md'
------------------------------------------------------------------------------------>

# 슬라이드 패턴 가이드

## 테이블 패턴

슬라이드에 테이블을 추가할 때 사용합니다.

```markdown
<div class="text-sm">

| 헤더1 | 헤더2 | 헤더3 |
|------|------|------|
| 내용1 | 내용2 | 내용3 |

</div>
```

### 스타일 가이드
- 테이블은 항상 `<div class="text-sm">` 으로 감싸서 글씨 크기를 줄임
- 슬라이드 공간 활용을 위해 작은 폰트 사용

## 추천세션 슬라이드 패턴

외부 세션이나 영상을 추천할 때 사용하는 패턴입니다.

```markdown
<br>

<img src="/images/{세션이미지}.png" class="h-90 mx-auto">
<br>

<div class="text-sm text-gray-400">
🔗 <a href="{영상URL}" target="_blank">{세션코드} - {세션제목}</a>
</div>

<div class="absolute inset-0 -z-1 bg-[url(/images/bg2.png)] bg-cover bg-center"></div>
```

### 구성 요소
- 세션 썸네일 이미지: `h-90 mx-auto` 클래스로 중앙 정렬
- 출처 링크: `text-sm text-gray-400` 스타일로 하단에 배치
- 🔗 이모지로 링크임을 시각적으로 표시
- `target="_blank"`로 새 탭에서 열기

### 예시
```markdown
<div class="text-sm text-gray-400">
🔗 <a href="https://www.youtube.com/watch?v=ymwpOYMg1ng" target="_blank">AIM3330 - Keep Your Agents Out of Trouble with Amazon Bedrock AgentCore</a>
</div>
```

## 출처/참고자료 슬라이드 패턴

슬라이드 하단에 출처나 참고자료를 표시할 때 사용합니다.

```markdown
<div class="text-sm text-gray-400">
🔗 <a href="{URL}" target="_blank">{출처 설명}</a>
</div>
```

### 스타일 가이드
- 폰트 크기: `text-sm` (작은 텍스트)
- 색상: `text-gray-400` (회색으로 눈에 덜 띄게)
- 위치: 슬라이드 하단 또는 관련 콘텐츠 아래
