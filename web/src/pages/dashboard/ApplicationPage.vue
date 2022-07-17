<template>
  <div class="m-5">
    <application-question-dialog
      v-if="application"
      :show="showDialog"
      @updated="addedApplicationQuestion"
      @close="showDialog = false"
      :app="application"
    ></application-question-dialog>

    <nav class="flex mb-3" aria-label="Breadcrumb">
      <ol class="inline-flex items-center space-x-1 md:space-x-3">
        <li>
          <div class="flex items-center">
            <router-link
              to="/applications"
              class="
                ml-1
                text-sm
                font-medium
                text-gray-700
                hover:text-gray-900
                md:ml-2
              "
              >Applications</router-link
            >
          </div>
        </li>
        <li aria-current="page">
          <div class="flex items-center">
            <svg
              class="w-6 h-6 text-gray-400"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                clip-rule="evenodd"
              ></path>
            </svg>
            <span
              class="ml-1 text-sm font-medium text-gray-500 md:ml-2"
              v-if="application"
              >{{ application.description }}</span
            >
          </div>
        </li>
      </ol>
    </nav>
    <div class="lg:w-1/2 xl:w-1/2 bg-white">
      <table class="table-auto" v-if="application">
        <tbody>
          <tr>
            <td class="p-2">Description</td>
            <td class="py-3 px-16 text-xl font-bold">
              {{ application.description }}
            </td>
          </tr>
          <tr>
            <td class="p-2">Header</td>
            <td class="py-3 px-16">{{ application.header }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="lg:w-3/4 xl:w-3/4 mt-3 bg-white">
      <div class="flex flex-row">
        <button
          type="button"
          class="
            py-2.5
            px-5
            m-3
            text-sm
            font-medium
            text-gray-900
            focus:outline-none
            bg-white
            rounded-lg
            border border-gray-200
            hover:bg-gray-100
            focus:z-10 focus:ring-4 focus:ring-gray-200
          "
          @click="showDialog = true"
        >
          Add Question
        </button>
      </div>

      <!-- draggable table -->
      <div class="col-6">
        <table
          class="
            border-collapse
            table-auto
            w-full
            whitespace-no-wrap
            bg-white
            table-striped
            relative
          "
        >
          <ul
            class="
              w-full
              text-sm
              font-medium
              text-gray-900
              bg-white
              border border-gray-200
            "
          >
            <transition-group>
              <draggable
                v-model="questionsSet"
                class="dragArea list-group w-full"
                :list="questionsSet"
                @change="log"
              >
                <li
                  v-for="q in questionsSet"
                  :key="q.id"
                  class="
                    py-4
                    cursor-move
                    px-4
                    w-full
                    hover:bg-gray-200
                    border-b border-gray-200
                  "
                >
                  <div class="flex flex-row">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-6 w-6"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                      stroke-width="2"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        d="M8 9l4-4 4 4m0 6l-4 4-4-4"
                      />
                    </svg>
                    <p>
                      {{ q.fieldTitle }}
                    </p>
                  </div>
                </li>
              </draggable>
            </transition-group>
          </ul>
        </table>

        <!-- <draggable
          :list="questions"
          class="list-group"
          ghost-class="ghost"
          :move="checkMove"
          @start="drag = true"
          @end="drag = false"
        >
          <div class="list-group-item cursor-move" v-for="(q, ix) in questions" :key="ix">
            {{ q.fieldTitle }}
          </div>
        </draggable> -->
      </div>

      <!-- end of table -->
      <data-table
        @prev="prev"
        @next="next"
        :dropts="dropts"
        :hasNext="hasNext"
        :hasPrev="hasPrev"
        :total="total"
        :page="page"
        :pages="pages"
        class="hidden"
        empty-message="you don't have any questions yet yet"
        :items="questions"
        :headers="headers"
        :loadingState="loading"
        @checkedAll="allChecked"
        @selected="singleSelected"
      >
        <template v-slot:[`title`]="{ item }">
          <div class="text-blue-500">
            <p>{{ item.fieldTitle }}</p>
          </div>
        </template>
        <template v-slot:[`saveTo`]="{ item }">
          <div class="text-gray-500">
            <p>{{ item.saveTo }}</p>
          </div>
        </template>
        <template v-slot:[`triggers`]="{ item }">
          <button
            type="button"
            class="
              text-white
              bg-green-700
              hover:bg-green-800
              focus:ring-4 focus:outline-none focus:ring-blue-300
              font-medium
              rounded-lg
              text-sm
              p-1
              text-center
              inline-flex
              items-center
            "
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="2"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M12 4v16m8-8H4"
              />
            </svg>

            <span class="sr-only">Icon description</span>
          </button>
        </template>
      </data-table>
    </div>
  </div>
</template>

<script lang="ts">
import { VueDraggableNext } from "vue-draggable-next";
import { defineComponent } from "vue";
import DataTable from "../../components/DataTable.vue";
import { fetchApplication, fetchApplicationQuestions } from "../../services";
import { parseDate, updateQparams } from "../../utils/helpers";
import ApplicationQuestionDialog from "../../components/applications/ApplicationQuestionDialog.vue";

export default defineComponent({
  components: {
    DataTable,
    ApplicationQuestionDialog,
    draggable: VueDraggableNext,
  },
  async created() {
    await this.fetchApplciation();
    await this.fetchQuestions();
  },
  methods: {
    async fetchQuestions() {
      const { data } = await fetchApplicationQuestions({
        app: this.$route.params.appid,
      });
      if (data) {
        this.questions = data.applicationQuestions;
        this.questionsSet = [...this.questions];
      }
    },
    async fetchApplciation() {
      const { data } = await fetchApplication({
        app: this.$route.params.appid,
      });
      if (data) {
        this.application = data.joborderApplication;
      }
    },
    updateQparams,
    async fetchApplications() {},
    singleSelected(e: any) {
      console.log(e);
    },
    addedApplicationQuestion() {
      alert("Added Application");
    },
    allChecked(e: any) {
      console.log(`All Checked, ${e}`);
    },
    async prev() {
      this.page--;
      await this.fetchQuestions();
      this.updateQparams(this.$route.path, this.page, this.pages);
    },
    async next() {
      this.page++;
      await this.fetchQuestions();
      this.updateQparams(this.$route.path, this.page, this.pages);
    },
    log(event) {
      console.log(event);
    },
  },
  data: () => ({
    total: 0,
    pages: 1,
    enabled: true,
    drag: false,
    hasNext: false,
    showDialog: false,
    hasPrev: false,
    page: 1 as any,
    pageSize: 10,
    loading: false,
    dropts: [] as any,
    questionsSet: [] as any,
    questions: [] as any,
    headers: [
      { value: "title", label: "Title" },
      { value: "saveTo", label: "Save To" },
      { value: "triggers", label: "Triggers" },
    ],
    application: null as any,
  }),
});
</script>

<style>
</style>