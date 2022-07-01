<template>
  <div>
    <work-history-form
      :show="showMainDialog"
      @close="showMainDialog = false"
    ></work-history-form>
    <dashboard-card-widget>
      <template v-slot:header>
        <div class="flex justify-between">
          <p class="p-3 font-semibold text-lg">Notes</p>
          <div class="flex flex-row justify-end gap-2 mx-2">
            <button
              @click="showMainDialog = true"
              type="button"
              class="
                hover:text-black
                border border-blue-700
                hover:bg-blue-100
                focus:ring-4 focus:outline-none focus:ring-blue-300
                font-medium
                rounded-lg
                text-sm
                px-1
                py-1
                text-center
                w-32
                h-10
                m-2
              "
            >
              Add Work History
            </button>
          </div>
        </div>
      </template>
      <template v-slot:body>
        <div>
          <div
            class="sm:col-span-1 md:flex lg:flex p-2"
            v-if="data.workHistory.length"
          >
            <div class="text-sm w-full">
              <ul
                class="
                  w-full
                  text-sm
                  font-medium
                  bg-white
                  border-t border-gray-200
                "
              >
                <li
                  :key="ix"
                  v-for="(wh, ix) in data.workHistory"
                  class="w-full px-4 py-2 border-b border-gray-200 rounded-t-lg"
                >
                  <div class="flex flex-row justify-between">
                    <p class="font-bold pt-2">
                      {{ wh.title }}
                    </p>
                    <div class="flex flex-row">
                      <p class="pt-2">2021</p>
                      <span class="p-2"> - </span>
                      <p class="pt-2">2022</p>
                      <div class="flex flex-row px-10">
                        <button class="text-blue-600 border-2 rounded-full">
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            class="h-4 w-4 m-2"
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
                          class="text-blue-600 border-2 mx-2 rounded-full"
                        >
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            class="h-4 w-4 m-2 text-red-600"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                          >
                            <path
                              fill-rule="evenodd"
                              d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                              clip-rule="evenodd"
                            />
                          </svg>
                        </button>
                      </div>
                    </div>
                  </div>
                  <!-- {{ wh }} -->
                </li>
              </ul>
            </div>
          </div>
          <p v-else class="text-center py-5">No Work History</p>
        </div>
      </template>
    </dashboard-card-widget>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DashboardCardWidget from "../DashboardCardWidget.vue";
import WorkHistoryForm from "./WorkHistoryForm.vue";

export default defineComponent({
  components: { DashboardCardWidget, WorkHistoryForm },
  props: ["data"],
  data: () => ({
    showMainDialog: false,
    editMode: false,
    loading: false,
  }),
});
</script>
