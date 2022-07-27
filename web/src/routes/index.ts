import { createRouter, createWebHistory } from "vue-router";
import Index from "../pages/Index.vue";
import Login from "../pages/Login.vue";
import Dashboard from "../pages/dashboard/Dashboard.vue";
import DashHome from "../pages/dashboard/DashHome.vue";
import Activities from "../pages/dashboard/Activities.vue";
import JobOrders from "../pages/dashboard/JobOrders.vue";
import JobOrder from "../pages/dashboard/JobOrdersPage.vue";
import Workflows from "../pages/dashboard/Workflows.vue"
import WorkflowPage from "../pages/dashboard/WorkflowPage.vue"
import Candidates from "../pages/dashboard/Candidates.vue";
import Candidate from "../pages/dashboard/CandidatePage.vue";
import Companies from "../pages/dashboard/Companies.vue";
import Company from "../pages/dashboard/CompanyPage.vue";
import Contacts from "../pages/dashboard/Contacts.vue";
import Applications from "../pages/dashboard/Applications.vue"
import Contact from "../pages/dashboard/ContactPage.vue";
import Reports from "../pages/dashboard/Reports.vue";
import CompanySetup from "../pages/CompanySetup.vue";
import AccountSettings from "../pages/dashboard/AccountSettings.vue";
import CompanyManagement from "../pages/dashboard/CompanyManagement.vue";
import NotFound from "../pages/errors/NotFound.vue";
import Activity from "../pages/dashboard/ActivityDetail.vue";
import ApplicationPage from "../pages/dashboard/ApplicationPage.vue"

import {
  authguard,
  candidatesRouteHandler,
  companiesRouteHandler,
  contactsRouteHandler,
  basicRouteHandler,
  jobOrderRouteHandler,
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
          beforeEnter: (to, from, next) => {
            basicRouteHandler(to, from, next);
          },
        },
        {
          path: "/activities",
          name: "Activities",
          component: Activities,
          beforeEnter: (to, from, next) => {
            basicRouteHandler(to, from, next);
          },
        },
        {
          path: "/activity/:aid",
          name: "Activity",
          component: Activity,
        },
        {
          path: "/joborders",
          name: "JobOrders",
          component: JobOrders,
          beforeEnter: (to, from, next) => {
            jobOrderRouteHandler(to, from, next);
          },
        },
        {
          path: "/joborders/:jid",
          name: "JobOrder",
          component: JobOrder,
          beforeEnter: (to, from, next) => {
            jobOrderRouteHandler(to, from, next);
          },
        },
        {
          path: "/workflows",
          name: "Workflows",
          component: Workflows,
          beforeEnter: (to, from, next) => {
            basicRouteHandler(to, from, next);
          },
        },
        {
          path: "/workflows/:wid",
          name: "Workflow",
          component: WorkflowPage,
          beforeEnter: (to, from, next) => {
            basicRouteHandler(to, from, next);
          },
        },
        {
          path: "/applications",
          name: "Applications",
          component: Applications,
          beforeEnter: (to, from, next) => {
            basicRouteHandler(to, from, next);
          },
        },
        {
          path: "/applications/:appid",
          name: "ApplicationPage",
          component: ApplicationPage,
          beforeEnter: (to, from, next) => {
            basicRouteHandler(to, from, next);
          },
        },
        {
          path: "/candidates",
          name: "Candidates",
          component: Candidates,
          beforeEnter: (to, from, next) => {
            candidatesRouteHandler(to, from, next);
          },
        },
        {
          path: "/candidates/:cid",
          name: "Candidate",
          component: Candidate,
          beforeEnter: (to, from, next) => {
            candidatesRouteHandler(to, from, next);
          },
        },
        {
          path: "/companies",
          name: "Companies",
          component: Companies,
          beforeEnter: (to, from, next) => {
            companiesRouteHandler(to, from, next);
          },
        },
        {
          name: "Company",
          component: Company,
          path: "/companies/:cpid",
          beforeEnter: (to, from, next) => {
            companiesRouteHandler(to, from, next);
          },
        },
        {
          path: "/contacts/:cid",
          name: "Contact",
          component: Contact,
          beforeEnter: (to, from, next) => {
            contactsRouteHandler(to, from, next);
          },
        },
        {
          path: "/contacts",
          name: "Contacts",
          component: Contacts,
          beforeEnter: (to, from, next) => {
            contactsRouteHandler(to, from, next);
          },
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
