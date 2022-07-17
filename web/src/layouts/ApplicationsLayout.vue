<template>
  <div>
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
      :items="applications"
      :headers="headers"
      :loadingState="loading"
      @checkedAll="allChecked"
      @selected="singleSelected"
    >
      <template v-slot:[`description`]="{ item }">
        <div class="text-blue-500">
          <router-link :to="`/applications/${item.applicationId}`">{{
            item.description
          }}</router-link>
        </div>
      </template>
      <template v-slot:[`questions`]="{ item }">
        <div class="text-gray-500">
          <p>10</p>
        </div>
      </template>
      <template v-slot:[`updated`]="{ item }">
        <div class="text-gray-500">
          <p class="text-sm" v-text="parseDate(item.updatedAt)"></p>
        </div>
      </template>

      <template v-slot:[`enteredBy`]="{ item }">
        <div>
          <p>Amen Abe</p>
        </div>
      </template>
    </data-table>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import DataTable from "../components/DataTable.vue";
import { fetchApplications } from "../services";
import { formAddress, parseDate, updateQparams } from "../utils/helpers";

export default defineComponent({
  components: { DataTable },
  setup() {},
  async created() {
    // this.$store.commit("updateFormupdateStatus", uuid.v4());
    this.page = this.$route.query.page ?? this.page;
    await this.loadApplications();
  },

  methods: {
    parseDate,
    updateQparams,
    async prev() {
      this.page--;
      await this.loadApplications();
      this.updateQparams(this.$route.path, this.page, this.pages);
    },
    async next() {
      this.page++;
      await this.loadApplications();
      this.updateQparams(this.$route.path, this.page, this.pages);
    },
    setDropt() {
      let fin = [] as any;
      for (let i = 0; i < this.total; i++) {
        fin.push(`${i + 1}/${this.total}`);
      }
      this.dropts = fin;
    },
    async loadApplications() {
      const { data, errors } = await fetchApplications();
      if (data) {
        this.loading = false;
        this.applications = data.joborderApplications;
        this.total = data.jobOrders.total;
        this.page = data.jobOrders.page;
        this.pages = data.jobOrders.pages;
        this.hasPrev = data.jobOrders.hasPrev;
        this.hasNext = data.jobOrders.hasNext;
        this.setDropt();
      } else {
        this.loading = false;
      }
    },
    singleSelected(e: any) {
      console.log(e);
    },
    allChecked(e: any) {
      console.log(`All Checked, ${e}`);
    },
  },
  data: () => ({
    total: 0,
    pages: 1,
    hasNext: false,
    hasPrev: false,
    page: 1 as any,
    pageSize: 10,
    loading: false,
    dropts: [] as any,
    headers: [
      { value: "description", label: "name" },
      { value: "questions", label: "Questions" },
      { value: "updated", label: "Updated" },
      { value: "enteredBy", label: "Entered By" },
    ],
    applications: [],
  }),
});
</script>

<style>
</style>