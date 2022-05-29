import { createRouter, createWebHistory } from "vue-router";
import Index from "../pages/Index.vue";
import Login from "../pages/Login.vue";
import Dashboard from "../pages/Dashboard.vue";
import { authguard, loginPageGuard } from "../utils/authGuard";

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
      beforeEnter: (to, from, next) => {
        loginPageGuard(to, from, next);
      },
    },
    {
      path: "/dashboard",
      name: "dashboard",
      component: Dashboard,
      beforeEnter: (to, from, next) => {
        authguard(to, from, next);
      },
    },
  ],
});
