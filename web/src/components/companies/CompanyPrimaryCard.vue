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
          <p class="p-3 font-semibold text-lg">Primary</p>
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
                <td class="p-2">Address</td>
                <td v-if="editMode" class="mb-4">
                  <div class="grid grid-cols-2 mt-5 mx-11 gap-2 gap-y-2 mb-5">
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

                <td class="py-2 px-16" v-else>
                  {{ formAddress(data.address) }}
                </td>
              </tr>
              <tr>
                <td class="p-2">Phones</td>
                <td v-if="editMode">
                  <div class="grid grid-cols-2 mt-10 mx-11 gap-2 gap-y-2">
                    <input
                      v-model="cellNumber"
                      required
                      class="
                        w-full
                        p-1
                        text-sm
                        border-gray-200 border-2
                        rounded-md
                      "
                      placeholder="Cell Number"
                      type="name"
                      id="name"
                    />
                    <input
                      v-model="homeNumber"
                      required
                      class="
                        w-full
                        p-1
                        text-sm
                        border-gray-200 border-2
                        rounded-md
                      "
                      placeholder="Home Number"
                      type="name"
                      id="name"
                    />
                    <input
                      v-model="workNumber"
                      required
                      class="
                        w-full
                        p-1
                        text-sm
                        border-gray-200 border-2
                        rounded-md
                      "
                      placeholder="Work Number"
                      type="name"
                      id="name"
                    />
                  </div>
                </td>

                <td class="py-2 px-16" v-else>
                  {{ data.phones.cellNumber }}
                </td>
              </tr>
              <tr>
                <td class="p-2">Website</td>
                <td class="py-2 px-11 text-blue-500" v-if="editMode">
                  <input
                    v-model="website"
                    required
                    class="
                      w-full
                      p-1
                      text-sm
                      border-gray-200 border-2
                      rounded-md
                    "
                    placeholder="Work Number"
                    type="url"
                    id="website"
                  />
                </td>

                <td class="py-2 px-16 text-blue-500" v-else>
                  <a target="_blank" :href="data.website">{{ data.website }}</a>
                </td>
              </tr>
              <tr>
                <td class="p-2">Social Media</td>
                <td class="py-2 px-16"></td>
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
import { updateCompanyPrimary } from "../../services/candidates";
import Spinner from "../Spinner.vue";

export default defineComponent({
  components: { DashboardCardWidget, Spinner },
  props: ["data"],
  created() {
    this.country = this.data.address.country;
    this.state = this.data.address.country;
    this.city = this.data.address.city;
    this.cellNumber = this.data.phones.cellNumber;
    this.homeNumber = this.data.phones.homeNumber;
    this.workNumber = this.data.phones.workNumber;
    this.website = this.data.website;
  },
  data: () => ({
    editMode: false,
    city: "",
    state: "",
    country: "",
    website: "",
    loading: false,
    homeNumber: "",
    cellNumber: "",
    workNumber: "",
  }),
  methods: {
    formAddress,
    async saveChanges() {
      this.editMode = false;
      this.loading = true;
      const { data } = await updateCompanyPrimary({
        input: {
          phones: {
            cellPhone: this.cellNumber,
            homePhone: this.homeNumber,
            workPhone: this.workNumber,
          },
          website: this.website,
          city: this.city,
          country: this.country,
          state: this.state,
          company: this.$route.params.cpid,
        },
      });
      console.log(data, "data");
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
