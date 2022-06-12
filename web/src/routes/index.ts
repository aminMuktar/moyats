import { createRouter, createWebHistory } from "vue-router";
import Index from "../pages/Index.vue";
import Login from "../pages/Login.vue";
import Dashboard from "../pages/dashboard/Dashboard.vue";
import DashHome from "../pages/dashboard/DashHome.vue";
import Activities from "../pages/dashboard/Activities.vue";
import JobOrders from "../pages/dashboard/JobOrders.vue";
import JobOrder from "../pages/dashboard/JobOrdersPage.vue";
import Candidates from "../pages/dashboard/Candidates.vue";
import Candidate from "../pages/dashboard/CandidatePage.vue";
import Companies from "../pages/dashboard/Companies.vue";
import Company from "../pages/dashboard/CompanyPage.vue";
import Contacts from "../pages/dashboard/Contacts.vue";
import Contact from "../pages/dashboard/ContactPage.vue"
import Reports from "../pages/dashboard/Reports.vue";
import CompanySetup from "../pages/CompanySetup.vue";
import AccountSettings from "../pages/dashboard/AccountSettings.vue";
import CompanyManagement from "../pages/dashboard/CompanyManagement.vue";
import NotFound from "../pages/errors/NotFound.vue";

import {
  authguard,
  loginPageGuard,
  profileStatusGuard,
} from "../utils/authGuard";

export default createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/:pathMatch(.*)*",
      name: "404",
      component: NotFound,
    },
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
      path: "/$#asdfqwerqwer",
      name: "MainDashboard",
      component: Dashboard,
      beforeEnter: (to, from, next) => {
        authguard(to, from, next);
      },
      children: [
        {
          path: "/dashboard",
          name: "DashHome",
          component: DashHome,
        },
        {
          path: "/activities",
          name: "Activities",
          component: Activities,
        },
        {
          path: "/joborders",
          name: "JobOrders",
          component: JobOrders,
        },
        {
          path: "/joborders/:jid",
          name: "JobOrder",
          component: JobOrder,
        },
        {
          path: "/candidates",
          name: "Candidates",
          component: Candidates,
        },
        {
          path: "/candidates/:cid",
          name: "Candidate",
          component: Candidate,
        },
        {
          path: "/companies",
          name: "Companies",
          component: Companies,
        },
        {
          path: "/companies/:cpid",
          name: "Company",
          component: Company,
        },
        {
          path: "/contacts",
          name: "Contacts",
          component: Contacts,
        },
        {
          path: "/contacts/:cid",
          name: "Contact",
          component: Contact,
        },
        {
          path: "/reports",
          name: "Reports",
          component: Reports,
        },
        {
          path: "/account-settings",
          name: "AccountSttings",
          component: AccountSettings,
        },
      ],
    },
    {
      path: "/company-management",
      name: "CompanyManagement",
      component: CompanyManagement,
      beforeEnter: (to, from, next) => {
        authguard(to, from, next);
      },
    },
    {
      path: "/company-setup",
      name: "CompanySetup",
      component: CompanySetup,
      beforeEnter: (to, from, next) => {
        profileStatusGuard(to, from, next);
      },
    },
  ],
});
