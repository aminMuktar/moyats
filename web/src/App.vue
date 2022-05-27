<template>
  <div class="m-5">
    <button v-if="$store.state.core.token" @click="logout">logout</button><br />
    <router-view></router-view>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { logoutMutation } from "./scripts/gqlMutations";

export default defineComponent({
  methods: {
    async logout() {
      await this.$apollo.mutate({
        mutation: logoutMutation,
      });
      this.$store.commit("setToken", false);
      window.location.href = "http://" + window.location.host + "/login";
    },
  },
});
</script>
