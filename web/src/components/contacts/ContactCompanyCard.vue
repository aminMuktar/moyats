<template>
  <div>
    <dashboard-card-widget slot="body">
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">Company</p>
      </template>
      <template v-slot:body>
        <div>
          <table class="table-auto">
            <tbody>
              <tr>
                <td class="p-2">Company</td>
                <td class="py-2 px-16">{{ data.company.name }}</td>
              </tr>
              <tr>
                <td class="p-2">Department</td>
                <td class="py-2 px-16">{{ data.department }}</td>
              </tr>
              <tr>
                <td class="p-2">Reports To</td>
                <td class="py-2 px-16" v-if="data.contactReportsTo">
                  {{ data.contactReportsTo.firstName }}
                  {{ data.contactReportsTo.lastName }}
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
import { formAddress } from "../../utils/helpers";

export default defineComponent({
  components: { DashboardCardWidget },
  props: ["data"],
  created() {},
  methods: {
    formAddress,
  },
});
</script>