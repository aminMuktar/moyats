import gql from "graphql-tag"

export const CANDIDATE = gql`query candidate($candidate: UUID!) {
  candidate(candidate: $candidate) {
    candidateId
    notes
    active
    phones{
      cellNumber
      homeNumber
      workNumber
    }
    source{
      id
      name
    }
    workHistory {
      id
      title
      startDate
      endDate
      currentlyWorking
      reasonForLeaving
      employeer
    }
    latestJoborder {
      id
      joborderId
      jobDetail {
        title
      }
      company {
        id
        name
        companyId
      }
      jobOrderStatus {
        statusName
        color {
          hex
        }
      }
      createdAt
      updatedAt
    }
    pipeline {
      id
    }
    organization {
      name
    }
    candidateProfile {
      id
      firstName
      lastName
      email
    }
    address {
      country
      city
    }
    keySkills
    currentEmployeer
    dateAvailable
    currentPay
    desiredPay
    createdAt
    updatedAt
    attachments{
      file
      filename
      isResume
    }
  }
}
`

export const CANDIDATES = gql`query candidtes($page: Int!, $pageSize: Int!) {
  candidtes(page: $page, pageSize: $pageSize) {
    page
    pages
    hasNext
    hasPrev
    total
    objects {
      candidateId
      latestJoborder{
        id
        joborderId
        jobDetail{
          title
        }
        company{
          id
          name
          companyId
        }
        jobOrderStatus{
          statusName
          color{
            hex
          }
        }
        createdAt
      }
      pipeline{
        id
      }
      organization{
        name
      }
      candidateProfile{
        id
        firstName
        lastName
      }
      address{
        country
        city
      }
      updatedAt
    }
  }
}
`

export const ADD_CANDIDATE = gql`mutation addCandidate($input: CandidateInput, $attachments:Upload!) {
  addCandidate(input: $input, attachments:$attachments) {
    response {
      id
      candidateId
    }
  }
}
`

export const CANDIDATE_SOURCES = gql`query {
  candidateSources {
    id
    name
  }
}
`
export const ADD_CAND_WORK_HISTORY = gql`mutation addCandidateWorkhistory(
  $candidate: UUID!
  $input: CandidateWorkHistoryInput!
) {
  addCandidateWorkhistory(candidate: $candidate, input: $input) {
    response
  }
}`

export const UPDATE_CAND_WORK_HISTORY = gql`mutation updateCandidateWorkhistory(
  $candidiate: UUID!
  $input: CandidateWorkHistoryInput!
  $whistory: Int!
) {
  updateCandidateWorkhistory(
    candidate: $candidiate
    input: $input
    whistory: $whistory
  ) {
    response
  }
}
`

export const DELETE_CAND_WORK_HISTORY = gql`mutation removeCandidateWorkhistory($candidate: UUID!, $whid:Int!) {
  removeCandidateWorkhistory(candidate: $candidate,whid:$whid) {
    response
  }
}
`

export const UPDATE_CAND_PRIMARY = gql`mutation updateCandidatePrimary(
  $candidate: UUID!
  $input: CandidatePrimaryInput!
) {
  updateCandidatePrimary(candidate: $candidate, input: $input) {
    response
  }
}
`

export const UPDATE_CAND_DETAIL = gql`mutation updateCandidateDetail(
  $candidate: UUID!
  $input: CandidateDetailInput!
) {
  updateCandidateDetail(candidate: $candidate, input: $input) {
    response
  }
}
`

export const UPDATE_CAND_NOTES = gql`mutation updateCandidateNotes($candidate: UUID!, $notes: String!) {
  updateCandidateNotes(candidate: $candidate, notes: $notes) {
    response
  }
}
`

export const UPDATE_COMP_PRIMARY = gql`mutation updateCompanyPrimary($input: CompanyPrimaryInfoUpdateInput!) {
  updateCompanyPrimary(input: $input) {
    response
  }
}`

export const UPDATE_CONTACT_PRIMARY = gql`mutation updateContactPrimary($input: ContactPrimaryInfoUpdateInput!){
  updateContactPrimary(input:$input){
    response
  }
}`