<template>
  <dashboard-layout>
    <router-view />
  </dashboard-layout>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DashboardLayout from "../../layouts/DashboardLayout.vue";
import * as q from "../../queries/auth";

export default defineComponent({
  components: { DashboardLayout },
  setup() {},
  async created() {
    // await this.saveUserData()
  },
  methods: {
    async saveUserData() {
      const {
        data: { accountUser },
      } = await this.$apollo.query({
        query: q.ACCOUNT_DATA,
      });
      await this.$store.commit("saveUdata", accountUser);
    },
  },
});
</script>
