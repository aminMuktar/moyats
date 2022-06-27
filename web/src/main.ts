import { createApp } from "vue";
import App from "./App.vue";
import "./index.css";
import VueApexCharts from "vue3-apexcharts";
import Router from "./routes/index";
import { key, store } from "./store";
import { FIREBASE_CONFIG } from './firebase.config'
import * as firebase from '@firebase/app';
import VueTelInput from 'vue-tel-input';
import 'vue-tel-input/dist/vue-tel-input.css';
import '@firebase/messaging';
import { apolloProvider } from "./v-apollo";

const app = firebase.initializeApp(FIREBASE_CONFIG)

const maap = createApp(App)
maap.use(apolloProvider)
maap.use(Router)
maap.use(store, key)
maap.use(VueApexCharts);
maap.use(VueTelInput)
maap.mount("#app");
maap.config.globalProperties.$fapp = app