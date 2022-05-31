<template>
  <dashboard-card-widget :height="40">
    <template v-slot:header>
      <p class="p-3 font-semibold text-lg">Recent applications</p>
    </template>
    <template v-slot:body>
      <p class="pt-10 text-center">you don't have any applications</p>
    </template>
  </dashboard-card-widget>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DashboardCardWidget from "../DashboardCardWidget.vue";

export default defineComponent({
  components: { DashboardCardWidget },
  setup() {},
});
</script>
