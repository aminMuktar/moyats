<template>
  <div>
    <dashboard-card-widget slot="body">
      <template v-slot:header>
        <div>
          <div class="flex flex-row justify-between">
            <p class="p-3 font-semibold text-lg">Pipeline</p>
            <div class="flex flex-row">
              <button class="p-1 m-2 border-2">Add Existing Candidate</button>
              <button class="p-1 m-2 border-2">Add New Candidate</button>
            </div>
          </div>
          <div class="grid grid-cols-5 mx-2">
            <div
              class="my-2 border-2 py-1 text-center bg-gray-100"
              v-for="x in 5"
              :key="x"
            >
              <p>1</p>
              <p>New Applicant</p>
            </div>
          </div>
        </div>
      </template>
      <template v-slot:body>
        <div>
          <data-table
            @prev="prev"
            @next="next"
            :dropts="dropts"
            :hasNext="hasNext"
            :hasPrev="hasPrev"
            :total="total"
            :page="page"
            :pages="pages"
            :emptyMessage="'No candidates added yet'"
            :items="candidates"
            :headers="headers"
            @checkedAll="allChecked"
            @selected="singleSelected"
          ></data-table>
        </div>
      </template>
    </dashboard-card-widget>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DashboardCardWidget from "../DashboardCardWidget.vue";
import DataTable from "../DataTable.vue";

export default defineComponent({
  components: { DashboardCardWidget, DataTable },
  setup() {},
  data: () => ({
    total: 0,
    pages: 1,
    hasNext: false,
    hasPrev: false,
    page: 1,
    pageSize: 2,
    dropts: [] as any,
    candidates: [],
    headers: [
      {
        value: "name",
        label: "Name",
      },
      {
        value: "location",
        label: "Location",
      },
      {
        value: "source",
        label: "Source",
      },
      {
        value: "added",
        label: "Added Date",
      },
      {
        value: "staus",
        label: "Status Current",
      },
      {
        value: "action",
        label: "Action",
      },
    ],
  }),
  methods: {
    setDropt() {
      let fin = [];
      for (let i = 0; i < this.total; i++) {
        fin.push(`${i + 1}/${this.total}`);
      }
      console.clear();
      console.warn(this.total);
      this.dropts = fin;
    },
    async fetchPipelineCandidates() {},
    singleSelected(e: any) {
      console.log(e);
    },
    allChecked(e: any) {
      console.log(`All Checked, ${e}`);
    },
    async prev() {
      this.page--;
      await this.fetchPipelineCandidates();
    },
    async next() {
      this.page++;
      await this.fetchPipelineCandidates();
    },
  },
});
</script>
