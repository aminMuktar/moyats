import { InjectionKey } from "vue";
import { createStore, useStore as baseUseStore, Store } from "vuex";
import createPersistedState from "vuex-persistedstate";

export interface State {
  token: boolean;
}

export const key: InjectionKey<Store<State>> = Symbol();
export const CoreModule = {
  state: {
    token: false,
    test: ""
  },
  mutations: {
    setTest(state: any, token: any) {
      state.test = token
    },
    setToken(state: any, token: any) {
      state.token = token;
    },
  },
}

export const store = createStore<State>({
  modules: {
    core: CoreModule
  },
  plugins: [createPersistedState({
    storage: window.localStorage,
    paths: ["core.token", "core.test"],
  })],
});

// define your own `useStore` composition function
export function useStore() {
  return baseUseStore(key);
}

