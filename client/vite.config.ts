import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import Components from 'unplugin-vue-components/vite'
import AutoImport from 'unplugin-auto-import/vite'

const buildDir = '../server/templates/assignment_templates'
const assetsBuildDir = 'assets'

// https://vitejs.dev/config/
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        dir: buildDir,
        assetFileNames: (assetInfo) => {
          let extType = assetInfo?.name?.split('.').at(-1)
          if (!extType) return `${assetsBuildDir}/[name]-[hash][extname]`

          if (/png|jpe?g|svg|gif|tiff|bmp|ico/i.test(extType)) {
            extType = 'img'
          }
          return `${assetsBuildDir}/${extType}/[name]-[hash][extname]`
        },
        chunkFileNames: `${assetsBuildDir}/js/[name]-[hash].js`,
        entryFileNames: `${assetsBuildDir}/js/[name]-[hash].js`
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
