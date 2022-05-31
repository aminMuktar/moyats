import { createRouter, createWebHistory } from "vue-router";
import Index from "../pages/Index.vue";
import Login from "../pages/Login.vue";
import Dashboard from "../pages/dashboard/Dashboard.vue";
import DashHome from '../pages/dashboard/DashHome.vue'
import Activities from '../pages/dashboard/Activities.vue'
import JobOrders from '../pages/dashboard/JobOrders.vue'
import Candidates from '../pages/dashboard/Candidates.vue'
import Companies from '../pages/dashboard/Companies.vue'
import Contacts from '../pages/dashboard/Contacts.vue'
import Reports from '../pages/dashboard/Reports.vue'
import CompanySetup from '../pages/CompanySetup.vue'

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
      path: "/asdfasdfqwerqwer",
      name: "MainDashboard",
      component: Dashboard,
      beforeEnter: (to, from, next) => {
        authguard(to, from, next);
      },
      children: [
        {
          path: "/dashboard",
          name: "DashHome",
          component: DashHome
        },
        {
          path: "/activities",
          name: "Activities",
          component: Activities
        },
        {
          path: "/joborders",
          name: "JobOrders",
          component: JobOrders
        },
        {
          path: "/candidates",
          name: "Candidates",
          component: Candidates
        },
        {
          path: "/companies",
          name: "Companies",
          component: Companies
        },
        {
          path: "/contacts",
          name: "Contacts",
          component: Contacts
        },
        {
          path: "/reports",
          name: "Reports",
          component: Reports
        },
      ]
    },
    {
      path: "/company-setup",
      name: "CompanySetup",
      component: CompanySetup,
      // beforeEnter: (to, from, next) => {
      //   loginPageGuard(to, from, next);
      // },
    },
  ],
});
