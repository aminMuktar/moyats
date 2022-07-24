import { store } from "./../store/index";
import router from "../routes";

const token = store.state.core.token;
const ustate = store.state.core.u

export const authguard = (to: any, form: any, next: any) => {
  if (!token) {
    router.push("/login")
  }
  else if (!ustate) {
    router.push("/login")
  } else if (!ustate.setupComplete) {
    router.push("/company-setup")
  }
  next()
};

export const loginPageGuard = (to: any, from: any, next: any) => {
  token ? router.push("/dashboard") : next();
};


export const profileStatusGuard = (to: any, from: any, next: any) => {
  if (!ustate) {
    router.push("/login")
  }
  if (!token) {
    router.push("/login")
  }
  if (!ustate.setupComplete && ustate) {
    next()
  } else {
    router.push("/dashboard")
  }
}


export const jobOrderRouteHandler = (to: any, from: any, next: any) => {
  store.commit("setActiveSlideWindow", "joborders")
  next()
}


export const candidatesRouteHandler = (to: any, from: any, next: any) => {
  store.commit("setActiveSlideWindow", "candidates")
  next()
}

export const companiesRouteHandler = (to: any, from: any, next: any) => {
  store.commit("setActiveSlideWindow", "companies")
  next()
}

export const contactsRouteHandler = (to: any, from: any, next: any) => {
  store.commit("setActiveSlideWindow", "contacts")
  next()
}