import * as q from "../queries/candidates"
import { apolloClient } from "../v-apollo"

export const candidateSources = async () => {
    const res = await apolloClient.query({
        query: q.CANDIDATE_SOURCES
    })
    return res
}

export const addCandidate = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: q.ADD_CANDIDATE,
        variables
    })
    return res
}


export const fetchCandidate = async (variables: any) => {
    const res = await apolloClient.query({
        query: q.CANDIDATE,
        fetchPolicy: "network-only",
        variables
    })
    return res
}