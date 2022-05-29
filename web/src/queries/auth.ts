import { gql } from "graphql-tag";

// rename queries and mutations as cosntant variables with all caps
// avoid using mutation or query in the variable just keep it simple

export const LOGIN_USER = gql`
  mutation baseUserLogin($username: String!, $password: String!) {
    baseUserLogin(username: $username, password: $password) {
      payload
      token
    }
  }
`;

export const LOGOUT = gql`
  mutation {
    baseUserLogout {
      deleted
    }
  }
`;

export const ACCOUNT_DATA = gql`
  query {
    accountUser {
      email
      username
      baseContact {
        cellNumber
        workNumber
        homeNumber
      }
      isActive
      userProfile {
        profilePic
        firstName
        middleName
        lastName
      }
      accountType
      blocked
      emailVerified
      source
      address {
        country
        city
        zipCode
      }
      signiture
      notificationSetting {
        setting
        value
      }
      timezone
      dateFormat
      createdAt
      updatedAt
    }
  }
`;

export const SOCIAL_AUTH = gql`mutation socialAuth($input:SocialRegistrationInput!){
  socialAuth(input:$input){
    response{
      firstName
      lastName
      createdAt
    }
  }
}`
