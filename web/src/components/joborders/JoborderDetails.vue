<template>
  <div>
    <dashboard-card-widget slot="body">
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">Detail</p>
      </template>
      <template v-slot:body>
        <div>
          <table class="table-auto">
            <tbody>
              <tr>
                <td class="p-2">Start Date</td>
                <td class="py-2 px-2">{{ data.jobDetail.startDate }}</td>
              </tr>
              <tr>
                <td class="p-2">Salary</td>
                <td class="p-2">{{ data.jobDetail.salary }}</td>
              </tr>
              <tr>
                <td class="p-2">Duration</td>
                <td class="p-2">{{ data.jobDetail.duration }}</td>
              </tr>
              <tr>
                <td class="p-2">Maximum Rate</td>
                <td class="p-2">{{ data.jobDetail.maxRate }}</td>
              </tr>
              <tr>
                <td class="p-2">Maximum Rate</td>
                <td class="p-2">{{ data.jobDetail.maxRate }}</td>
              </tr>
              <tr>
                <td class="p-2">Type</td>
                <td class="p-2">Hire</td>
              </tr>
              <tr>
                <td class="p-2">Category</td>
                <td class="p-2">{{ data.jobDetail.category.categoryName }}</td>
              </tr>
              <tr>
                <td class="p-2">publish</td>
                <td class="p-2">
                  <div>
                    <p v-if="data.jobDetail.publish">Yes</p>
                    <p v-else>No</p>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="p-2">Openings</td>
                <td class="p-2">{{ data.jobDetail.openings }}</td>
              </tr>
              <tr>
                <td class="p-2">Remaining Openings</td>
                <td class="p-2">{{ data.jobDetail.remainingOpenings }}</td>
              </tr>
              <tr>
                <td class="p-2">Created</td>
                <td class="p-2">{{ parseDate(data.createdAt) }}</td>
              </tr>
              <tr>
                <td class="p-2">Update At</td>
                <td class="p-2">{{ parseDate(data.updatedAt) }}</td>
              </tr>
              <tr>
                <td class="p-2">Status</td>
                <td class="p-2">
                  <chip
                    :text="data.jobOrderStatus.statusName"
                    :color="data.jobOrderStatus.color.hex"
                  ></chip>
                </td>
              </tr>
              <tr>
                <td class="p-2">Activity</td>
                <td class="p-2">1 in pipeline (0 submitted)</td>
              </tr>
            </tbody>
          </table>
        </div>
      </template>
    </dashboard-card-widget>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DashboardCardWidget from "../DashboardCardWidget.vue";
import Chip from "../widgets/Chip.vue";
import { parseDate } from "../../utils/helpers";

export default defineComponent({
  components: { DashboardCardWidget, Chip },
  setup() {},
  methods: {
    parseDate,
  },
  props: ["data"],
});
</script>
