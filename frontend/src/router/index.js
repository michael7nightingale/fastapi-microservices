import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import LoginView from "@/views/LoginView.vue";
import ShopView from "@/views/ShopView.vue";
import ProductView from "@/views/ProductView.vue";
import CartView from "@/views/CartView.vue";
import RegisterView from "@/views/RegisterView.vue";
import CategoryView from "@/views/CategoryView.vue";
import SubcategoryView from "@/views/SubcategoryView.vue";
import NavigationView from "@/views/NavigationView.vue";


const routes = [
  {
    path: '/',
    name: 'homepage',
    component: HomeView
  },
  {
    path: '/auth/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/auth/register',
    name: 'register',
    component: RegisterView
  },
  {
    path: "/navigation",
    name: "navigation",
    component: NavigationView
  },
  {
    path: '/shop',
    name: 'shop',
    component: ShopView
  },
  {
    path: '/shop/:category_id',
    name: 'category',
    component: CategoryView
  },
  {
    path: '/shop/:category_id/:subcategory_id',
    name: 'subcategory',
    component: SubcategoryView
  },
  {
    path: '/product/:id',
    name: 'product',
    component: ProductView
  },
  {
    path: '/cart',
    name: 'cart',
    component: CartView
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
