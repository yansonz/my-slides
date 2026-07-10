import { defineConfig } from '@slidev/cli'

export default defineConfig({
  title: 'iwasthere — 크로스핏 박스를 위한 회원 사진·영상 공유',
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
