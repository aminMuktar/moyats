import gql from "graphql-tag";

export const COMPANIES = gql`
  query companies($pageSize: Int!, $page: Int!) {
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
`;

export const COMPANY = gql`
  query company($cid: String!) {
    company(cid: $cid) {
      id
      name
      website
      companyId
      phones {
        cellNumber
      }
      owner {
        firstName
        lastName
      }
      companyStatus {
        id
        name
        default
        color {
          hex
        }
      }
      address {
        country
        city
      }
      owner{
        firstName
        lastName
      }
      createdAt
      updatedAt
    }
  }
`;


export const SEARCH_COMPANY = gql`query  searchCompany($query: String!){
  searchCompany(query: $query){
    companyId
    name
  }
}`


export const SEARCH_RECRUITER = gql`query  searchRecruiter($query: String!){
  searchRecruiter(query: $query){
    orgMemberId
    user{
      username
      firstName
      lastName
    }
  }
}`


export const ADD_COMPANY = gql`mutation addCompany($input: CompanyInput!){
  addCompany(input:$input) {
    response {
      id
    }
  }
}`

export const COMPANY_CONTACTS = gql`query companyContacts($company: UUID!, $page: Int!, $size: Int!) {
  companyContacts(company: $company, page: $page, pageSize: $size) {
    page
    pages
    objects {
      id
        companyContactId
        firstName
        lastName
        department
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


export const COMAPNY_STATUSES = gql`query {
  companyStatuses{
    id
    name
    color{
      id
      hex
    }
    default
  }
}`