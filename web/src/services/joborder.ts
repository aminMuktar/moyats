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
        query: q.APPLICATIONS,
        fetchPolicy: "network-only"
    })
    return res
}

export const fetchApplication = async (variables: any) => {
    const res = await apolloClient.query({
        query: q.APPLICATION,
        variables
    })
    return res
}

export const fetchApplicationQuestions = async (variables: any) => {
    const res = await apolloClient.query({
        query: q.APPLICATION_QUESTIONS,
        fetchPolicy: "network-only",
        variables
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


export const updateJoborderDescription = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: q.UPDATE_JOBORDER_DESC,
        variables
    })
    return res
}

export const updateJoborderNotes = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: q.UPDATE_JOBORDER_NOTES,
        variables
    })
    return res
}

export const saveApplicationDetails = async () => {
    const res = await apolloClient.query({
        query: q.SAVE_APP_DETAIL_TYPES
    })
    return res
}

export const saveApplicationQuestion = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: q.SAVE_APP_QUESTION,
        variables
    })
    return res
}

export const addApplication = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: q.ADD_APPLICATION,
        variables
    })
    return res
}



export const updateJobOrderStatus = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: q.UPDATE_JOB_ORDER_STATUS,
        variables
    })
    return res
}

export const loadJobOrderApplications = async (variables: any) => {
    const res = await apolloClient.query({
        query: q.JOBORDER_PIPELINES,
        fetchPolicy: "network-only",
        variables
    })
    return res
}