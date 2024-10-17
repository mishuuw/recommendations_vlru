import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/components/views/MainView.vue'
import SomePageView from '@/components/views/SomePageView.vue'
import RegistrationView from '@/components/views/RegistrationView.vue'
import AuthorizationView from '@/components/views/AuthorizationView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/some-page',
      name: 'some-page',
      component: SomePageView
    },
    {
      path: '/registration',
      name: 'registration',
      component: RegistrationView
    },
    {
      path: '/authorization',
      name: 'authorization',
      component: AuthorizationView
    }
  ]
})
  
export default router
  