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
    u: null,
    activities: null,
    formupdateStatus: null,
    activeSlideWindow: "",
    activateSlider: false,
    scompany: "null",
  },
  mutations: {
    setScompany(state, payload) {
      state.scompany = payload;
    },
    setActiveSlideWindow(state, payload) {
      state.activeSlideWindow = payload;
    },
    updateFormupdateStatus(state: any, data: any) {
      state.formupdateStatus = data
    },
    clearToken(state: any) {
      state.token = false;
    },
    saveUdata(state: any, data: any) {
      state.u = data;
    },
    setToken(state: any, token: any) {
      state.token = token;
    },
    setActivities(state: any, activities: any) {
      state.activities = activities;
    },
    setActivateSlider(state: any, payload: any) {
      state.activateSlider = payload;
    }
  },
  getters: {
    getFormupdateStatus(state) {
      return state.formupdateStatus
    },
    getActiveSlideWindow(state) {
      return state.activeSlideWindow
    },
    getActivateSlider(state) {
      return state.activateSlider
    },
    getscompany(state) {
      return state.scompany
    }
  }
};

export const store = createStore<State>({
  modules: {
    core: CoreModule,
  },
  plugins: [
    createPersistedState({
      storage: window.localStorage,
      paths: ["core.token", "core.u", "core.activities", "core.activeSlideWindow", "core.scompany"],
    }),
  ],
});

// define your own `useStore` composition function
export function useStore() {
  return baseUseStore(key);
}
