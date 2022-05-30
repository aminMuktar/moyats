<template>
  <router-view></router-view>
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
