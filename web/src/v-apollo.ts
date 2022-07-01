import { ApolloClient, ApolloLink, createHttpLink, HttpLink, InMemoryCache } from "@apollo/client/core";
import { createApolloProvider } from "@vue/apollo-option";
import { createUploadLink } from "apollo-upload-client";

const prod = false;
const uri = prod ? "https://mooyats.com/graphql/" : "http://127.0.0.1:8000/graphql/"

export const httpLink = createHttpLink({
    uri,
    credentials: "include",
});


export const apolloClient = new ApolloClient({
    cache: new InMemoryCache(),
    connectToDevTools: true,
    credentials: "include",
    link: ApolloLink.from([
        createUploadLink({
            uri: uri,
            credentials: "include",
        })
    ]),
    uri: uri,
});

// Create the apollo client
// export const apolloClient = new ApolloClient({
//     link: httpLink,
//     cache: new InMemoryCache(),
//     connectToDevTools: true,
//     credentials: "include"
// });

// Create a provider
export const apolloProvider = createApolloProvider({
    defaultClient: apolloClient,
});
