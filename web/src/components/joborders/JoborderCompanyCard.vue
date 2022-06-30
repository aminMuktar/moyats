<template>
  <div>
    <div class="flex flex-col mb-5 overflow-hidden bg-white relative">
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
              <button class="border-2 my-2" @click="editMode = true">
                <svg
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
                  <td class="py-2 px-20" v-if="editMode">
                    <div class="flex flex-row py-2" v-if="data.company">
                      <pill
                        :clearable="true"
                        v-if="!editCmp"
                        :text="data.company.name"
                        @clear="editCmp = true"
                      ></pill>
                      <company-selector
                        v-else
                        @itemClicked="companySelected"
                        :showHeader="false"
                      ></company-selector>
                    </div>
                  </td>
                  <td class="py-2 px-20" v-else>
                    {{ data.company.name }}
                  </td>
                </tr>

                <tr>
                  <td class="p-2">Contact</td>
                  <td class="py-2 px-20" v-if="editMode">
                    <pill
                      :clearable="true"
                      v-if="!editCon && data.company.contacts.length"
                      :text="getFullName(data.company.contacts[0])"
                      @clear="editCon = true"
                    ></pill>
                    <company-contact-selector
                      v-else
                      :cid="company"
                      :showHeader="false"
                    ></company-contact-selector>
                  </td>
                  <td v-else class="py-2 px-20">
                    <div
                      v-if="
                        data.company.contacts && data.company.contacts.length
                      "
                    >
                      <div
                        class="pt-2"
                        v-html="getFullName(data.company.contacts[0])"
                      ></div>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </template>
      </dashboard-card-widget>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DashboardCardWidget from "../DashboardCardWidget.vue";
import { formAddress, getFullName, formatContacts } from "../../utils/helpers";
import Chip from "../widgets/Chip.vue";
import CompanySelector from "../selectors/CompanySelector.vue";
import Pill from "../pill.vue";
import CompanyContactSelector from "../selectors/CompanyContactSelector.vue";
import { updateJoborderCompany } from "../../services";
import Spinner from "../Spinner.vue";

export default defineComponent({
  components: {
    DashboardCardWidget,
    Chip,
    CompanySelector,
    Pill,
    CompanyContactSelector,
    Spinner,
  },
  setup() {},
  created() {
    this.company = this.data.company;
  },
  data: () => ({
    editMode: false,
    company: null as any,
    loading: false,
    editCon: false,
    editCmp: false,
  }),
  props: ["data"],
  methods: {
    formAddress,
    getFullName,
    formatContacts,
    companySelected(v) {
      this.company = v;
    },
    async saveChanges() {
      this.editMode = false;
      this.loading = true;
      console.log(this.$route.params);
      const { data, errors } = await updateJoborderCompany({
        company: this.company.companyId,
        joborder: this.$route.params.jid,
      });
      if (data) {
        this.loading = false;
        this.$emit("updated");
      } else {
        this.loading = false;
      }
    },
  },
});
</script>
