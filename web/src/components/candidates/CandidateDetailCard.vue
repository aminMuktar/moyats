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
            <p class="p-3 font-semibold text-lg">Detail</p>
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
                  <td class="p-2">Created</td>
                  <td class="py-3 px-16">
                    {{ parseDate(data.createdAt) }}
                  </td>
                </tr>
                <tr>
                  <td class="p-2">Updated</td>
                  <td class="py-3 px-16">
                    {{ parseDate(data.updatedAt) }}
                  </td>
                </tr>
                <tr>
                  <td class="p-2">Source</td>
                  <td v-if="editMode">
                    <div class="flex flex-row py-2 px-11 gap-1">
                      <select
                        required
                        class="
                          p-2
                          text-sm
                          border-gray-200 border-2
                          rounded-md
                          text-gray-600
                        "
                        placeholder="Title"
                        type="selector"
                        id="name"
                        v-model="source"
                      >
                        <option value="" disabled selected hidden>
                          Choose position types
                        </option>
                        <option
                          :value="pt.id"
                          v-for="(pt, ix) in candSources"
                          :key="ix"
                          v-text="pt.name"
                        ></option>
                      </select>
                    </div>
                  </td>

                  <td class="py-3 px-16" v-else>{{ data.source.name }}</td>
                </tr>
                <tr>
                  <td class="p-2">Key Skills</td>
                  <td v-if="editMode">
                    <div class="flex flex-row py-2 px-11 gap-1">
                      <input
                        v-model="keySkills"
                        required
                        class="
                          w-full
                          p-1
                          text-sm
                          border-gray-200 border-2
                          rounded-md
                        "
                        placeholder="Add Key Skills"
                        type="name"
                        id="name"
                      />
                    </div>
                  </td>

                  <td class="py-3 px-16" v-else>{{ data.keySkills }}</td>
                </tr>
                <tr>
                  <td class="p-2">Current Employer</td>
                  <td v-if="editMode">
                    <div class="flex flex-row py-2 px-11 gap-1">
                      <input
                        v-model="currentEmployeer"
                        required
                        class="
                          w-full
                          p-1
                          text-sm
                          border-gray-200 border-2
                          rounded-md
                        "
                        placeholder="Current Employeer"
                        type="name"
                        id="name"
                      />
                    </div>
                  </td>
                  <td class="py-3 px-16" v-else>{{ data.currentEmployeer }}</td>
                </tr>
                <tr>
                  <td class="p-2">Date Available</td>
                  <td v-if="editMode">
                    <div class="flex flex-row py-2 px-11 gap-1">
                      <date-picker
                        class="
                          bg-gray-50
                          border border-gray-300
                          text-gray-900 text-sm
                          rounded-lg
                          focus:ring-blue-500 focus:border-blue-500
                          w-full
                          p-2.5
                        "
                        locale="en,fa"
                        format="YYYY-M-D"
                        v-model="dateAvailable"
                      ></date-picker>
                    </div>
                  </td>
                  <td v-else class="py-3 px-16">{{ data.dateAvailable }}</td>
                </tr>
                <tr>
                  <td class="p-2">Current Pay</td>
                  <td v-if="editMode">
                    <div class="flex flex-row py-2 px-11 gap-1">
                      <input
                        v-model="currentPay"
                        required
                        class="
                          w-full
                          p-1
                          text-sm
                          border-gray-200 border-2
                          rounded-md
                        "
                        placeholder="Current Pay"
                        type="name"
                        id="name"
                      />
                    </div>
                  </td>
                  <td class="py-3 px-16" v-else>{{ data.currentPay }}</td>
                </tr>
                <tr>
                  <td class="p-2">Desired Pay</td>
                  <td v-if="editMode">
                    <div class="flex flex-row py-2 px-11 gap-1">
                      <input
                        v-model="desiredPay"
                        required
                        class="
                          w-full
                          p-1
                          text-sm
                          border-gray-200 border-2
                          rounded-md
                        "
                        placeholder="Desired Pay"
                        type="name"
                        id="name"
                      />
                    </div>
                  </td>
                  <td class="py-3 px-16" v-else>{{ data.desiredPay }}</td>
                </tr>
                <tr>
                  <td class="p-2">Activity</td>
                  <td class="py-3 px-16">In 1 pipeline / Submitted 1 time</td>
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
import {
  candidateSources,
  updateCandidateDetail,
} from "../../services/candidates";
import { parseDate } from "../../utils/helpers";
import DatePicker from "vue3-persian-datetime-picker";
import DashboardCardWidget from "../DashboardCardWidget.vue";
import Spinner from "../Spinner.vue";

export default defineComponent({
  components: { DashboardCardWidget, Spinner, DatePicker },
  created() {
    this.active = this.data.active;
    this.source = this.data.source.id;
    this.keySkills = this.data.keySkills;
    this.currentEmployeer = this.data.currentEmployeer;
    this.dateAvailable = this.data.dateAvailable;
    this.currentPay = this.data.currentPay;
    this.desiredPay = this.data.desiredPay;
    this.fetchCandidateSources();
  },
  props: ["data"],
  data: () => ({
    source: "",
    keySkills: "",
    currentEmployeer: "",
    dateAvailable: "",
    currentPay: "",
    desiredPay: "",
    editMode: false,
    loading: false,
    active: false,
    candSources: [] as any,
  }),
  methods: {
    parseDate,
    async saveChanges() {
      this.editMode = false;
      this.loading = true;
      const { data, errors } = await updateCandidateDetail({
        candidate: this.$route.params.cid,
        input: {
          source: this.source,
          keySkills: this.keySkills,
          currentEmployeer: this.currentEmployeer,
          dateAvailable: this.dateAvailable,
          currentPay: this.currentPay,
          desiredPay: this.desiredPay,
        },
      });
      if (data) {
        this.loading = false;
        this.$emit("updated");
      } else {
        this.loading = false;
      }
    },
    async fetchCandidateSources() {
      const { data } = await candidateSources();
      this.candSources = data.candidateSources;
    },
  },
});
</script>
