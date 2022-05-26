import { createRouter, createWebHistory } from "vue-router";
import Index from "./Index.vue";
import Login from "./Login.vue";

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
