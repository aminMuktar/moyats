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
            <p class="p-3 font-semibold text-lg">Primary</p>
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
                  <td class="p-2">Location</td>
                  <td v-if="editMode">
                    <div class="flex flex-row py-2 px-16 gap-2">
                      <input
                        v-model="city"
                        required
                        class="
                          w-full
                          p-1
                          text-sm
                          border-gray-200 border-2
                          rounded-md
                        "
                        placeholder="City"
                        type="name"
                        id="name"
                      />
                      <input
                        v-model="state"
                        required
                        class="
                          w-full
                          p-1
                          text-sm
                          border-gray-200 border-2
                          rounded-md
                        "
                        placeholder="State"
                        type="name"
                        id="name"
                      />
                      <input
                        v-model="country"
                        required
                        class="
                          w-full
                          p-1
                          text-sm
                          border-gray-200 border-2
                          rounded-md
                        "
                        placeholder="Country"
                        type="name"
                        id="name"
                      />
                    </div>
                  </td>
                  <td class="py-3 px-16" v-else>
                    {{ formAddress(data.jobDetail.location) }}
                  </td>
                </tr>
                <tr>
                  <td class="p-2">Recruiter</td>
                  <td v-if="editMode">
                    <div
                      class="flex flex-row py-2 px-16"
                      v-if="data.jobDetail.recruiter"
                    >
                      <pill
                        clearable="true"
                        v-if="!editRec"
                        :text="getFullName(data.jobDetail.recruiter.user)"
                        @clear="editRec = true"
                      ></pill>
                      <recruiter-selector
                        :showLabel="false"
                        v-if="editRec"
                      ></recruiter-selector>
                    </div>
                  </td>
                  <td class="py-3 px-16" v-else>
                    {{ data.owner.firstName }} {{ data.owner.firstName }}
                  </td>
                </tr>
                <tr>
                  <td class="p-2">Owner</td>
                  <div class="flex flex-row py-2 px-16" v-if="editMode">
                    <pill
                      :clearable="false"
                      :text="getFullName(data.owner)"
                      v-if="data.owner"
                    ></pill>

                    <input
                      v-else
                      :value="data.owner.firstName"
                      required
                      class="
                        w-full
                        p-1
                        text-sm
                        border-gray-200 border-2
                        rounded-md
                      "
                      placeholder="Title"
                      type="name"
                      id="name"
                    />
                  </div>
                  <td class="py-3 px-16" v-else>
                    {{ data.owner.firstName }} {{ data.owner.firstName }}
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
import { formAddress, getFullName } from "../../utils/helpers";
import Spinner from "../Spinner.vue";
import { updateJobOrderPrimary } from "../../services";
import Pill from "../pill.vue";
import RecruiterSelector from "../selectors/RecruiterSelector.vue";

export default defineComponent({
  components: { DashboardCardWidget, Spinner, Pill, RecruiterSelector },
  props: ["data"],
  created() {
    this.city = this.data.jobDetail.location.city;
    this.state = this.data.jobDetail.location.country;
    this.country = this.data.jobDetail.location.country;
  },
  data: () => ({
    loading: false,
    editOwner: false,
    editRec: false,
    editMode: false,
    recruiter: null,
    location: "",
    city: "",
    state: "",
    country: "",
  }),
  methods: {
    formAddress,
    getFullName,
    async saveChanges() {
      // TODO: validate inputs here
      this.editMode = false;
      this.loading = true;
      const { data, errors } = await updateJobOrderPrimary({
        input: {
          city: this.city,
          country: this.country,
          recruiter:
            this.recruiter ?? this.data.jobDetail.recruiter.orgMemberId,
        },
        joborder: this.$route.params.jid,
      });
      if (data) {
        this.loading = false;
        this.editOwner = false;
        this.editRec = false;
        this.$emit("updated");
      } else {
        this.loading = true;
      }
    },
  },
});
</script>
