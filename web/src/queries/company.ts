import gql from "graphql-tag"

export const COMPANIES = gql`query companies($pageSize: Int!, $page: Int!) {
    companies(pageSize: $pageSize, page: $page) {
      objects {
        id
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

  