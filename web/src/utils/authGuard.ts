import { store } from "./../store/index";
import router from "../routes";

export const authguard = (to: any, form: any, next: any) => {
  const cook = store.state.core.token;
  if (cook) {
    next();
  } else {
    router.push("/login");
  }
};
