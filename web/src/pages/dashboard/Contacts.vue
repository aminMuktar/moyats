<template>
  <div class="font-sans gap-y-3 flex flex-col">
    <div>
      <p class="text-3xl pb-5 font-semibold">Contacts</p>
    </div>
    <companies-layout></companies-layout>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import ActivitiesLayout from "../../layouts/ActivitiesLayout.vue";
import CompaniesLayout from "../../layouts/CompaniesLayout.vue";

export default defineComponent({
  components: {
    ActivitiesLayout,
    CompaniesLayout,
  },
});
</script>
