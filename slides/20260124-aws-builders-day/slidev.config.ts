import { defineConfig } from '@slidev/cli'

export default defineConfig({
  title: '발표 제목',
  theme: 'default',
  colorSchema: 'dark',
  fonts: {
    sans: 'Noto Sans KR',
    serif: 'Noto Serif KR',
    mono: 'Fira Code',
  },
  export: {
    format: 'pdf',
    timeout: 30000,
    dark: true,
    withClicks: false,
  },
})
