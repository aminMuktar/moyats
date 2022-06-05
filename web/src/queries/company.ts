import gql from "graphql-tag"

export const COMPANIES = gql`query companies($pageSize: Int!, $page: Int!) {
    companies(pageSize: $pageSize, page: $page) {
      page
      pages
      hasNext
      hasPrev
      total
      objects {
        id
        companyId
        name
        companyStatus {
          id
          name
          default
          color {
            hex
          }
        }
        updatedAt
        address {
          country
          city
        }
      }
    }
  }
  `

  