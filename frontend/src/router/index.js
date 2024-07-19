import { createRouter, createWebHistory } from "vue-router";
import HomeComponent from "../views/Home.vue";
import RecordWidget from "@/views/RecordWidget.vue";

const routes = [
  {
    path: "/",
    name: "HomeComponent",
    component: HomeComponent,
  },
  {
    path: "/record",
    name: "RecordWidget",
    component: RecordWidget
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
