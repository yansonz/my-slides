import { defineConfig } from '@slidev/cli'

export default defineConfig({
  title: '발표 제목',
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
