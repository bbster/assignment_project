import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import Components from 'unplugin-vue-components/vite'
import AutoImport from 'unplugin-auto-import/vite'

// https://vitejs.dev/config/
export default defineConfig({
  build: {
    emptyOutDir: true,
    rollupOptions: {
      output: {
        dir: '../server/templates/job_description',
        assetFileNames: (assetInfo) => {
          let extType = assetInfo?.name?.split('.').at(-1)
          if (!extType) return `assets/[name]-[hash][extname]`

          if (/png|jpe?g|svg|gif|tiff|bmp|ico/i.test(extType)) {
            extType = 'img'
          }
          return `assets/${extType}/[name]-[hash][extname]`
        },
        chunkFileNames: 'assets/js/[name]-[hash].js',
        entryFileNames: 'assets/js/[name]-[hash].js'
      }
    }
  },
  plugins: [
    vue(),
    AutoImport({
      dts: './auto-imports.d.ts',
      include: [/\.ts?$/],
      dirs: ['./composables', './composables/**'],
      imports: ['vue', 'vue-router', '@vueuse/core']
    }),
    Components({
      dts: './components.d.ts',
      dirs: ['src/components'],
      directoryAsNamespace: false,
      extensions: ['vue'],
      types: [
        {
          from: 'vue-router',
          names: ['RouterLink', 'RouterView']
        }
      ]
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
