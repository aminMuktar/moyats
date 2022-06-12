<template>
  <div>
    <dashboard-card-widget slot="body">
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">Description</p>
      </template>
      <template v-slot:body>
        <div>
          <div class="sm:col-span-1 md:flex lg:flex p-2">
            <p>
              JOIN US AS A BUSINESS ANALYST Similar Industry Titles and Key
              Words: Business Analyst, BA, Planner About This Opportunity As a
              Business Analyst, you’ll apply your financial, analytical and
              communication skills to impact the bottom line. You’ll negotiate
              and maintain business relationships with the largest vendors in
              the industry and benchmark the competition to stay on top of the
              latest trends in merchandising and how they may apply at
              QuattroTek. You will leverage professional partnerships with
              buyers and vendors to achieve optimal inventory levels and drive
              sales. Help bring our guests what they want, when they want it,
              online or at whichever QuattroTek store they shop. As a Business
              Analyst, you’ll take the lead as you…
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
