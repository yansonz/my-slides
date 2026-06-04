import { defineConfig } from '@slidev/cli'

export default defineConfig({
  title: 'Kiro 한국 사용자 모임 2026 상반기 회고',
  theme: 'default',
  fonts: {
    sans: 'Roboto',
    serif: 'Roboto Slab',
    mono: 'Fira Code',
  },
  export: {
    format: 'pdf',
    timeout: 30000,
    dark: false,
    withClicks: false,
  },
})
