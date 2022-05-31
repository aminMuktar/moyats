<template>
  <div class="font-sans gap-y-3 flex flex-col">
    <div>
      <p class="text-3xl pb-5 font-semibold">My Dashboard</p>
    </div>
    <div class="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-3 gap-3">
      <stat-widget v-for="x in 3" :key="x" />
    </div>
    <div class="gap-y-3 flex flex-col">
      <div class="grid md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 gap-3">
        <interviews-widget />
        <followup-widget />
      </div>
      <recent-applications-widget />
      <div class="grid md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 gap-3">
        <workflow-activity />
        <workflow-activity />
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import FollowupWidget from "../../components/widgets/FollowupWidget.vue";
import InterviewsWidget from "../../components/widgets/InterviewsWidget.vue";
import RecentApplicationsWidget from "../../components/widgets/RecentApplicationsWidget.vue";
import StatWidget from "../../components/widgets/StatWidget.vue";
import WorkflowActivity from "../../components/widgets/WorkflowActivity.vue";

export default defineComponent({
  components: {
    InterviewsWidget,
    RecentApplicationsWidget,
    FollowupWidget,
    WorkflowActivity,
    StatWidget,
  },
});
</script>
