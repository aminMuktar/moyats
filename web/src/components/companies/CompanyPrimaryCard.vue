<template>
  <div>
    <dashboard-card-widget slot="body">
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">Primary</p>
      </template>
      <template v-slot:body>
        <div>
          <table class="table-auto">
            <tbody>
              <tr>
                <td class="p-2">Address</td>
                <td class="py-2 px-16">{{ formAddress(data.address) }}</td>
              </tr>
              <tr>
                <td class="p-2">Phones</td>
                <td class="py-2 px-16" v-if="data.phones">
                  {{ data.phones.cellNumber }}
                </td>
              </tr>
              <tr>
                <td class="p-2">Website</td>
                <td class="py-2 px-16 text-blue-500" v-if="data.website">
                  <a target="_blank" :href="data.website">{{ data.website }}</a>
                </td>
              </tr>
              <tr>
                <td class="p-2">Social Media</td>
                <td class="py-2 px-16"></td>
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
