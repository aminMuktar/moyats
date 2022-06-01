<template>
  <activities-layout>
    <router-view></router-view>
  </activities-layout>
</template>
<script lang="ts">
import { defineComponent } from "@vue/runtime-core";
import ActivitiesLayout from "../../layouts/ActivitiesLayout.vue";
export default defineComponent({
  components: {
    ActivitiesLayout,
  },
});
</script>
