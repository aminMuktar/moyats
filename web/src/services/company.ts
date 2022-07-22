import { apolloClient } from "../v-apollo"
import { ADD_CONTACT } from "../queries/contact"
import { ADD_COMPANY, SEARCH_COMPANY, SEARCH_RECRUITER } from "../queries/company"

export const searchCompany = async (query: string) => {
    const res = await apolloClient.query({
        query: SEARCH_COMPANY,
        fetchPolicy: "network-only",
        variables: {
            query: query
        }
    })
    return res
}

export const searchRecruiter = async (query: string) => {
    const res = await apolloClient.query({
        query: SEARCH_RECRUITER,
        fetchPolicy: "network-only",
        variables: {
            query: query
        }
    })
    return res
}

export const addCompany = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: ADD_COMPANY,
        variables
    })
    return res
}

export const addContact = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: ADD_CONTACT,
        variables
    })
    return res
}