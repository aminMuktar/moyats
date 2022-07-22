<template>
  <div class="flex w-full flex-col">
    <div
      class="flex flex-col rounded-lg overflow-hidden bg-white shadow relative"
    >
      <div
        v-if="loadingState"
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
      <form class="w-full" ref="form" @submit="saveChanges">
        <div class="flex p-2 border-b-2 flex-row w-full fixed gap-2 bg-white">
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
        <div clas>
          <div class="flex col-span-2 w-full p-4 mt-16">
            <div class="w-56">
              <label class="sr-only" for="name">Title</label>
              <span class="m-1">Company Name* </span>
            </div>
            <div class="w-full grid gap-3 ml-9">
              <input
                required
                v-model="companyName"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="Company Name"
                type="text"
                id="name"
              />
            </div>
          </div>

          <div class="flex col-span-2 p-2">
            <div class="w-56">
              <label class="sr-only" for="name">Location</label>
              <span class="m-3 w-full">Location*</span>
            </div>
            <div class="grid grid-cols-3 gap-2">
              <input
                required
                v-model="city"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="City"
                type="text"
                id="name"
              />
              <input
                v-model="state"
                required
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="State"
                type="text"
                id="name"
              />
              <input
                required
                v-model="country"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="Country"
                type="text"
                id="name"
              />
            </div>
          </div>
          <div class="flex col-span-2 w-full p-4">
            <div class="w-56">
              <label class="sr-only" for="name">Phones</label>
              <span class="m-1">Phones* </span>
            </div>
            <div class="w-full grid lg:grid-cols-2 xl:grid-cols-2 gap-3 ml-10">
              <input
                v-model="cellNumber"
                required
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                type="tel"
                pattern="(\+\s*2\s*5\s*1\s*9\s*(([0-9]\s*){8}\s*))|(0\s*9\s*(([0-9]\s*){8}))"
                placeholder="Cell Number"
                id="name"
              />
              <input
                v-model="homeNumber"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="Home Number"
                type="tel"
                pattern="(\+\s*2\s*5\s*1\s*9\s*(([0-9]\s*){8}\s*))|(0\s*9\s*(([0-9]\s*){8}))"
                id="name"
              />
              <input
                v-model="workNumber"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="Work Number"
                type="tel"
                pattern="(\+\s*2\s*5\s*1\s*9\s*(([0-9]\s*){8}\s*))|(0\s*9\s*(([0-9]\s*){8}))"
                id="name"
              />
            </div>
          </div>
          <!-- website form input -->
          <div class="flex col-span-2 w-full p-4">
            <div class="w-56">
              <label class="sr-only" for="name">Website</label>
              <span class="m-1">Website* </span>
            </div>
            <div class="w-full grid gap-3 ml-10">
              <input
                v-model="website"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="Website"
                type="text"
                id="name"
              />
            </div>
          </div>
          <!-- textarea form input -->
          <div class="flex col-span-2 w-full p-4">
            <div class="w-56">
              <label class="sr-only" for="name">Key Technologies </label>
              <span class="m-1">Key Technologies* </span>
            </div>
            <div class="w-full grid gap-3 ml-10">
              <textarea
                v-model="keyTecs"
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
                placeholder="Key Technologies"
                id="name"
              ></textarea>
            </div>
          </div>
          <!-- departments input -->
          <div class="flex col-span-2 w-full p-4">
            <div class="w-56">
              <label class="sr-only" for="name">Departments</label>
              <span class="m-1">Departments* </span>
            </div>
            <div class="w-full grid gap-3 ml-10">
              <input
                v-model="departments"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="Departments"
                type="text"
                id="name"
              />
            </div>
          </div>
          <!-- notes -->
          <div class="flex col-span-2 w-full p-4">
            <div class="w-56">
              <label class="sr-only" for="name">Notes</label>
              <span class="m-1">Notes* </span>
            </div>
            <div class="w-full grid gap-3 ml-10">
              <textarea
                v-model="notes"
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
                placeholder="Notes"
                id="name"
              ></textarea>
            </div>
          </div>
          <div class="col-span-2 flex p-2 mb-52"></div>
        </div>
      </form>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { uuid } from "vue-uuid";
import { addCompany } from "../../services";

export default defineComponent({
  data: () => ({
    keyTecs: "",
    loadingState: false,
    firstName: "",
    middleName: "",
    city: "",
    state: "",
    country: "",
    notes: "",
    website: "",
    companyName: "",
    cellNumber: "",
    homeNumber: "",
    workNumber: "",
    departments: "",
  }),
  methods: {
    async saveChanges(e) {
      e.preventDefault();
      this.loadingState = true;
      const { data, errors } = await addCompany({
        input: {
          name: this.companyName,
          phones: {
            cellPhone: this.cellNumber,
            homePhone: this.homeNumber,
            workPhone: this.workNumber,
          },
          city: this.city,
          country: this.country,
          state: this.state,
          website: this.website,
          keyTechnologies: this.keyTecs,
          departments: this.departments,
          notes: this.notes,
        },
      });
      if (!errors) {
        this.loadingState = false;
        this.$emit("companyAdded");
        this.$store.commit("updateFormupdateStatus", uuid.v4());
        this.$emit("close");
      }
    },
  },
});
</script>
