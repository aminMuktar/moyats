<template>
  <div
    class="min-h-full items-center justify-center py-12 px-4 sm:px-6 lg:px-8"
  >
    <!-- <p>State --- {{ $store.state.core.token }} ---</p>
    <p class="pt-12">Non-persisted State: --- {{ $store.state.core.test }} --- </p> -->
    <form action="" method="post" v-if="!$store.state.core.token">
      email: <input type="text" v-model="username" /> <br /><br />
      password:<input type="password" v-model="password" /><br /><br />
      <button @click="login">login</button><br />
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { loginMutation, logoutMutation } from "../scripts/gqlMutations";

export default defineComponent({
  data() {
    return {
      auth: false,
      username: "",
      password: "",
    };
  },
  methods: {
    async login(e: any) {
      e.preventDefault();
      const { data, errors } = await this.$apollo.mutate({
        mutation: loginMutation,
        variables: {
          username: this.username,
          password: this.password,
        },
      });

      if (!errors) {
        this.$store.commit("setToken", !!data.baseUserLogin.token);
        console.log(this.$store.state.core.token);
        console.log(window.location.host);
        window.location.href = "http://" + window.location.host + "/dashboard";
      } else {
        console.log("errorrrr", errors);
      }
    },
  },
});
</script>
