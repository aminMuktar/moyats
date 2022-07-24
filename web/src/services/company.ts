import { apolloClient } from "../v-apollo"
import { ADD_CONTACT, UPDATE_CONTACT_DETAIL, UPDATE_CONTACT_NOTES } from "../queries/contact"
import { ADD_COMPANY, COMPANY_CONTACTS, SEARCH_COMPANY, SEARCH_RECRUITER } from "../queries/company"

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

export const updateContactDetails = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: UPDATE_CONTACT_DETAIL,
        variables
    })
    return res
}

export const updateContactNotes = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: UPDATE_CONTACT_NOTES,
        variables
    })
    return res
}

export const loadCompanyContacts = async (variables: any) => {
    const res = await apolloClient.query({
        query: COMPANY_CONTACTS,
        fetchPolicy: "network-only",
        variables
    })
    return res
}