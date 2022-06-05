import gql from "graphql-tag"


export const CANDIDATES = gql`query candidtes($page: Int!, $pageSize: Int!) {
  candidtes(page: $page, pageSize: $pageSize) {
    objects {
      candidateId
      latestJoborder{
        id
        jobDetail{
          title
        }
        company{
          id
          name
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