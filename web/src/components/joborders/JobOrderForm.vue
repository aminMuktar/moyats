<template>
  <div class="flex w-full flex-col">
    <div class="flex p-2 border-b-2 flex-row w-full fixed gap-2 bg-white">
      <button
        class="
          bg-green-500
          p-2
          text-white
          rounded-md
          tracking-wider
          hover:bg-green-600
        "
        @click="saveChanges"
      >
        Save Changes
      </button>
      <button
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
    <form class="w-full mt-16" ref="form">
      <div class="grid grid-cols-1 w-full">
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
          <div class="flex gap-2">
            <input
              v-model="f.city"
              required
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="City"
              type="text"
              id="name"
            />
            <input
              v-model="f.state"
              required
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="State"
              type="text"
              id="name"
            />
            <input
              v-model="f.zipcode"
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
              :value="px.v"
              v-for="(px, ix) in positionTypes"
              :key="ix"
              v-text="px.l"
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
              :value="px.v"
              v-for="(px, ix) in orderTypes"
              :key="ix"
              v-text="px.l"
            ></option>
          </select>
        </div>
        <div class="flex col-span-2 w-full p-2">
          <div class="w-52">
            <span class="m-3">Recruiter* </span>
          </div>
          <div>
            <div class="bg-blue-300 rounded-md flex left-0">
              <a
                href=""
                class="
                  h-full
                  w-full
                  flex
                  justify-center
                  items-center
                  pl-4
                  pr-4
                  text-gray-600
                "
              >
                Someone</a
              >
            </div>
          </div>
        </div>
        <div class="flex col-span-2 w-full p-2">
          <div class="w-52">
            <label class="sr-only" for="name">Owner</label>
            <span class="m-3">Owner* </span>
          </div>
          <div>
            <div class="bg-blue-300 rounded-md">
              <a
                href=""
                class="
                  h-full
                  w-full
                  flex
                  justify-center
                  items-center
                  pl-4
                  pr-4
                  text-gray-600
                "
              >
                Someone</a
              >
            </div>
          </div>
        </div>
        <!-- second section start -->
        <div class="col-span-2 flex p-2">
          <div class="w-52">
            <label class="sr-only" for="name">Start Date</label>
            <span class="m-3">Start Date* </span>
          </div>
          <div>
            <input
              required
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="Start date"
              type="text"
              id="name"
            />
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
            <span class="m-3">Maximum Rate* </span>
          </div>
          <div>
            <input
              required
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
            <span class="m-3">Minimum Rate* </span>
          </div>
          <div>
            <input
              v-model="f.minRate"
              required
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
            v-model="f.positionType"
          >
            <option
              :value="st.v"
              v-for="(st, ix) in statuses"
              :key="ix"
              v-text="st.l"
            ></option>
          </select>
        </div>
        <div class="flex col-span-2 w-full p-2">
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
        </div>
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
            v-model="f.positionType"
          >
            <option
              :value="st.v"
              v-for="(st, ix) in statuses"
              :key="ix"
              v-text="st.l"
            ></option>
          </select>
        </div>
        <div class="flex col-span-2 w-full p-2 border-t-2">
          <div class="w-52">
            <span class="m-3">Company* </span>
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
              :value="st.v"
              v-for="(st, ix) in statuses"
              :key="ix"
              v-text="st.l"
            ></option>
          </select>
        </div>
        <div class="flex col-span-2 w-full p-2">
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
            v-model="f.positionType"
          >
            <option
              :value="st.v"
              v-for="(st, ix) in statuses"
              :key="ix"
              v-text="st.l"
            ></option>
          </select>
        </div>
      </div>

      <div class="col-span-1 flex flex-col p-2 border-t-2 mr-10">
        <label class="p-3" for="">Description</label>
        <textarea
          id="message"
          rows="4"
          class="
            block
            p-2.5
            w-full
            m-2 bg-gray-100
            text-sm text-gray-900
            rounded-lg
            border border-gray-300
            focus:ring-blue-500 focus:border-blue-500
          "
          placeholder="Your message..."
        ></textarea>
      </div>
      <div class="col-span-1 flex-col flex p-2 border-t-2 mr-10">
        <p class="p-1 pb-5 font-bold text-xl">Applications</p>
        <div class="mt-3">
          <div class="flex items-center mb-4 px-2">
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
                focus:ring-blue-500
                focus:ring-2
              "
            />
            <label
              for="default-checkbox"
              class="ml-2 text-sm font-medium text-gray-900"
              >Default checkbox</label
            >
          </div>
          <div class="flex items-center px-2">
            <input
              checked
              id="checked-checkbox"
              type="checkbox"
              value=""
              class="
                w-4
                h-4
                text-blue-600
                bg-gray-100
                rounded
                border-gray-300
                focus:ring-blue-500
                dark:focus:ring-blue-600 
                focus:ring-2
              "
            />
            <label
              for="checked-checkbox"
              class="ml-2 text-sm font-medium text-gray-900"
              >Checked state</label
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

export default defineComponent({
  setup() {},
  data: () => ({
    f: {
      title: "",
      city: "",
      state: "",
      zipcode: "",
      positionType: "",
      recruiter: 10,
      owner: 10,
      orderType: "",
      salary: "",
      duration: "",
      maxRate: "",
      minRate: "",
      category: "",
      openings: 0,
      pipeline_workflow: "",
      publish: false,
    },
    statuses: [
      { l: "Active", v: "lkjlk23lkj123lk12l" },
      { l: "Closed", v: "lkjlk23lkj123lk12l" },
    ],
    pipeline_workflows: [{ l: "General Application", v: "lkjlk23lkj123lk12l" }],
    orderTypes: [{ l: "Hire", v: "lkjlk23lkj123lk12l" }],
    positionTypes: [
      { l: "Remote", v: "rm" },
      { l: "Full Time", v: "fl" },
      { l: "Part Time", v: "pt" },
      { l: "Freelance", v: "fr" },
      { l: "With Relocation", v: "rl" },
    ],
  }),
  methods: {
    saveChanges() {
      console.log(this.f);
    },
  },
});
</script>
