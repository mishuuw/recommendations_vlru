import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/components/views/MainView.vue'
import SomePageView from '@/components/views/SomePageView.vue'
import RegistrationView from '@/components/views/RegistrationView.vue'
import AuthorizationView from '@/components/views/AuthorizationView.vue'
import PostersView from '@/components/views/PostersView.vue'
import FavoritesView from '@/components/views/FavoritesView.vue'
import PurchaseView from '@/components/views/PurchaseView.vue'

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
    },
    {
      path: '/posters',
      name: 'posters',
      component: PostersView
    },
    {
      path: '/favorites', 
      name: 'favorites', 
      component: FavoritesView
    },
    {
      path: '/history', 
      name: 'history', 
      component: PurchaseView
    }
  ]
})
  
export default router
  