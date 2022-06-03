import { gql } from "graphql-tag";

export const JOB_ORDERS = gql` query jobOrders($pageSize: Int!, $page: Int!) {
    jobOrders(pageSize: $pageSize, page: $page){
      page
      objects {
        id
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
        notes
        organization{
            name
        }    
        pipelineWorkflow{
          id
          pipelineSetup{
            id
            title
          }
        }
        jobOrderStatus{
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
  }
  `