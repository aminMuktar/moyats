<template>
  <div class="font-sans">
    <div>
      <p class="text-3xl pb-5 font-semibold">My Dashboard</p>
    </div>
    <div class="gap-y-3 flex flex-col">
      <div class="grid md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 gap-3">
        <interviews-widget />
        <followup-widget />
      </div>
      <recent-applications-widget />
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import FollowupWidget from "../../components/widgets/FollowupWidget.vue";
import InterviewsWidget from "../../components/widgets/InterviewsWidget.vue";
import RecentApplicationsWidget from "../../components/widgets/RecentApplicationsWidget.vue";

export default defineComponent({
  components: { InterviewsWidget, RecentApplicationsWidget, FollowupWidget },
});
</script>
