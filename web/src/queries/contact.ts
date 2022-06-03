import gql from "graphql-tag"

export const CONTACTS = gql`query contacts($pageSize: Int!, $page: Int!) {
    contacts(pageSize: $pageSize, page: $page) {
      objects {
        id
        firstName
        lastName
        reachable
        phones{
          cellNumber
        }
        company{
          id
          name
        }
        email
        updatedAt
      }
    }
  }
  `