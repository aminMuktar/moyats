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

export const updateCandidateWorkhistory = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: q.UPDATE_CAND_WORK_HISTORY,
        variables
    })
    return res
}

export const addCandidateWorkhistory = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: q.ADD_CAND_WORK_HISTORY,
        variables
    })
    return res
}

export const removeCandidateWorkhistory = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: q.DELETE_CAND_WORK_HISTORY,
        variables
    })
    return res
}

export const updateCandidatePrimary = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: q.UPDATE_CAND_PRIMARY,
        variables
    })
    return res
}


export const updateCandidateDetail = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: q.UPDATE_CAND_DETAIL,
        variables
    })
    return res
}

export const updateCandidateNotes = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: q.UPDATE_CAND_NOTES,
        variables
    })
    return res
}

export const updateCompanyPrimary = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: q.UPDATE_COMP_PRIMARY,
        variables
    })
    return res
}

export const updateContactPrimary = async (variables: any) => {
    const res = await apolloClient.mutate({
        mutation: q.UPDATE_CONTACT_PRIMARY,
        variables
    })
    return res
}

export const candidateApplicationJoborders = async (variables: any) => {
    const res = await apolloClient.query({
        query: q.CANDIDATE_APP_JOBORDERS,
        variables
    })
    return res
}