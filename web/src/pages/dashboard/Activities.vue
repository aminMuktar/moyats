<template>
  <div class="font-sans gap-y-3 flex flex-col">
    <div>
      <p class="text-3xl pb-5 font-semibold">Activities</p>
    </div>
    <activities-layout></activities-layout>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import ActivitiesLayout from "../../layouts/ActivitiesLayout.vue";

export default defineComponent({
  components: {
    ActivitiesLayout
},
});
</script>
