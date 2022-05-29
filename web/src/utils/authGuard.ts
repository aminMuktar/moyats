import { store } from "./../store/index";
import router from "../routes";

const cook = store.state.core.token;

export const authguard = (to: any, form: any, next: any) => {
  cook ? next() : router.push("/login");
};

export const loginPageGuard = (to: any, from: any, next: any) => {
  cook ? router.push("/dashboard") : next();
};
