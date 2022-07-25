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

export const CONTACT = gql`query contact($cid: String!){
  contact(cid: $cid) {
    id
    companyContactId
    reachable
    phones {
      cellNumber
    }
    address{
      city
      country
    }
    notes
    contactReportsTo{
      companyContactId
      firstName
      lastName
    }
    department
    firstName
    lastName
    email
    status {
      name
      color {
        hex
      }
    }
    owner{
      firstName
      lastName
    }
    company {
      id
      name
      companyId
      companyStatus {
        name
        color {
          hex
        }
      }
    }
    createdAt
    updatedAt
  }
}
`


export const ADD_CONTACT = gql`mutation addContact($input: CompanyContactInput!) {
  addContact(input: $input) {
    ok
    contact {
      id
      companyContactId
      lastName
    }
  }
}`


export const UPDATE_CONTACT_DETAIL = gql`mutation updateContactCompany(
  $company: String
  $contact: String
  $dep: String
) {
  updateContactCompany(company: $company, contact: $contact, department: $dep) {
    response
  }
}
`

export const UPDATE_CONTACT_NOTES = gql`mutation updateContactNote($contact: String!, $note: String!) {
  updateContactNote(contact: $contact, note: $note) {
    response
  }
}
`

export const CONTACT_STATUSES = gql`query {
  contactStatuses {
    id
    name
    color{
      hex
    }
    default
    initial
  }
}
`

export const UPDATE_CONTACT_STATUS = gql`mutation updateContactStatus($contact: String, $status: Int!) {
  updateContactStatus(contact: $contact, status: $status) {
    response
  }
}
`

export const UPDATE_COMPANY_STATUS = gql`mutation updateCompanyStatus($company: String, $status: Int!) {  
  updateCompanyStatus(company: $company, status: $status) {
    response
  }
}`