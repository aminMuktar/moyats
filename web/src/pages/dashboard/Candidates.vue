<template>
  <div class="font-sans gap-y-3 flex flex-col m-5">
    <div>
      <p class="text-3xl pb-5 font-semibold">Candidates</p>
    </div>
    <candidates-layout></candidates-layout>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import ActivitiesLayout from "../../layouts/ActivitiesLayout.vue";
import CandidatesLayout from "../../layouts/CandidatesLayout.vue";

export default defineComponent({
  components: {
    ActivitiesLayout,
    CandidatesLayout,
  },
});
</script>
