<template>
  <div>
    <dashboard-card-widget slot="body">
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">Notes</p>
      </template>
      <template v-slot:body>
        <div>
          <div class="sm:col-span-1 md:flex lg:flex p-2">
            <p>
              JOIN US AS A BUSINESS ANALYST Similar Industry Titles and Key
              Words: Business Analyst, BA, Planner About This Opportunity As a
              Business Analyst, you’ll apply your financial, analytical and
              communication skills to impact the bottom line.
            </p>
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
  components: { DashboardCardWidget },
  setup() {},
});
</script>
