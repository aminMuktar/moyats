<template>
  <div class="bg-white">
    <p class="font-bold text-3xl p-3">Workflows</p>
    <div class="w-full bg-white">
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
          border border-gray-400
          hover:bg-gray-100
          focus:z-10 focus:ring-4 focus:ring-gray-200
        "
      >
        Add Workflow
      </button>
    </div>
    <data-table
      @prev="prev"
      @next="next"
      :dropts="dropts"
      :hasNext="hasNext"
      :hasPrev="hasPrev"
      :total="10"
      :page="page"
      :pages="pages"
      empty-message="you don't have any candidates yet"
      :items="workflows"
      :headers="headers"
      :loadingState="loading"
      @checkedAll="allChecked"
      @selected="singleSelected"
    >
      <template v-slot:[`name`]="{ item }">
        <div class="text-blue-500">
          <router-link :to="`/workflows/${item.pipelineId}`">{{
            item.title
          }}</router-link>
        </div>
      </template>
    </data-table>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DataTable from "../components/DataTable.vue";
import { loadPipelineWorkflows } from "../services";
import { updateQparams } from "../utils/helpers";

export default defineComponent({
  props: ["data"],
  components: {
    DataTable,
  },
  async created() {
    await this.fetchPipelineWorkflows();
  },
  data: () => ({
    workflows: [] as any,
    total: 0,
    pages: 1,
    hasNext: false,
    hasPrev: false,
    page: 1 as any,
    pageSize: 10,
    showDialog: false,
    loading: false,
    dropts: [] as any,
    headers: [{ value: "name", label: "Name" }],
  }),
  methods: {
    async fetchPipelineWorkflows() {
      const {
        data: { pipelineWorkflows },
      } = await loadPipelineWorkflows();
      this.workflows = pipelineWorkflows;
    },
    updateQparams,
    async prev() {
      this.page--;
      await this.fetchPipelineWorkflows();
      this.updateQparams(this.$route.path, this.page, this.pages);
    },
    async next() {
      this.page++;
      await this.fetchPipelineWorkflows();
      this.updateQparams(this.$route.path, this.page, this.pages);
    },
    singleSelected() {},
    allChecked() {},
    setDropt() {
      let fin = [] as any;
      for (let i = 0; i < this.total; i++) {
        fin.push(`${i + 1}/${this.total}`);
      }
      this.dropts = fin;
    },
  },
});
</script>
