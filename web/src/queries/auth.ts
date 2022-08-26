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
      firstName
      lastName
      accountType
      blocked
      emailVerified
      source
      address {
        country
        city
        zipCode
      }
      setupComplete
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

export const SOCIAL_AUTH = gql`
  mutation socialAuth($input: SocialRegistrationInput!) {
    socialAuth(input: $input) {
      response {
        firstName
        lastName
        createdAt
      }
    }
  }
`;

export const ACCOUNT_SETUP = gql`
  mutation setupAccount($input: OrgSetupInput!) {
    setupAccount(input: $input) {
      response {
        name
        createdAt
      }
    }
  }
`;

export const ACTIVITIES = gql`
  query activities($page: Int!, $pageSize: Int!) {
    activities(page: $page, pageSize: $pageSize) {
      page
      pages
      hasNext
      hasPrev
      total
      objects {
        id
        activityId
        contentObject
        activityType
        createdAt
        annotation
        contentType {
          id
          appLabel
          model
        }
        user {
          firstName
          lastName
        }
      }
    }
  }
`;

export const ACTIVITY_INFO = gql`
  query activity($activityId: String!) {
    activity(activityId: $activityId) {
      activity {
        id
        activityId
        contentObject
        activityType
        createdAt
        contentType {
          id
          appLabel
          model
        }
        user {
          firstName
          lastName
        }
      }
    }
  }
`;


export const UPDATE_USER = gql `
  mutation updateUser($input: UpdateUserInput!){
    updateUser(input: $input){
      response {
        email
        username
        baseContact {
          cellNumber
          workNumber
          homeNumber
        }
        isActive
        firstName
        lastName
        accountType
        blocked
        emailVerified
        source
        address {
          country
          city
          zipCode
        }
        setupComplete
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
  }
`

export const CHECKUSER_PASSWORD = gql `
  mutation checkUserPassword($password: String!) {
    checkUserPassword(password: $password) {
      response
    }
  }
`

export const CHANGEUSER_PASSWORD = gql `
  mutation changeUserPassword($password: String!){
    changeUserPassword(password: $password){
      response
    }
  }
`
