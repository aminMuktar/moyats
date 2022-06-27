import { APPLICATIONS, JOBORDER_CATEGORIES, JOB_ORDER_STATUS, JOB_ORDER_TYPES, POSITION_TYPES } from "../queries/joborder"
import { apolloClient } from "../v-apollo"

export const fetchPositionTypes = async () => {
    const res = await apolloClient.query({
        query: POSITION_TYPES
    })
    return res
}

export const fetchJoborderTypes = async () => {
    const res = await apolloClient.query({
        query: JOB_ORDER_TYPES
    })
    return res
}

export const fetchJoborderStatuses = async () => {
    const res = await apolloClient.query({
        query: JOB_ORDER_STATUS
    })
    return res
}

export const fetchJoborderCategories = async () => {
    const res = await apolloClient.query({
        query: JOBORDER_CATEGORIES
    })
    return res
}

export const fetchApplications = async () => {
    const res = await apolloClient.query({
        query: APPLICATIONS
    })
    return res
}