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
                <p>Active</p>
                <p>No</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Created</p>
                <p>05-05-2022</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Updated</p>
                <p>05-05-2022</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Source</p>
                <p>LinkedIn</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Key Skills</p>
                <p>Debugging, Testing</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Current Employer</p>
                <p>Amen Abe</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Date Available</p>
                <p>asdffffffadsfasdfasdf</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Current Employer</p>
                <p>Amen Abe</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Current Pay</p>
                <p>3,000 ETB</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Desired Pay</p>
                <p>13,000 ETB</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Activity</p>
                <p>In 1 pipeline / Submitted 1 time</p>
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
import DashboardCardWidget from "./DashboardCardWidget.vue";

export default defineComponent({
  components: { DashboardCardWidget },
  setup() {},
});
</script>
