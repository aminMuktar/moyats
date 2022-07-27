<template>
  <div>
    <workflows-layout></workflows-layout>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import WorkflowsLayout from "../../layouts/WorkflowsLayout.vue";
import { loadPipelineWorkflows } from "../../services";

export default defineComponent({
  components: { WorkflowsLayout },
});
</script>
