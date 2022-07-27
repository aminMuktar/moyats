<template>
  <div v-if="setups" class="bg-white">
    <!-- TODO fetch workflow details and replace title -->
    <p class="p-6 font-bold text-xl">General Workflow</p>
    <div class="overflow-x-auto relative">
      <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50">
          <tr>
            <th scope="col" class="py-3 px-6">Status</th>
            <th scope="col" class="py-3 px-6">Mapping</th>
            <th scope="col" class="py-3 px-6">Prereqs</th>
            <th scope="col" class="py-3 px-6">Triggers</th>
            <th scope="col" class="py-3 px-6">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr
            class="bg-white border-b w-full"
            v-for="(st, ix) in setups"
            :key="ix"
          >
            <th
              scope="row"
              class="py-4 px-6 font-medium text-gray-900 whitespace-nowrap"
            >
              <chip
                :text="st.status.statusName"
                :color="st.status.color.hex"
              ></chip>
            </th>
            <td class="py-4 px-6 font-bold">
              <p v-if="st.mappingStatus">
                {{ st.mappingStatus.statusName }}
              </p>
              <p v-else>-</p>
            </td>
            <td class="">
              <div
                v-for="(pr, ix) in st.prerequisiteStatus"
                :key="ix"
                class="flex flex-col gap-3"
              >
                <chip
                  class="my-3"
                  :text="pr.statusName"
                  :color="pr.color.hex"
                ></chip>
              </div>
            </td>
            <td class="py-4 px-6">
              <div class="flex flex-row">
                <p v-for="(tr, ix) in st.triggers" :key="ix">
                  {{ tr.description.slice(0, 100) }}
                </p>
                <button class="mx-2 rounded-md hover:bg-gray-200">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 text-green-500"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-11a1 1 0 10-2 0v2H7a1 1 0 100 2h2v2a1 1 0 102 0v-2h2a1 1 0 100-2h-2V7z"
                      clip-rule="evenodd"
                    />
                  </svg>
                </button>
              </div>
            </td>
            <td class="py-4 px-6" @click="deleteStep(st)">
              <button class="mx-2 rounded-md hover:bg-gray-200">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 text-red-500"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fill-rule="evenodd"
                    d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                    clip-rule="evenodd"
                  />
                </svg>
              </button>
            </td>
          </tr>
          <!-- </draggable> -->
        </tbody>
      </table>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { loadPipelineSetup } from "../../services";
import { VueDraggableNext } from "vue-draggable-next";
import Chip from "../../components/widgets/Chip.vue";

export default defineComponent({
  components: { draggable: VueDraggableNext, Chip },
  data: () => ({
    setups: null as any,
  }),
  async created() {
    await this.fetchWorkflow();
  },
  methods: {
    async deleteStep(st) {},
    async fetchWorkflow() {
      const { data } = await loadPipelineSetup({
        workflow: this.$route.params.wid,
      });
      if (data) {
        this.setups = data.pipelineWorkflowSetup;
      }
    },
  },
});
</script>
