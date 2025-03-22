import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
    server: {
      proxy: {
        '/api': {
          target: 'https://legendary-carnival-gp75wwr5xx5cwv5j-8000.app.github.dev',
          changeOrigin: true,
          secure: false,
        },
      },
    },
})
