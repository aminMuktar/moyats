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
    userId
    firstName
    lastName
  }
}`