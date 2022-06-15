<template>
  <div>
    <dashboard-card-widget slot="body">
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">Description</p>
      </template>
      <template v-slot:body>
        <div>
          <div class="sm:col-span-1 md:flex lg:flex p-2">
            <div v-html="data.description" class="prose">
            </div>
          </div>
        </div>
      </template>
    </dashboard-card-widget>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DashboardCardWidget from "../DashboardCardWidget.vue";

export default defineComponent({
  props: ["data"],
  components: { DashboardCardWidget },
  setup() {},
});
</script>
