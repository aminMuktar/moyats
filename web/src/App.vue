<template>
  <div class="m-5">
    <button v-if="$store.state.core.token" @click="logout">logout</button><br />
    <router-view></router-view>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { LOGOUT } from "./queries/auth";

export default defineComponent({
  methods: {
    async logout() {
      await this.$apollo.mutate({
        mutation: LOGOUT,
      });
      this.$store.commit("setToken", false);
      window.location.href = "http://" + window.location.host + "/login";
    },
  },
});
</script>
