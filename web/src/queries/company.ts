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
        owner {
          firstName
          lastName
        }
        organization {
          name
          orgType
          description
          subdomain
        }
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
<<<<<<< Updated upstream
`;

<<<<<<< HEAD

=======
export const COMPANY = gql`
  query company($cid: String!) {
    company(cid: $cid) {
=======
  `
>>>>>>> 5b0d8bbc18897dae4550c5644dc058628aaf9c31

export const COMPANY = gql`query company($cid: String!) {
  company(cid: $cid) {
    id
    name
    website
    phones{
      cellNumber
    }
    owner{
      firstName
      lastName
    }
    companyStatus {
>>>>>>> Stashed changes
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
    }
    owner{
      firstName
      lastName
    }
    createdAt
    updatedAt
  }
`;
