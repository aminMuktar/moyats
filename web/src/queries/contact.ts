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
        companyContactId
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
          companyId
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