<template>
  <div>
    <dashboard-card-widget>
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">Detail</p>
      </template>
      <template v-slot:body>
        <div>
          <table class="table-auto">
            <tbody>
              <tr>
                <td class="p-2">Email</td>
                <td class="py-3 px-16">
                  <input
                    v-model="active"
                    id="default-checkbox"
                    type="checkbox"
                    value=""
                    class="
                      w-4
                      h-4
                      text-blue-600
                      bg-gray-100
                      rounded
                      border-gray-300
                      focus:ring-blue-500
                      dark:focus:ring-blue-600 dark:ring-offset-gray-800
                      focus:ring-2
                      dark:bg-gray-700 dark:border-gray-600
                    "
                  />
                </td>
              </tr>
              <tr>
                <td class="p-2">Created</td>
                <td class="py-3 px-16">
                  {{ parseDate(data.createdAt) }}
                </td>
              </tr>
              <tr>
                <td class="p-2">Updated</td>
                <td class="py-3 px-16">
                  {{ parseDate(data.updatedAt) }}
                </td>
              </tr>
              <tr>
                <td class="p-2">Source</td>
                <td class="py-3 px-16">{{ data.source.name }}</td>
              </tr>
              <tr>
                <td class="p-2">Key Skills</td>
                <td class="py-3 px-16">{{ data.keySkills }}</td>
              </tr>
              <tr>
                <td class="p-2">Current Employer</td>
                <td class="py-3 px-16">{{ data.currentEmployeer }}</td>
              </tr>
              <tr>
                <td class="p-2">Date Available</td>
                <td class="py-3 px-16">{{ data.dateAvailable }}</td>
              </tr>
              <tr>
                <td class="p-2">Current Pay</td>
                <td class="py-3 px-16">{{ data.currentPay }}</td>
              </tr>
              <tr>
                <td class="p-2">Desired Pay</td>
                <td class="py-3 px-16">{{ data.desiredPay }}</td>
              </tr>
              <tr>
                <td class="p-2">Activity</td>
                <td class="py-3 px-16">In 1 pipeline / Submitted 1 time</td>
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
import { parseDate } from "../../utils/helpers";
import DashboardCardWidget from "../DashboardCardWidget.vue";

export default defineComponent({
  components: { DashboardCardWidget },
  created() {
    this.active = this.data.active;
  },
  props: ["data"],
  data: () => ({
    editMode: false,
    active: false,
  }),
  methods: { parseDate },
});
</script>
