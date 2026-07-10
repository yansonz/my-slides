import { defineConfig } from '@slidev/cli'

export default defineConfig({
  title: 'iwasthere — 이벤트 사진, 내 얼굴만 찾아주는 서비스',
  theme: 'default',
  fonts: {
    sans: 'Pretendard, Inter',
    serif: 'Pretendard, Inter',
    mono: 'Fira Code',
  },
  export: {
    format: 'pdf',
    timeout: 30000,
    dark: false,
    withClicks: false,
  },
})
