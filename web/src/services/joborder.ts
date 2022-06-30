import * as q from "../queries/joborder"
import { apolloClient } from "../v-apollo"

export const fetchPositionTypes = async () => {
    const res = await apolloClient.query({
        query: q.POSITION_TYPES
    })
    return res
}

export const fetchJoborderTypes = async () => {
    const res = await apolloClient.query({
        query: q.JOB_ORDER_TYPES
    })
    return res
}

export const fetchJoborderStatuses = async () => {
    const res = await apolloClient.query({
        query: q.JOB_ORDER_STATUS
    })
    return res
}

export const fetchJoborderCategories = async () => {
    const res = await apolloClient.query({
        query: q.JOBORDER_CATEGORIES
    })
    return res
}

export const fetchApplications = async () => {
    const res = await apolloClient.query({
        query: q.APPLICATIONS
    })
    return res
}

export const searchCompanyContacts = async (variables: any) => {
    const res = await await apolloClient.query({
        query: q.COMPANY_CONTACTS,
        variables
    })
    return res
}

export const addJobOrder = async (variables: any) => {
    const res = await await apolloClient.mutate({
        mutation: q.ADD_JOBORDER,
        variables
    })
    return res
}

export const updateJobOrderPrimary = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: q.UPDATE_JOBORDER_PRIMARY,
        variables
    })
    return res
}

export const updateJoborderDetail = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: q.UPDATE_JOBORDER_DETAIL,
        variables
    })
    return res
}

export const updateJoborderCompany = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: q.UPDATE_JOBORDER_COMPANY,
        variables
    })
    return res
}