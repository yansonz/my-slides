---
theme: default
title: iwasthere — 이벤트 사진, 내 얼굴만 찾아주는 서비스
info: |
  ## iwasthere Sales Deck
  이벤트 단체사진에서 AI로 내 사진만 찾아주는 서비스
author: iwasthere
date: 2026-07-10
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
---

<!-- Cover -->
<div class="iwt-cover">
  <img src="/iwt.png" class="logo" />
  <h1>iwasthere</h1>
  <p>이벤트 참여자에게 사진 공유,<br/>안전하고 빠르게 해보세요</p>
</div>

<style>
@import './style.css';
</style>

---

<!-- Problem -->
<div class="iwt-problem">
  <div class="iwt-header">
    <span class="iwt-badge">문제 정의</span>
    <h1>이벤트 사진, 지금 어떻게 받고 계세요?</h1>
  </div>

  <div class="iwt-body">
  <div class="pain-point">
    <h3>📱 수백 장 단체사진에서 내 사진 찾기</h3>
    <p>러닝크루, 크로스핏, 웨딩, 개발자 행사... 매번 수백 장을 일일이 스크롤</p>
  </div>

  <div class="pain-point">
    <h3>⏳ 공유 링크 만료 & 분산</h3>
    <p>구글드라이브, 카카오톡, 에어드랍... 어디에 올라왔는지 찾기 힘듦</p>
  </div>

  <div class="pain-point">
    <h3>🙈 타인 얼굴 노출 우려</h3>
    <p>SNS에 올리고 싶지만 다른 사람 얼굴이 함께 찍혀있음</p>
  </div>
  </div>
</div>

---

<!-- Solution Overview -->
<div class="iwt-solution">
  <div class="iwt-header">
    <span class="iwt-badge">솔루션</span>
    <h1>얼굴 인증 한 번이면, 내 사진만 5초 검색</h1>
  </div>

  <div class="iwt-body">
  <div class="feature-grid">
    <div class="feature-card">
      <div class="icon">📸</div>
      <h3>얼굴 인증 기반 검색</h3>
      <p>회원가입 없이 카메라로 얼굴만 확인하면 내가 나온 사진을 자동으로 찾아줘요</p>
    </div>
    <div class="feature-card">
      <div class="icon">🔗</div>
      <h3>링크 하나로 접근</h3>
      <p>앱 설치 없이 웹(PWA)에서 링크 클릭만으로 이벤트 사진에 접근</p>
    </div>
    <div class="feature-card">
      <div class="icon">🎭</div>
      <h3>타인 얼굴 자동 모자이크</h3>
      <p>다른 사람 얼굴은 기본적으로 가려져서 안심하고 공유·다운로드</p>
    </div>
    <div class="feature-card">
      <div class="icon">🎬</div>
      <h3>사진 + 동영상 지원</h3>
      <p>사진뿐 아니라 행사 영상에서도 프레임 단위로 내 얼굴을 찾아줘요 (Pro)</p>
    </div>
  </div>
  </div>
</div>

---

<!-- How It Works -->
<div class="iwt-content">
  <div class="iwt-header">
    <span class="iwt-badge">작동 방식</span>
    <h1>3단계로 끝나는 이벤트 사진 관리</h1>
  </div>

  <div class="iwt-body">
  <div class="iwt-two-col">
    <div>
      <h2 style="color: var(--iwt-primary);">📷 주최자 (이벤트 생성)</h2>
      <ol style="line-height: 2; color: var(--iwt-gray-600); font-size: 0.95rem; padding-left: 1.25rem;">
        <li>이메일 인증 후 로그인 (OTP, 비밀번호 없음)</li>
        <li>사진·동영상 업로드 & 공유 링크 생성</li>
        <li>참여자에게 링크 전달</li>
      </ol>
      <p style="margin-top: 1rem; font-size: 0.82rem; color: var(--iwt-gray-400);">
        보관 기간: Free 48시간 · Pro 7일 (만료 후 순차 삭제)
      </p>
    </div>
    <div>
      <h2 style="color: var(--iwt-primary);">🙋 참여자 (회원가입 불필요)</h2>
      <ol style="line-height: 2; color: var(--iwt-gray-600); font-size: 0.95rem; padding-left: 1.25rem;">
        <li>링크 접속</li>
        <li>카메라로 얼굴 확인 (라이브니스 체크)</li>
        <li>내 사진만 검색 & 다운로드</li>
      </ol>
      <p style="margin-top: 1rem; font-size: 0.82rem; color: var(--iwt-gray-400);">
        얼굴 데이터는 매칭 즉시 삭제, 서버에 보관하지 않음
      </p>
    </div>
  </div>
  </div>
</div>

---

<!-- Target Users -->
<div class="iwt-content">
  <div class="iwt-header">
    <span class="iwt-badge">타겟 고객</span>
    <h1>이런 분들에게 딱 맞습니다</h1>
  </div>

  <div class="iwt-body iwt-body-top">
  <div class="feature-grid" style="grid-template-columns: repeat(4, 1fr);">
    <div class="feature-card" style="text-align: center; padding: 2rem 1.25rem;">
      <div class="icon" style="font-size: 2.6rem;">🏃</div>
      <h3 style="font-size: 1.1rem; margin-top: 0.75rem;">러닝 크루<br>그룹 운동</h3>
      <p style="font-size: 0.85rem;">매회 수십~수백 장의 활동 사진</p>
    </div>
    <div class="feature-card" style="text-align: center; padding: 2rem 1.25rem;">
      <div class="icon" style="font-size: 2.6rem;">💻</div>
      <h3 style="font-size: 1.1rem; margin-top: 0.75rem;">사내 행사<br>컨퍼런스</h3>
      <p style="font-size: 0.85rem;">수백 명 규모<br>행사 현장 사진</p>
    </div>
    <div class="feature-card" style="text-align: center; padding: 2rem 1.25rem;">
      <div class="icon" style="font-size: 2.6rem;">🏋️</div>
      <h3 style="font-size: 1.1rem; margin-top: 0.75rem;">피트니스<br>대회 참가</h3>
      <p style="font-size: 0.85rem;">하이록스, 크로스핏<br>대회 사진</p>
    </div>
    <div class="feature-card" style="text-align: center; padding: 2rem 1.25rem;">
      <div class="icon" style="font-size: 2.6rem;">💍</div>
      <h3 style="font-size: 1.1rem; margin-top: 0.75rem;">웨딩 / 돌잔치<br>가족모임</h3>
      <p style="font-size: 0.85rem;">하객 사진을 각자에게 자동 배분</p>
    </div>
  </div>
  </div>
</div>

---

<!-- Pricing -->
<div class="iwt-pricing">
  <div class="iwt-header">
    <span class="iwt-badge">가격</span>
    <h1>요금제 (결제 시스템 준비 중)</h1>
  </div>

  <div class="iwt-body">
  <p class="pricing-subtitle">신규 가입 시 Pro 플랜을 30일간 무료로 체험할 수 있어요</p>

  <div class="pricing-grid">
    <div class="pricing-card">
      <h3>Free</h3>
      <div class="price">무료</div>
      <ul>
        <li>활성 이벤트 3개</li>
        <li>이벤트당 사진 50장</li>
        <li>동영상 미지원</li>
        <li>사진 1장당 최대 8MB</li>
        <li>48시간 보관</li>
        <li>타인 얼굴 자동 모자이크 (항상 켜짐)</li>
      </ul>
    </div>
    <div class="pricing-card featured">
      <h3>Pro</h3>
      <div class="price">가격 미정</div>
      <ul>
        <li>활성 이벤트 50개</li>
        <li>이벤트당 사진 500장</li>
        <li>이벤트당 동영상 50개 (최대 500MB)</li>
        <li>사진 1장당 최대 15MB</li>
        <li>168시간(7일) 보관</li>
        <li>타인 얼굴 모자이크 on/off 선택 가능</li>
      </ul>
    </div>
  </div>
  </div>
</div>

---

<!-- CTA -->
<div class="iwt-cta">
  <h1>지금 시작하세요</h1>
  <p>이벤트 사진 관리,<br/>iwasthere가 해결해 드립니다</p>
  <a href="https://iwasthere.pics" class="cta-button">무료로 시작하기 →</a>

  <div style="margin-top: 2.5rem; opacity: 0.7; font-size: 0.85rem;">
    <a href="https://iwasthere.pics" target="_blank" style="color: inherit; text-decoration: none;">https://iwasthere.pics</a>
  </div>

  <div class="iwt-contact">
    <span>✉️ support@iwasthere.pics</span>
    <span>📷 <a href="http://instagram.com/whyyanmoves" target="_blank" style="color: inherit; text-decoration: none;">@whyyanmoves</a></span>
    <span>📞 010-5665-9614</span>
  </div>
</div>
