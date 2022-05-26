// import { createStore, useStore, Store } from "vuex";
// import { InjectionKey } from "vue";

// export interface State {
//   user: any;
//   token: any;
// }
// export const key: InjectionKey<Store<State>> = Symbol();

// export const store = createStore<State>({
//   state: {
//     user: null,
//     token: null,
//   },
//   mutations: {
//     setUser(state, user) {
//       state.user = user;
//     },
//     setToken(state, token) {
//       state.user = token;
//     },
//   },
//   getters: {
//     isAuthenticated(state) {
//       return !!state.token;
//     },
//   },
// });
import { InjectionKey } from "vue";
import { createStore, useStore as baseUseStore, Store } from "vuex";

export interface State {
  token: boolean;
}

export const key: InjectionKey<Store<State>> = Symbol();

export const store = createStore<State>({
  state: {
    token: false,
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
    },
  },
});

// define your own `useStore` composition function
export function useStore() {
  return baseUseStore(key);
}
