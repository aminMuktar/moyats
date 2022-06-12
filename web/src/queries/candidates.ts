import gql from "graphql-tag"


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