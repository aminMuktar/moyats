import { gql } from "graphql-tag";

export const loginMutation = gql`
  mutation baseUserLogin($username: String!, $password: String!) {
    baseUserLogin(username: $username, password: $password) {
      payload
      token
    }
  }
`;

export const logoutMutation = gql`
  mutation {
    baseUserLogout {
      deleted
    }
  }
`;
