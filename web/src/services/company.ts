import { SEARCH_COMPANY, SEARCH_RECRUITER } from "../queries/company"
import { APPLICATIONS, JOBORDER_CATEGORIES, JOB_ORDER_STATUS, JOB_ORDER_TYPES, POSITION_TYPES } from "../queries/joborder"
import { apolloClient } from "../v-apollo"

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