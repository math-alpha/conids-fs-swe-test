import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('@/views/AboutView.vue')
    },{
      path: "/purchases",
      alias: "/purchases",
      name: "purchases",
      component: () => import("@/components/PurchasesList.vue"),
    },
    {
      path: "/purchases/:id",
      name: "purchases-details",
      component: () => import("@/components/PurchaseDetails.vue"),
    },
    {
      path: "/add-purchases",
      name: "add-purchases",
      component: () => import("@/components/AddPurchase.vue"),
    },
  ]
})

export default router
