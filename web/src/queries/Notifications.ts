import { gql } from "graphql-tag";

export const NOTIFICATION =  gql `query notification{
    notification{
      action
      aFrom{
        email
      }
      seen
      cleared
    }
  }`

export const UPDATENOTIFICATION = gql `
  mutation updateNotification($notificationId: String!, $seen: Boolean!){
    updateNotification(notificationId: $notificationId, seen: $seen){
      response
    }
  }
`

export const UPDATENOTIFICATIONS = gql `
mutation updateNotifications($cleared: Boolean!){
  updateNotifications(cleared: $cleared){
    response
  }
}
`
