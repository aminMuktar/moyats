import { gql } from "graphql-tag";

export const accountData = gql`
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
