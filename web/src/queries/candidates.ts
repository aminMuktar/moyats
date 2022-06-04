import gql from "graphql-tag"


export const CANDIDATES = gql`query candidtes($page: Int!, $pageSize: Int!) {
    candidtes(page: $page, pageSize: $pageSize) {
      objects {
        id
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