<template>
  <div class="font-sans gap-y-3 flex flex-col m-5">
    <div>
      <p class="text-3xl pb-5 font-semibold">Job Orders</p>
    </div>
    <job-orders-layout></job-orders-layout>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import ActivitiesLayout from "../../layouts/ActivitiesLayout.vue";
import JobOrdersLayout from "../../layouts/JobOrdersLayout.vue";

export default defineComponent({
  components: {
    ActivitiesLayout,
    JobOrdersLayout,
  },
});
</script>
