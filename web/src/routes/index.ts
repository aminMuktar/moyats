import { createRouter, createWebHistory } from "vue-router";
import Index from "../pages/Index.vue";
import Login from "../pages/Login.vue";

export default createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "index",
      component: Index,
    },
    {
      path: "/login",
      name: "login",
      component: Login,
    },
  ],
});
