# 영상/캡처 삽입 가이드

`slides.md`의 6번(주요 기능·코치), 7번(주요 기능·회원) 슬라이드에는
`<div class="iwt-placeholder">...</div>` 로 표시된 자리가 있습니다.
실제 캡처나 시연 영상이 준비되면 이 div를 아래 방법 중 하나로 통째로 교체하세요.

## 방법 1: 로컬 영상 파일 (권장)

오프라인에서도 안정적으로 재생되고, 발표 중 인터넷 연결에 의존하지 않습니다.

1. 영상을 mp4로 준비해 `public/` 폴더에 넣습니다.
   예: `public/coach-upload.mp4`, `public/member-search-demo.mp4`
2. placeholder div를 아래 코드로 교체합니다.

```html
<div class="iwt-media">
  <video src="/coach-upload.mp4" controls muted loop></video>
</div>
```

- `controls`: 재생/일시정지 컨트롤 표시
- `muted`: 자동재생을 쓸 경우 브라우저 정책상 필요 (발표 중 직접 재생할 거면 제거 가능)
- `loop`: 반복 재생
- `autoplay`를 추가하면 슬라이드 진입 시 자동 재생 (단, `muted`와 함께 써야 브라우저가 허용함)

## 방법 2: 유튜브 임베딩

영상을 이미 유튜브에 올려뒀거나 용량 부담을 피하고 싶을 때 사용합니다.
단, 발표 환경에 인터넷 연결이 필요합니다.

```html
<div class="iwt-media">
  <iframe
    src="https://www.youtube.com/embed/VIDEO_ID"
    allow="autoplay; encrypted-media"
    allowfullscreen
  ></iframe>
</div>
```

`VIDEO_ID`는 유튜브 영상 URL의 `watch?v=` 뒤에 오는 값입니다.

## 이미지(정적 캡처)만 넣을 경우

```html
<div class="iwt-media">
  <img src="/coach-upload-screenshot.png" style="width:100%; height:100%; object-fit:cover;" />
</div>
```

## 참고

- `.iwt-media`는 placeholder와 동일한 위치·크기(30% 영역, 6번은 와이드형, 7번은 세로형)를 그대로 채웁니다.
- 이미지/영상 비율이 잘려도 괜찮다면 `object-fit: cover`(기본값), 잘림 없이 전체를 보여주려면 `object-fit: contain`으로 바꾸세요.
