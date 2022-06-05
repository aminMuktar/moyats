<template>
  <div>
    <dashboard-card-widget slot="body">
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">Activity Feed</p>
      </template>
      <template v-slot:body>
        <div>
          <div class="sm:col-span-1 md:flex lg:flex p-2">
            <div class="w-1/4 ml-4 text-sm"></div>
          </div>
          <p class="text-center py-5">No Activities Yet</p>
        </div>
      </template>
    </dashboard-card-widget>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DashboardCardWidget from "./DashboardCardWidget.vue";

export default defineComponent({
  components: { DashboardCardWidget },
  setup() {},
});
</script>
