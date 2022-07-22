<template>
  <div class="flex w-full flex-col">
    <div
      class="flex flex-col rounded-lg overflow-hidden bg-white shadow relative"
    >
      <!-- loading overlay -->

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
        <div class="flex p-2 flex-row w-full fixed gap-2 bg-white">
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
        <div class="grid grid-cols-1 w-full">
          <div class="flex col-span-2 w-full p-4 mt-16">
            <div class="w-56">
              <label class="sr-only" for="name">Title</label>
              <span class="m-1">Name* </span>
            </div>
            <div class="w-full grid lg:grid-cols-3 xl:grid-cols-3 gap-3 ml-9">
              <input
                required
                v-model="firstName"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="First Name"
                type="text"
                id="name"
              />
              <input
                required
                v-model="lastName"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="Last Name"
                type="text"
                id="name"
              />
            </div>
          </div>
          <div class="flex col-span-2 p-2">
            <div class="w-56">
              <label class="sr-only" for="name">Title</label>
              <span class="m-3 w-full">Title*</span>
            </div>
            <div class="flex gap-0 w-full ml-12 mr-2">
              <input
                pattern="^[w-.]+@([w-]+.)+[w-]{2,4}$"
                required
                v-model="title"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="Title"
                type="text"
                id="title"
              />
            </div>
          </div>
          <div class="flex col-span-2 p-2">
            <div class="w-56">
              <label class="sr-only" for="name">Email</label>
              <span class="m-3 w-full">Email*</span>
            </div>
            <div class="flex gap-0 w-full ml-12 mr-2">
              <input
                pattern="^[w-.]+@([w-]+.)+[w-]{2,4}$"
                required
                v-model="email"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="Email"
                type="email"
                id="email"
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
          <!-- adress inputs -->
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
          <company-selector
            :showHeader="true"
            @cleared="company = null"
            @itemClicked="companySelected"
          ></company-selector>
        </div>

        <div class="col-span-2 flex p-2 mb-52"></div>
      </form>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { uuid } from "vue-uuid";
import { addContact } from "../../services";
import CompanySelector from "../selectors/CompanySelector.vue";

export default defineComponent({
  components: { CompanySelector },
  data: () => ({
    firstName: "",
    lastName: "",
    email: "",
    title: "",
    loadingState: false,
    cellNumber: "",
    homeNumber: "",
    workNumber: "",
    city: "",
    state: "",
    country: "",
    company: null as any,
  }),
  methods: {
    companySelected(v) {
      this.company = v;
    },
    saveChanges(e) {
      e.preventDefault();
      this.loadingState = true;
      const { data, errors }: any = addContact({
        input: {
          firstName: this.firstName,
          lastName: this.lastName,
          phones: {
            cellPhone: this.cellNumber,
            homePhone: this.homeNumber,
            workPhone: this.workNumber,
          },
          email: this.email,
          city: this.city,
          country: this.country,
          state: this.state,
          company: this.company.companyId,
        },
      });
      if (!errors) {
        this.loadingState = false;
        this.$emit("contactAdded");
        this.$store.commit("updateFormupdateStatus", uuid.v4());
        this.$emit("close");
      }
    },
  },
});
</script>
