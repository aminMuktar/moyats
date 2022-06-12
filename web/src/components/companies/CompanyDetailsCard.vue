<template>
  <div>
    <dashboard-card-widget slot="body">
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">Details</p>
      </template>
      <template v-slot:body>
        <div>
          <table class="table-auto">
            <tbody>
              <tr>
                <td class="p-2">Tags</td>
                <td class="py-2 px-16"></td>
              </tr>
              <tr>
                <td class="p-2">Key Technologies</td>
                <td class="py-2 px-16"></td>
              </tr>
              <tr>
                <td class="p-2">Created</td>
                <td class="py-2 px-16"></td>
              </tr>
              <tr>
                <td class="p-2">Updated</td>
                <td class="py-2 px-16"></td>
              </tr>
              <tr>
                <td class="p-2">Owner</td>
                <td class="py-2 px-16"></td>
              </tr>
              <tr>
                <td class="p-2">Departments</td>
                <td class="py-2 px-16"></td>
              </tr>
              <tr>
                <td class="p-2">Status</td>
                <td class="py-2 px-16">
                    <Chip :text="'active'" :color="'green'"></Chip>
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
import Chip from "../widgets/Chip.vue";

export default defineComponent({
  components: { DashboardCardWidget, Chip },
  props: ["data"],
  created() {},
  methods: {
    formAddress,
  },
});
</script>
