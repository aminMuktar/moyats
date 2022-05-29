<template>
  <div>Dashboard</div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { ACCOUNT_DATA } from "../queries/auth";

export default defineComponent({
  data: () => {
    return {
      email: null,
    };
  },
  methods: {
    async userData() {
      const { data, errors } = await this.$apollo.query({
        query: ACCOUNT_DATA,
      });
      if (!errors) {
        this.email = data.accountUser.email;
      }
    },
  },
});
</script>
