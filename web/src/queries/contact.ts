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