<template>
  <div>
    <div
      v-if="loading"
      class="
        absolute
        bg-white bg-opacity-60
        z-10
        h-full
        w-full
        flex
        items-start
        justify-center
      "
    >
      <spinner style="margin-top: 15%"></spinner>
    </div>
    <dashboard-card-widget>
      <template v-slot:header>
        <div class="flex justify-between">
          <p class="p-3 font-semibold text-lg">Company</p>
          <div class="flex flex-row justify-end gap-2 mx-2">
            <button class="border-2 my-2" @click="editMode = !editMode">
              <svg
                v-if="editMode"
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6 m-1"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
              <svg
                v-else
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6 m-1"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"
                />
              </svg>
            </button>
            <button
              class="p-2 border-2 my-2 bg-green-400 border-green-200"
              @click="saveChanges"
              v-if="editMode"
            >
              save
            </button>
          </div>
        </div>
      </template>

      <template v-slot:body>
        <div>
          <table class="table-auto">
            <tbody>
              <tr>
                <td class="p-2">Company</td>
                <td class="p-4" v-if="editMode">
                  <pill
                    :clearable="true"
                    v-if="!editCmp"
                    :text="data.company.name"
                    @clear="editCmp = true"
                  ></pill>
                  <company-selector
                    v-else
                    :showHeader="false"
                    @cleared="company = null"
                    @itemClicked="companySelected"
                  ></company-selector>
                </td>
                <td class="py-2 px-16" v-else>
                  <div v-if="data.company">
                    {{ data.company.name }}
                  </div>
                </td>
              </tr>
              <tr>
                <td class="p-2">Department</td>
                <!-- td with department input -->
                <td class="px-4" v-if="editMode">
                  <input
                    v-model="department"
                    required
                    class="
                      w-full
                      p-1
                      text-sm
                      border-gray-200 border-2
                      rounded-md
                    "
                  />
                </td>
                <td v-else class="py-2 px-16">{{ data.department }}</td>
              </tr>
              <tr class="hidden">
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
import CompanySelector from "../selectors/CompanySelector.vue";
import Pill from "../pill.vue";
import { updateContactDetails } from "../../services";
import Spinner from "../Spinner.vue";

export default defineComponent({
  components: { DashboardCardWidget, CompanySelector, Pill, Spinner },
  props: ["data"],
  created() {
    this.department = this.data.department;
    this.company = this.data.company;
    console.log(this.company);
  },
  data: () => ({
    company: null as any,
    loading: false,
    department: "",
    editMode: false,
    editCmp: false,
  }),
  methods: {
    formAddress,
    companySelected(v) {
      this.company = v;
      console.log(this.company,"selected")
    },
    async saveChanges(e) {
      e.preventDefault();
      this.loading = true;
      const { data } = await updateContactDetails({
        company: this.company.companyId,
        dep: this.department,
        contact: this.$route.params.cid,
      });
      if (data) {
        this.loading = false;
        this.$emit("updated");
        this.editMode = false;
      } else {
        this.loading = false;
        this.editMode = false;
      }
    },
  },
});
</script>
