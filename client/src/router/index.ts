import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/job-description',
      name: 'job-description',
      component: () => import('../views/JobDescriptionView.vue')
    }
  ]
})

export default router
