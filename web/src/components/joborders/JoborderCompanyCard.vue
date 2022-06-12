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
                <td class="py-2 px-20">{{ data.company.name }}</td>
              </tr>

              <tr>
                <td class="p-2">Department</td>
                <td
                  class="py-2 px-20"
                  v-if="
                    data.company.contacts && data.company.contacts.length > 0
                  "
                >
                  {{ data.company.contacts[0].department }}
                </td>
                <td v-else class="p-2"></td>
              </tr>

              <tr>
                <td class="p-2">Contact</td>
                <td
                  class="px-20"
                  v-if="
                    data.company.contacts && data.company.contacts.length > 0
                  "
                >
                  <div class="pt-2" v-html="formatContacts(data.company.contacts)">
                  </div>
                </td>
                <td v-else class="py-2 px-20"></td>
              </tr>
              <tr>
                <td class="p-2">Address</td>
                <td class="py-2 px-20">
                  {{ formAddress(data.company.address) }}
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
import { formAddress, formatContacts } from "../../utils/helpers";
import Chip from "../widgets/Chip.vue";

export default defineComponent({
  components: { DashboardCardWidget, Chip },
  setup() {},
  props: ["data"],
  methods: {
    formAddress,
    formatContacts,
  },
});
</script>
