import { createApp } from "vue";
import App from "./App.vue";
import "./index.css";
import { ApolloClient, HttpLink, InMemoryCache } from "@apollo/client/core";
import { createApolloProvider } from "@vue/apollo-option";
import Router from "./routes/index";
import { key, store } from "./store";
import { FIREBASE_CONFIG } from './firebase.config'
import * as firebase from '@firebase/app';
import '@firebase/messaging';


const app = firebase.initializeApp(FIREBASE_CONFIG)
// navigator.serviceWorker.register('./static/firebase-messaging-sw.js', {
//     scope: "firebase-cloud-messaging-push-scope"
// }).then((registration) => {
//     const messaging = firebase.messaging()
//     console.warn(messaging)
//     messaging.useServiceWorker(registration)
// }).catch(err => {
//     console.error(err);
// })

const httpLink = new HttpLink({
  // You should use an absolute URL here
  uri: "http://127.0.0.1:8000/graphql/",
  credentials: "include",
});

// Create the apollo client
const apolloClient = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache(),
  connectToDevTools: true,
});

// Create a provider
const apolloProvider = createApolloProvider({
  defaultClient: apolloClient,
});

const maap = createApp(App)
maap.use(apolloProvider)
maap.use(Router)
maap.use(store, key)
maap.mount("#app");
maap.config.globalProperties.$fapp = app