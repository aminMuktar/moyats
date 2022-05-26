<template>
  <div
    class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8"
  >
    <button @click="login">login</button><br />
    <button @click="logout">logout</button><br />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { loginMutation, logoutMutation } from "./scripts/gqlMutations";

export default defineComponent({
  data: () => {
    return {
      auth: false,
      username: null,
      password: null,
    };
  },
  created() {
    // console.log(this.$store.state.token);
  },
  methods: {
    async login() {
      const { data, errors } = await this.$apollo.mutate({
        mutation: loginMutation,
        variables: {
          username: this.username,
          password: this.password,
        },
      });

      if (!errors) {
        this.$store.commit("setToken", !!data.baseUserLogin.token);
        console.log(!!this.$store.state.token);
      }
    },
    async logout() {
      await this.$apollo.mutate({
        mutation: logoutMutation,
      });
    },
  },
});
</script>
