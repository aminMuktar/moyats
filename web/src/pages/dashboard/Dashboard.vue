<template>
  <dashboard-layout>
    <router-view />
  </dashboard-layout>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DashboardLayout from "../../layouts/DashboardLayout.vue";

export default defineComponent({
  components: { DashboardLayout },
  setup() {},
});
</script>
