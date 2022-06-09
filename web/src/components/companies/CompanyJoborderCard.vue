<template>
  <div>
    <dashboard-card-widget slot="body">
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">Job Orders</p>
      </template>
      <template v-slot:body>
        <div>
          <div>
            <div class="w-1/4 text-sm">
              <table class="text-sm text-left">
                <thead class="text-xs uppercase bg-gray-50">
                  <tr></tr>
                </thead>
                <tbody>
                  <tr class="bg-white border-b" v-for="x in 2" :key="x">
                    <th
                      scope="row"
                      class="
                        px-6
                        py-4
                        font-medium
                        text-gray-900
                        whitespace-nowrap
                      "
                    >
                      <div>
                        <span class="text-md font-bold">
                          System Administrator - </span
                        >Seattle, Washington
                      </div>
                      <!-- candidates in pipelines -> candidates submitted -> candidates interviewing -> candidates placed -->
                      <span class="font-bold">2 -> 0 -> 0 -> 1</span>
                    </th>
                    <td class="px-6 py-4">
                      <Chip
                        :text="'filled'"
                        :color="'rgb(200, 105, 80)'"
                      ></Chip>
                    </td>
                  </tr>
                </tbody>
              </table>
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
