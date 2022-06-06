<template>
  <div>
    <dashboard-card-widget slot="body">
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">Company</p>
      </template>
      <template v-slot:body>
        <div>
          <div class="sm:col-span-1 md:flex lg:flex p-2">
            <div class="text-sm w-full lg:w-3/4 xl:w-3/4">
              <div class="flex justify-between my-4 ">
                <p>Company</p>
                <p>Moyats.Inc</p>
              </div>
              <div class="flex justify-between my-4">
                <p>Department</p>
                <div class="text-right">
                    <p>Jaime Landorf</p>
                    <p>catsonedemo+jlandorf@gmail.com</p>
                </div>
              </div>
              <div class="flex justify-between my-4">
                <p>Contact</p>
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
import DashboardCardWidget from "../DashboardCardWidget.vue";

export default defineComponent({
  components: { DashboardCardWidget },
  setup() {},
});
</script>
