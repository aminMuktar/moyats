<template>
  <div>
    <dashboard-card-widget>
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">Primary</p>
      </template>
      <template v-slot:body>
        <div>
          <table class="table-auto">
            <tbody>
              <tr>
                <td class="p-2">Email</td>
                <td class="py-3 px-16">
                  {{ data.candidateProfile.email }}
                </td>
              </tr>
              <tr>
                <td class="p-2">Phones</td>
                <td class="py-3 px-16">
                  {{ data.phones.cellNumber }}
                </td>
              </tr>
              <tr>
                <td class="p-2">Social Media</td>
                <td class="py-3 px-16"></td>
              </tr>
              <tr>
                <td class="p-2">Address</td>
                <td class="py-3 px-16">{{ formAddress(data.address) }}</td>
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
import { formAddress } from "../../utils/helpers";
import DashboardCardWidget from "../DashboardCardWidget.vue";

export default defineComponent({
  components: { DashboardCardWidget },
  props: ["data"],
  data: () => ({
    editMode: false,
  }),
  methods: {
    formAddress,
  },
});
</script>
