<template>
  <div class="m-5">
    <p class="text-5xl">Ameno</p>
    <button class="p-4 mt-10 bg-blue-200" @click="login">Login User</button>
    <button class="p-4 mt-10 bg-blue-200" @click="logout">Logout</button>
  </div>
</template>
<script lang="ts">
import gql from "graphql-tag";
import { defineComponent } from "vue";

export default defineComponent({
  methods: {
    async logout() {
      await this.$apollo.mutate({
        mutation: gql`
          mutation {
            baseUserLogout {
              deleted
            }
          }
        `,
      });
    },
    async login() {
      const { data } = await this.$apollo.mutate({
        mutation: gql`
          mutation {
            baseUserLogin(
              username: "jack12345@gmail.com"
              password: "#Hallelujah"
            ) {
              payload
              token
            }
          }
        `,
      });
      console.warn(data, "response after login");
    },
  },
  created() {
    this.$apollo.mutate({
      mutation: gql`
        query {
          accountUser {
            email
            emailVerified
            lastLogin
            accountType
            userProfile {
              profilePic
              firstName
              lastName
              middleName
            }
            baseContact {
              cellNumber
              homeNumber
              workNumber
            }
            address {
              city
              country
              zipCode
            }
            source
            timezone
            dateFormat
          }
        }
      `,
    });
  },
  // setup() {

  // },
});
</script>
