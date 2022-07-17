<template>
  <div class="font-sans gap-y-3 flex flex-col m-5">
    <div>
      <p class="text-3xl pb-5 font-semibold">Applications</p>
    </div>
    <applications-layout></applications-layout>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import ActivitiesLayout from "../../layouts/ActivitiesLayout.vue";
import ApplicationsLayout from "../../layouts/ApplicationsLayout.vue";

export default defineComponent({
  components: {
    ActivitiesLayout,
    ApplicationsLayout,
  },
});
</script>
