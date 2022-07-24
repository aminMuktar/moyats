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
        <spinner style="margin-top: 40%"></spinner>
      </div>
      <dashboard-card-widget>
        <template v-slot:header>
          <div class="flex justify-between">
            <p class="p-3 font-semibold text-lg">Detail</p>
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
                  <td class="p-2">Start Date</td>
                  <td v-if="editMode">
                    <input
                      v-model="startDate"
                      required
                      class="
                        w-full
                        p-1
                        text-sm
                        border-gray-200 border-2
                        rounded-md
                      "
                      placeholder="Start Date"
                      type="name"
                      id="name"
                    />
                  </td>
                  <td class="py-2 px-2" v-else>
                    {{ data.jobDetail.startDate }}
                  </td>
                </tr>
                <tr>
                  <td class="p-2">Salary</td>
                  <td v-if="editMode">
                    <input
                      v-model="salary"
                      required
                      class="
                        w-full
                        p-1
                        text-sm
                        border-gray-200 border-2
                        rounded-md
                      "
                      placeholder="Salary"
                      type="name"
                      id="name"
                    />
                  </td>
                  <td v-else class="p-2">{{ data.jobDetail.salary }}</td>
                </tr>
                <tr>
                  <td class="p-2">Duration</td>
                  <td v-if="editMode">
                    <input
                      v-model="duration"
                      required
                      class="
                        w-full
                        p-1
                        text-sm
                        border-gray-200 border-2
                        rounded-md
                      "
                      placeholder="Job Duration"
                      type="name"
                      id="name"
                    />
                  </td>

                  <td class="p-2" v-else>{{ data.jobDetail.duration }}</td>
                </tr>
                <tr>
                  <td class="p-2">Maximum Rate</td>
                  <td v-if="editMode">
                    <input
                      v-model="maxRate"
                      required
                      class="
                        w-full
                        p-1
                        text-sm
                        border-gray-200 border-2
                        rounded-md
                      "
                      placeholder="Maximum rate"
                      type="name"
                      id="name"
                    />
                  </td>

                  <td class="p-2" v-else>{{ data.jobDetail.maxRate }}</td>
                </tr>
                <tr>
                  <td class="p-2">Minimum Rate</td>
                  <td v-if="editMode">
                    <input
                      v-model="minRate"
                      required
                      class="
                        w-full
                        p-1
                        text-sm
                        border-gray-200 border-2
                        rounded-md
                      "
                      placeholder="Minimum rate"
                      type="name"
                      id="name"
                    />
                  </td>

                  <td class="p-2" v-else>{{ data.jobDetail.minRate }}</td>
                </tr>
                <tr>
                  <td class="p-2">Type</td>
                  <td v-if="editMode">
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
                      v-model="positionType"
                    >
                      <option value="" disabled selected hidden>
                        Choose position types
                      </option>
                      <option
                        :value="pt.id"
                        v-for="(pt, ix) in positionTypes"
                        :key="ix"
                        v-text="pt.label"
                      ></option>
                    </select>
                  </td>
                  <td class="p-2" v-else>
                    {{ positionType }}
                  </td>
                </tr>
                <tr>
                  <td class="p-2">Category</td>
                  <td v-if="editMode">
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
                      v-model="category"
                    >
                      <option value="" disabled selected hidden>
                        Choose category
                      </option>
                      <option
                        :value="st.id"
                        v-for="(st, ix) in categories"
                        :key="ix"
                        v-text="st.categoryName"
                      ></option>
                    </select>
                  </td>
                  <td class="p-2" v-else>
                    {{ data.jobDetail.category.categoryName }}
                  </td>
                </tr>
                <tr>
                  <td class="p-2">publish</td>
                  <td v-if="editMode">
                    <div class="flex items-center mb-4 mt-2">
                      <input
                        id="checkbox"
                        type="checkbox"
                        v-model="publish"
                        value=""
                        class="
                          w-4
                          h-4
                          text-blue-600
                          bg-gray-100
                          rounded
                          border-gray-300
                          focus:ring-blue-500
                          dark:focus:ring-blue-600 dark:ring-offset-gray-800
                          focus:ring-2
                          dark:bg-gray-700 dark:border-gray-600
                        "
                      />
                      <label
                        for="default-checkbox"
                        class="
                          ml-2
                          text-sm
                          font-medium
                          text-gray-900
                          dark:text-gray-300
                        "
                      ></label>
                    </div>
                  </td>
                  <td class="p-2" v-else>
                    <div>
                      <p v-if="data.jobDetail.publish">Yes</p>
                      <p v-else>No</p>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td class="p-2">Openings</td>
                  <td v-if="editMode">
                    <input
                      v-model="openings"
                      required
                      class="
                        w-full
                        p-1
                        text-sm
                        border-gray-200 border-2
                        rounded-md
                      "
                      placeholder="Openings"
                      type="name"
                      id="name"
                    />
                  </td>
                  <td class="p-2" v-else>{{ data.jobDetail.openings }}</td>
                </tr>
                <tr>
                  <td class="p-2">Remaining Openings</td>
                  <td class="p-2">{{ data.jobDetail.remainingOpenings }}</td>
                </tr>
                <tr>
                  <td class="p-2">Created</td>
                  <td class="p-2">{{ parseDate(data.createdAt) }}</td>
                </tr>
                <tr>
                  <td class="p-2">Update At</td>
                  <td class="p-2">{{ parseDate(data.updatedAt) }}</td>
                </tr>
                <tr>
                  <td class="p-2">Status</td>
                  <td class="p-2">
                    <chip
                      @click="toggleStatusSlider('joborder')"
                      :text="data.jobOrderStatus.statusName"
                      :color="data.jobOrderStatus.color.hex"
                    ></chip>
                  </td>
                </tr>
                <tr>
                  <td class="p-2">Activity</td>
                  <td class="p-2">1 in pipeline (0 submitted)</td>
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
import Chip from "../widgets/Chip.vue";
import { parseDate, toggleStatusSlider } from "../../utils/helpers";
import Spinner from "../Spinner.vue";
import {
  fetchJoborderCategories,
  fetchPositionTypes,
  updateJoborderDetail,
} from "../../services";

export default defineComponent({
  components: { DashboardCardWidget, Chip, Spinner },
  setup() {},
  async created() {
    this.startDate = this.data.jobDetail.startDate;
    this.salary = this.data.jobDetail.salary;
    this.duration = this.data.jobDetail.duration;
    this.maxRate = this.data.jobDetail.maxRate;
    this.minRate = this.data.jobDetail.maxRate;
    this.category = this.data.jobDetail.category.id;
    this.publish = this.data.jobDetail.publish;
    this.openings = this.data.jobDetail.openings;
    this.positionType = this.data.jobDetail.positionType.toLowerCase();
    await this.loadJoborderCategories();
    await this.loadPositionTypes();
    // this.maxRate = this.data.jobDetail.maxRate;
  },
  data: () => ({
    editMode: false,
    startDate: "",
    loading: false,
    salary: "",
    duration: "",
    maxRate: "",
    minRate: "",
    publish: false,
    category: null,
    openings: null,
    positionType: null,
    categories: [] as any,
    positionTypes: [] as any,
  }),
  methods: {
    parseDate,
    async saveChanges() {
      this.editMode = false;
      this.loading = true;
      const { data, errors } = await updateJoborderDetail({
        input: {
          salary: this.salary,
          startDate: this.startDate,
          duration: this.duration,
          maxRate: this.maxRate,
          minRate: this.minRate,
          type: this.positionType,
          category: this.category,
          publish: this.publish,
          openings: this.openings,
        },
        joborder: this.$route.params.jid,
      });
      if (data) {
        this.loading = false;
        this.$emit("updated");
      } else {
        this.loading = false;
      }
    },
    toggleStatusSlider,
    async loadPositionTypes() {
      const { data, errors } = await fetchPositionTypes();
      if (!errors) {
        this.positionTypes = data.positionTypes;
      }
    },
    async loadJoborderCategories() {
      const { data, errors } = await fetchJoborderCategories();
      if (!errors) {
        this.categories = data.categories;
      }
    },
  },
  props: ["data"],
});
</script>
