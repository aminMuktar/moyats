import { createApp } from "vue";
import App from "./App.vue";
import "./index.css";
import { ApolloClient, HttpLink, InMemoryCache } from "@apollo/client/core";
import { createApolloProvider } from "@vue/apollo-option";
import Router from "./routes/index";
import { key, store } from "./store";

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

createApp(App).use(apolloProvider).use(Router).use(store, key).mount("#app");
