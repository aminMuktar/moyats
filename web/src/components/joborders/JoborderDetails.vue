<template>
  <div>
    <dashboard-card-widget slot="body">
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">Detail</p>
      </template>
      <template v-slot:body>
        <div>
          <div class="sm:col-span-1 md:flex lg:flex p-2">
            <div class="text-sm w-full lg:w-3/4 xl:w-3/4">
              <div class="flex justify-between my-4">
                <p>Start Date</p>
                <p>04-13-2022</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Salary</p>
                <p>45000</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Duration</p>
                <p>10 months</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Maximum Rate</p>
                <p>55,000</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Type</p>
                <p>Hire</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Category</p>
                <p>Music Industry</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Publish</p>
                <p>Yes</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Openings</p>
                <p>20</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Remaining Openings</p>
                <p>20</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Tags</p>
                <p></p>
              </div>
              <div class="flex justify-between my-4">
                <p>Created</p>
                <p>04-13-2022</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Updated</p>
                <p>05-26-2022</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Status</p>
                <chip :text="'Active'" :color="'green'"></chip>
              </div>
              <div class="flex justify-between my-4">
                <p>Activity</p>
                <p>1 in pipeline (0 submitted)</p>
              </div>
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
import Chip from "../widgets/Chip.vue";

export default defineComponent({
  components: { DashboardCardWidget, Chip },
  setup() {},
});
</script>
