import { ApolloClient, createHttpLink, HttpLink, InMemoryCache } from "@apollo/client/core";
import { createApolloProvider } from "@vue/apollo-option";

const prod = true;
const uri = prod ? "https://mooyats.com/graphql/" : "http://127.0.0.1:8000/graphql/"
export const httpLink = createHttpLink({
    uri,
    credentials: "include",
});

// Create the apollo client
export const apolloClient = new ApolloClient({
    link: httpLink,
    cache: new InMemoryCache(),
    connectToDevTools: true,
    credentials: "include"
});

// Create a provider
export const apolloProvider = createApolloProvider({
    defaultClient: apolloClient,
});
