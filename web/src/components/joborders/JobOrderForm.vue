<template>
  <div class="flex w-full flex-col">
    <form class="w-full" ref="form" @submit="saveChanges">
      <div
        class="flex p-2 border-b-2 flex-row w-full fixed gap-2 bg-white"
        style="z-index: 100"
      >
        <button
          type="submit"
          class="
            bg-green-500
            p-2
            text-white
            rounded-md
            tracking-wider
            hover:bg-green-600
          "
        >
          Save Changes
        </button>
        <button
          type="button"
          @click="$emit('close')"
          class="
            border-red-500
            p-2
            border-2
            text-red-700
            rounded-md
            tracking-wider
            hover:bg-red-100
          "
        >
          Cancel
        </button>
      </div>
      <div class="grid grid-cols-1 w-full mt-16">
        <div class="flex col-span-2 w-full p-4">
          <div class="w-52">
            <label class="sr-only" for="name">Title</label>
            <span class="m-1">Title* </span>
          </div>
          <div class="w-full ml-10">
            <input
              v-model="f.title"
              required
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="Title"
              type="name"
              id="name"
            />
          </div>
        </div>
        <div class="flex col-span-2 p-2">
          <div class="w-52">
            <label class="sr-only" for="name">Location</label>
            <span class="m-3 w-full">Location*</span>
          </div>
          <div
            class="
              grid
              xl:grid-cols-3
              lg:grid-cols-3
              md:grid-cols-2
              sm:grid-cols-2
              grid-cols-1
              gap-2
            "
          >
            <div>
              <input
                v-model="f.city"
                required
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="City"
                type="text"
                id="name"
              />
            </div>
            <div>
              <input
                v-model="f.state"
                required
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="State"
                type="text"
                id="name"
              />
            </div>
            <input
              v-model="f.country"
              required
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="Country"
              type="text"
              id="name"
            />
          </div>
        </div>
        <div class="flex col-span-2 w-full p-2">
          <label class="sr-only" for="name">Position Type</label>
          <div class="w-52">
            <span class="m-3">Position Type*</span>
          </div>
          <select
            required
            class="
              w-1/3
              p-2
              text-sm
              border-gray-200 border-2
              rounded-md
              text-gray-600
            "
            placeholder="Title"
            type="selector"
            id="name"
            v-model="f.positionType"
          >
            <option
              :value="px.id"
              v-for="(px, ix) in positionTypes"
              :key="ix"
              v-text="px.label"
            ></option>
          </select>
        </div>
        <div class="flex col-span-2 w-full p-2">
          <label class="sr-only" for="name">Job Order Type</label>
          <div class="w-52">
            <span class="m-3">Job Order Type*</span>
          </div>
          <select
            required
            class="
              w-1/3
              p-2
              text-sm
              border-gray-200 border-2
              rounded-md
              text-gray-600
            "
            placeholder="Title"
            type="selector"
            id="name"
            v-model="f.orderType"
          >
            <option
              :value="px.id"
              v-for="(px, ix) in orderTypes"
              :key="ix"
              v-text="px.typeName"
            ></option>
          </select>
        </div>
        <recruiter-selector
          @itemClicked="recruiterSelected"
        ></recruiter-selector>
        <!-- second section start -->
        <div class="col-span-2 flex p-2">
          <div class="w-52">
            <label class="sr-only" for="name">Start Date</label>
            <span class="m-3">Start Date* </span>
          </div>
          <div>
            <input
              pattern="[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])"
              aria-errormessage="Failed nigga"
              required
              v-model="f.startDate"
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="Start date"
              type="text"
              id="name"
            />
            <small>please use yyyy-mm-dd format Example: 2000-05-05</small>
          </div>
        </div>
        <div class="col-span-2 flex p-2">
          <div class="w-52">
            <label class="sr-only" for="name">Salary</label>
            <span class="m-3">Salary* </span>
          </div>
          <div>
            <input
              v-model="f.salary"
              required
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="Salary"
              type="text"
              id="name"
            />
          </div>
        </div>
        <div class="col-span-2 flex p-2">
          <div class="w-52">
            <label class="sr-only" for="name">Duration</label>
            <span class="m-3">Duration* </span>
          </div>
          <div>
            <input
              v-model="f.duration"
              required
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="Duration"
              type="text"
              id="name"
            />
          </div>
        </div>
        <div class="col-span-2 flex p-2">
          <div class="w-52">
            <label class="sr-only" for="name">Maximum Rate</label>
            <span class="m-3">Maximum Rate </span>
          </div>
          <div>
            <input
              v-model="f.maxRate"
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="Maximum Rate"
              type="text"
              id="name"
            />
          </div>
        </div>
        <div class="col-span-2 flex p-2">
          <div class="w-52">
            <label class="sr-only" for="name">Maximum Rate</label>
            <span class="m-3">Minimum Rate </span>
          </div>
          <div>
            <input
              v-model="f.minRate"
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="Maximum Rate"
              type="text"
              id="name"
            />
          </div>
        </div>
        <div class="col-span-2 flex p-2">
          <div class="w-52">
            <label class="sr-only" for="name">Openinigs</label>
            <span class="m-3">Openinigs* </span>
          </div>
          <div>
            <input
              v-model="f.openings"
              required
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="Maximum Rate"
              type="text"
              id="name"
            />
          </div>
        </div>
        <div class="flex col-span-2 w-full p-2 border-t-2">
          <div class="w-52">
            <span class="m-3">Status* </span>
          </div>
          <select
            required
            class="
              w-1/3
              p-2
              text-sm
              border-gray-200 border-2
              rounded-md
              text-gray-600
            "
            placeholder="Title"
            type="selector"
            id="name"
            v-model="f.orderStatus"
          >
            <option
              :value="st.id"
              v-for="(st, ix) in statuses"
              :key="ix"
              v-text="st.statusName"
            ></option>
          </select>
        </div>
        <!-- <div class="flex col-span-2 w-full p-2" v-if="false">
          <div class="w-52">
            <span class="m-3">Pipeline Workflow* </span>
          </div>
          <select
            required
            class="
              w-1/3
              p-2
              text-sm
              border-gray-200 border-2
              rounded-md
              text-gray-600
            "
            placeholder="Title"
            type="selector"
            id="name"
            v-model="f.pipeline_workflow"
          >
            <option
              :value="st.v"
              v-for="(st, ix) in pipeline_workflows"
              :key="ix"
              v-text="st.l"
            ></option>
          </select>
        </div> -->
        <div class="flex col-span-2 w-full p-2">
          <div class="w-52">
            <span class="m-3">Category* </span>
          </div>
          <select
            required
            class="
              w-1/3
              p-2
              text-sm
              border-gray-200 border-2
              rounded-md
              text-gray-600
            "
            placeholder="Title"
            type="selector"
            id="name"
            v-model="f.category"
          >
            <option
              :value="st.id"
              v-for="(st, ix) in categories"
              :key="ix"
              v-text="st.categoryName"
            ></option>
          </select>
        </div>
        <company-selector
          @cleared="f.company = null"
          @itemClicked="companySelected"
        ></company-selector>
        <company-contact-selector
          @itemClicked="companyContactSelected"
          :cid="f.company"
          v-if="f.company"
        ></company-contact-selector>
        <!-- <div class="flex col-span-2 w-full p-2" v-if="f.company">
          <div class="w-52">
            <span class="m-3">Contact* </span>
          </div>
          <select
            required
            class="
              w-1/3
              p-2
              text-sm
              border-gray-200 border-2
              rounded-md
              text-gray-600
            "
            placeholder="Title"
            type="selector"
            id="name"
            v-model="f.contact"
          >
            <option
              :value="st.v"
              v-for="(st, ix) in statuses"
              :key="ix"
              v-text="st.l"
            ></option>
          </select>
        </div> -->
      </div>

      <div class="col-span-1 flex flex-col p-2 border-t-2 mr-10">
        <label class="p-3" for="">Description</label>
        <textarea
          v-model="f.description"
          id="message"
          rows="4"
          class="
            block
            p-2.5
            w-full
            m-2
            bg-gray-100
            text-sm text-gray-900
            rounded-lg
            border border-gray-300
            focus:ring-blue-500 focus:border-blue-500
          "
          placeholder="Your message..."
        ></textarea>
      </div>
      <div class="col-span-1 flex flex-col p-2 border-t-2 mr-10">
        <label class="p-3" for="">Notes</label>
        <textarea
          v-model="f.notes"
          id="message"
          rows="4"
          class="
            block
            p-2.5
            w-full
            m-2
            bg-gray-100
            text-sm text-gray-900
            rounded-lg
            border border-gray-300
            focus:ring-blue-500 focus:border-blue-500
          "
          placeholder="Add notes here ..."
        ></textarea>
      </div>
      <div class="col-span-1 flex-col flex p-2 border-t-2 mr-10">
        <p class="p-1 pb-5 font-bold text-xl">Applications</p>
        <div class="mt-3">
          <div
            class="flex items-center mb-4 px-2"
            v-for="(app, idx) in applications"
            :key="idx"
          >
            <input
              id="default-checkbox"
              type="checkbox"
              value=""
              class="
                w-4
                h-4
                text-blue-600
                bg-gray-100
                rounded
                border-gray-300
                focus:ring-blue-500 focus:ring-2
              "
              @change="f.application = app"
            />
            <label
              for="default-checkbox"
              class="ml-2 text-sm font-medium text-gray-900"
              >{{ app.description }}</label
            >
          </div>
        </div>
      </div>

      <div class="col-span-2 flex p-2 mb-52"></div>
    </form>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import RecruiterSelector from "../selectors/RecruiterSelector.vue";
import CompanySelector from "../selectors/CompanySelector.vue";
import CompanyContactSelector from "../selectors/CompanyContactSelector.vue";

import {
  addJobOrder,
  fetchApplications,
  fetchJoborderCategories,
  fetchJoborderStatuses,
  fetchJoborderTypes,
  fetchPositionTypes,
} from "../../services";

export default defineComponent({
  components: { RecruiterSelector, CompanySelector, CompanyContactSelector },
  setup() {},
  async created() {
    await this.loadPositionTypes();
    await this.loadJoborderTypes();
    await this.loadJoborderStatus();
    await this.loadJoborderCategories();
    await this.loadApplications();
  },
  data: () => ({
    f: {
      title: "",
      city: "",
      country: "",
      state: "",
      positionType: "",
      recruiter: null as any,
      owner: 10,
      orderType: "",
      startDate: "",
      salary: "",
      duration: "",
      maxRate: "",
      minRate: "",
      category: "",
      orderStatus: "",
      description: "",
      notes: "",
      openings: "",
      application: null as any,
      pipeline_workflow: "",
      publish: false,
      company: null as any,
      contact: null as any,
    },
    companyContacts: [] as any,
    companyPicked: false,
    positionTypes: [] as any,
    selectedVal: null as any,
    statuses: [] as any,
    categories: [] as any,
    applications: [] as any,
    pipeline_workflows: [{ l: "General Application", v: "lkjlk23lkj123lk12l" }],
    orderTypes: [{ l: "Hire", v: "lkjlk23lkj123lk12l" }] as any,
  }),
  methods: {
    handleChosen() {
      console.log("dawg");
    },
    async loadPositionTypes() {
      const { data, errors } = await fetchPositionTypes();
      if (!errors) {
        this.positionTypes = data.positionTypes;
      }
    },
    async loadJoborderTypes() {
      const { data, errors } = await fetchJoborderTypes();
      if (!errors) {
        this.orderTypes = data.joborderTypes;
      }
    },
    async loadJoborderStatus() {
      const { data, errors } = await fetchJoborderStatuses();
      if (!errors) {
        this.statuses = data.joborderStatus;
      }
    },
    async loadJoborderCategories() {
      const { data, errors } = await fetchJoborderCategories();
      if (!errors) {
        this.categories = data.categories;
      }
    },
    async loadApplications() {
      const { data, errors } = await fetchApplications();
      if (!errors) {
        this.applications = data.joborderApplications;
      }
    },
    recruiterSelected(v) {
      this.f.recruiter = v;
    },
    companySelected(v) {
      this.f.company = v;
    },
    companyContactSelected(v) {
      this.f.contact = v;
    },
    async saveChanges(e) {
      e.preventDefault();
      const { data, errors } = await addJobOrder({
        input: {
          notes: this.f.notes,
          description: this.f.description,
          title: this.f.title,
          city: this.f.city,
          state: this.f.state,
          country: this.f.country,
          positionType: this.f.positionType,
          recruiter: "c332fa7e-359b-4945-845b-8b1e7e7d78e3",
          startDate: this.f.startDate,
          salary: this.f.salary,
          maxRate: this.f.maxRate,
          minRate: this.f.minRate,
          duration: this.f.duration,
          openings: this.f.openings,
          orderType: this.f.orderType,
          category: this.f.category,
          status: this.f.orderStatus,
          company: this.f.company.companyId,
          contact: this.f.contact.companyContactId,
          applications: [this.f.application.applicationId],
        },
      });
      if (!errors) {
        console.log(data);
        alert("job order has been added");
        this.$emit("joborderadded");
      }
    },
  },
});
</script>
