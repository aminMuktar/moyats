<template>
  <div>
    <dashboard-card-widget>
      <template v-slot:header>
        <div class="flex justify-between">
          <p class="p-3 font-semibold text-lg">Details</p>
        </div>
      </template>
      <template v-slot:body>
        <div>
          <table class="table-auto">
            <tbody>
              <tr>
                <td class="p-2">Created</td>
                <td class="py-2 px-16">{{ parseDate(data.createdAt) }}</td>
              </tr>
              <tr>
                <td class="p-2">Updated</td>
                <td class="py-2 px-16">{{ parseDate(data.updatedAt) }}</td>
              </tr>
              <tr>
                <td class="p-2">Owner</td>
                <td class="py-2 px-16">
                  {{ data.owner.firstName }} {{ data.owner.lastName }}
                </td>
              </tr>
              <tr>
                <td class="p-2">Status</td>
                <td class="py-2 px-16">
                  <Chip
                    @click="toggleStatusSlider('company', data.companyId)"
                    :text="data.companyStatus.name"
                    :color="data.companyStatus.color.hex"
                  ></Chip>
                </td>
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
import {
  formAddress,
  parseDate,
  toggleStatusSlider,
} from "../../utils/helpers";
import Chip from "../widgets/Chip.vue";

export default defineComponent({
  components: { DashboardCardWidget, Chip },
  props: ["data"],
  created() {},
  data: () => ({
    editMode: false,
  }),
  methods: {
    parseDate,
    formAddress,
    toggleStatusSlider,
  },
});
</script>
