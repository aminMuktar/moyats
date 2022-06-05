import gql from "graphql-tag"

export const CONTACTS = gql`query contacts($pageSize: Int!, $page: Int!) {
    contacts(pageSize: $pageSize, page: $page) {
      page
      pages
      hasNext
      hasPrev
      total
      objects {
        id
        firstName
        lastName
        reachable
        phones{
          cellNumber
        }
        status{
          name
          color{
            hex
          }
        }  
        company{
          id
          name
          companyStatus{
            name
            color{
              hex
            }
          }
        }
        email
        updatedAt
      }
    }
  }
  `