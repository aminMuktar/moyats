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
                <td class="p-2">Location</td>
                <td class="py-2 px-16">{{ formAddress(data.jobDetail.location) }}</td>
              </tr>
              <tr>
                <td class="p-2">Recruiter</td>
                <td class="py-2 px-16">{{data.owner.firstName}} {{data.owner.firstName}}</td>
              </tr>
              <tr>
                <td class="p-2">Owner</td>
                <td class="py-2 px-16">{{data.owner.firstName}} {{data.owner.firstName}}</td>
              </tr>
              <tr>
                <td class="p-2">Address</td>
                <td class="py-2 px-16">{{ formAddress(data.jobDetail.location) }}</td>
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
