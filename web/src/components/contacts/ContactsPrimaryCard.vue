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
                <td class="p-2">Name</td>
                <td class="py-2 px-16">
                  {{ data.firstName }} {{ data.lastName }}
                </td>
              </tr>
              <tr>
                <td class="p-2">Phones</td>
                <td class="py-2 px-16">
                  <!-- add other multple cell numbers here type by type -->
                  <div class="flex flex-row">
                    <span>
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="h-5 w-5"
                        viewBox="0 0 20 20"
                        fill="currentColor"
                      >
                        <path
                          fill-rule="evenodd"
                          d="M7 2a2 2 0 00-2 2v12a2 2 0 002 2h6a2 2 0 002-2V4a2 2 0 00-2-2H7zm3 14a1 1 0 100-2 1 1 0 000 2z"
                          clip-rule="evenodd"
                        />
                      </svg>
                    </span>
                    {{ data.phones.cellNumber }}
                  </div>
                </td>
              </tr>
              <tr>
                <td class="p-2">Address</td>
                <td class="py-2 px-16">{{ formAddress(data.address)}}</td>
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
