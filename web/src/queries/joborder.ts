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
          recruiter{
            id
            orgMemberId
            user{
              userId
              firstName
              lastName
            }
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
    description
    owner{
      username
      firstName
      lastName
    }
    applications{
      header
      applicationId
      description
    }
    jobDetail {
      id
      title
      location {
        country
        city
        zipCode
      }
      recruiter{
        id
        orgMemberId
        user{
          userId
          firstName
          lastName
        }
      }
      positionType
      category {
        id
        categoryName
      }
      publish
      duration
      startDate
      salary
      maxRate
      minRate
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

export const POSITION_TYPES = gql`query {
  positionTypes{
    id
    label
  }
}
`

export const JOB_ORDER_TYPES = gql`query{
  joborderTypes{
    id
    typeName
  }
}`

export const JOB_ORDER_STATUS = gql`query{
  joborderStatus{
    id
    statusName
    description
    color{
      id
      hex
    }
  }
}`

export const JOBORDER_CATEGORIES = gql`query {
  categories{
    id
    categoryName
  }
}`

export const APPLICATIONS = gql`query {
  joborderApplications{
    id
    updatedAt
    applicationId
    description
  }
}`

export const APPLICATION = gql`query joborderApplication($app: String!) {
  joborderApplication(application: $app) {
    id
    applicationId
    description
    header
    updatedAt
    createdAt
  }
}
`

export const APPLICATION_QUESTIONS = gql`query appQuestions($app: String!){
  applicationQuestions(application: $app) {
    id
    questionId
    fieldTitle
    comment
    saveTo
    required
    createdAt
    updatedAt
  }
}
`

export const COMPANY_CONTACTS = gql`query searchCompanyContact($company: UUID!  $query: String!){
    searchCompanyContact(
      company: $company
      query: $query
    ) {
      id
      firstName
      lastName
      companyContactId
    }
  }
`

export const ADD_JOBORDER = gql`mutation addJobOrder($input: JobOrderInputs!) {
  addJoborder(input: $input) {
    response {
      id
    }
  }
}
`

export const UPDATE_JOBORDER_PRIMARY = gql`mutation updateJoborderPrimary($input: JobOrderPrimaryInput!,$joborder: UUID!) {
  updateJoborderPrimary(input: $input, joborder: $joborder) {
    response
  }
}
`
export const UPDATE_JOBORDER_DETAIL = gql`mutation updateJoborderDetails(
  $input: JobOrderDetailInput!
  $joborder: String!
) {
  updateJoborderDetails(input: $input, joborder: $joborder) {
    response
  }
}
`

export const UPDATE_JOBORDER_COMPANY = gql`mutation updateJoborderCompany($company: UUID!, $joborder: UUID!) {
  updateJoborderCompany(company: $company, joborder: $joborder) {
    response
  }
}
`

export const UPDATE_JOBORDER_DESC = gql`mutation updateJoborderDescription($description: String!, $joborder: String!) {
  updateJoborderDescription(description: $description, joborder: $joborder) {
    response
  }
}
`
export const UPDATE_JOBORDER_NOTES = gql`
  mutation updateJoborderNotes($notes: String!, $joborder: String!) {
    updateJoborderNotes(notes: $notes, joborder: $joborder) {
      response
    }
  }
`

export const SAVE_APP_DETAIL_TYPES = gql`query {
  saveApplicationDetailTypes{
    id
    label
  }
}`

export const SAVE_APP_QUESTION = gql`mutation saveApplicationQuestion(
  $app: String!
  $input: ApplicationQuestionInput!
) {
  saveApplicationQuestion(application: $app, input: $input) {
    response
  }
}
`
export const ADD_APPLICATION = gql`mutation addApplication($desc: String!, $header: String!) {
  addApplication(description: $desc, header: $header) {
    response {
      id
      applicationId
      description
      header
    }
  }
}
`
export const UPDATE_JOB_ORDER_STATUS = gql`mutation updateJoborderStatus($joborder: String, $status: Int!) {
  updateJoborderStatus(joborder: $joborder, status: $status) {
    response
  }
}
`

export const JOBORDER_PIPELINES = gql`query joborderApplicantPipeline(
  $joborder: String!
  $page: Int!
  $pageSize: Int!
) {
  joborderApplicantPipeline(
    joborder: $joborder
    page: $page
    pageSize: $pageSize
  ) {
    page
    pages
    total
    objects {
      id
      status{
        id
        statusName
        color{
          id
          hex
        }
      }
      createdAt
      updatedAt
      candidate {
        id
        candidateId
        source{
          id
          name
          description
        }
        candidateId
        address{
          country
          city
        }
        candidateProfile {
          firstName
          lastName
          email
        }
      }
    }
  }
}
`