import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import '@/assets/style.global.scss'

const enableMocking = async () => {
  if (!import.meta.env.VITE_API_MOCK) return

  const { worker } = await import('../mocks/browser')

  return worker.start({ onUnhandledRequest: 'bypass' })
}

enableMocking().then(() => {
  const app = createApp(App)

  app.use(router)

  app.mount('#app')
})
