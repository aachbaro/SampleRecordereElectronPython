import { createRouter, createWebHistory } from 'vue-router';
import HomeComponent from '../views/Home.vue';

const routes = [
  {
    path: '/',
    name: 'HomeComponent',
    component: HomeComponent
  }
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});

export default router;