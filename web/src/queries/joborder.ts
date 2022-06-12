import { gql } from "graphql-tag";

export const JOB_ORDERS = gql` query jobOrders($pageSize: Int!, $page: Int!) {
    jobOrders(pageSize: $pageSize, page: $page){
      page
      pages
      hasNext
      hasPrev
      total
      objects {
        id
        joborderId
        notes
        description
        jobDetail {
          id
          title
          location {
            country
            city
            zipCode
          }
          positionType
          category {
            categoryName
          }
          startDate
          salary
          maxRate
          openings
          remainingOpenings
        }
        company{
          id
          contacts{
            id
            firstName
            lastName
            email
            phones{
              cellNumber
            }
          }
          companyId
          companyStatus{
            name
            color{
              hex
            }
          }
        }
        notes
        organization{
            name
        }    
        pipelineWorkflow{
          id
          title
          pipelineSetups{
            id
          }
        }
        jobOrderStatus{
          id
          statusName
          color{
            hex
          }  
        }
        updatedAt
        createdAt
      }
    }
  }
  `

export const JOB_ORDER = gql`query jobOrder($id: String!){
  jobOrder(id: $id) {
    id
    joborderId
    notes
    description
    owner{
      username
      firstName
      lastName
    }
    jobDetail {
      id
      title
      location {
        country
        city
        zipCode
      }
      positionType
      category {
        categoryName
      }
      publish
      duration
      startDate
      salary
      maxRate
      openings
      remainingOpenings
    }
    company{
      name
      address{
        country
        city
        zipCode        
      }
      contacts{
        firstName
        lastName
        email
        department
        phones{
          cellNumber
        }
      }
      companyId
      companyStatus{
        name
        color{
          hex
        }
      }
    }
    organization {
      name
    }
    notes
    pipelineWorkflow {
      id
      title
      pipelineSetups {
        id
      }
    }
    jobOrderStatus {
      id
      statusName
      color {
        hex
      }
    }
    updatedAt
    createdAt
  }
}
`