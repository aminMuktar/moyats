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
        <div v-if="editMode" style="width: 95%">
          <textarea
            v-model="notes"
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
        <div v-else>
          <div class="sm:col-span-1 md:flex lg:flex p-2" v-if="data.notes">
            <p v-text="data.notes"></p>
          </div>
          <p class="text-center py-5" v-else>No Notes Yet</p>
        </div>
      </template>
    </dashboard-card-widget>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { updateContactNotes } from "../../services";
import DashboardCardWidget from "../DashboardCardWidget.vue";
import Spinner from "../Spinner.vue";

export default defineComponent({
  components: { DashboardCardWidget, Spinner },
  setup() {},
  props: ["data"],
  data: () => ({
    editMode: false,
    editCmp: false,
    loading: false,
    notes: "",
  }),
  created() {
    this.notes = this.data.notes;
  },
  methods: {
    async saveChanges(e) {
      e.preventDefault();
      this.loading = true;
      const { data } = await updateContactNotes({
        contact: this.$route.params.cid,
        note: this.notes,
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
