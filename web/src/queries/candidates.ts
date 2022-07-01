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