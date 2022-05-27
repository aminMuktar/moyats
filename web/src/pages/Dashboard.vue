<template>
  <div>Dashboard</div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { accountData } from "./../scripts/gqlQueryies";

export default defineComponent({
  data: () => {
    return {
      email: null,
    };
  },
  methods: {
    async userData() {
      const { data, errors } = await this.$apollo.query({
        query: accountData,
      });
      if (!errors) {
        this.email = data.accountUser.email;
      }
    },
  },
});
</script>
