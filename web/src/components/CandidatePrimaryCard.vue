<template>
  <div>
    <dashboard-card-widget slot="body">
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">Primary</p>
      </template>
      <template v-slot:body>
        <div>
          <div class="sm:col-span-1 md:flex lg:flex p-2">
            <div class="text-sm w-full lg:w-3/4 xl:w-3/4">
              <div class="flex justify-between my-4 ">
                <p>Email</p>
                <p>bdere12345@gmail.com</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Phones</p>
                <p>0911359586</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Social Media</p>
                <p></p>
              </div>
              <div class="flex justify-between my-4">
                <p>Address</p>
                <p>Addis Ababa, Ethiopia, 1000</p>
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
