<template>
  <div>
    <dashboard-card-widget>
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
          >
            <template v-slot:[`name`]="{ item }">
              <div>
                <router-link
                  class="text-sm text-blue-500 font-semibold"
                  :to="`/candidates/${item.candidate.candidateId}`"
                >
                  {{ item.candidate.candidateProfile.firstName }}
                  {{ item.candidate.candidateProfile.lastName }}
                </router-link>
              </div>
            </template>
            <template v-slot:[`location`]="{ item }">
              <div>
                <p
                  class="text-sm text-gray-500"
                  v-text="formAddress(item.candidate.address)"
                ></p>
              </div>
            </template>
            <template v-slot:[`createdAt`]="{ item }">
              <div>
                <p
                  class="text-sm text-gray-500"
                  v-text="parseDate(item.createdAt)"
                ></p>
              </div>
            </template>

            <template v-slot:[`status`]="{ item }">
              <div class="flex flex-row">
                <chip
                  :text="item.status.statusName"
                  :color="item.status.color.hex"
                ></chip>
              </div>
            </template>
            <template v-slot:[`source`]="{ item }">
              <div>
                <p
                  class="text-sm text-gray-500"
                  v-text="item.candidate.source.name"
                ></p>
              </div>
            </template>
          </data-table>
        </div>
      </template>
    </dashboard-card-widget>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { loadJobOrderApplications } from "../../services";
import { formAddress,parseDate } from "../../utils/helpers";
import DashboardCardWidget from "../DashboardCardWidget.vue";
import DataTable from "../DataTable.vue";
import Chip from "../widgets/Chip.vue";

export default defineComponent({
  components: { DashboardCardWidget, DataTable, Chip },
  async created() {
    await this.fetchJoborderCandidates();
  },
  data: () => ({
    total: 0,
    pages: 1,
    hasNext: false,
    hasPrev: false,
    page: 1,
    pageSize: 2,
    dropts: [] as any,
    candidates: [] as any,
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
        value: "createdAt",
        label: "Added Date",
      },
      {
        value: "status",
        label: "Status Current",
      },
      // {
      //   value: "action",
      //   label: "Action",
      // },
    ],
  }),
  methods: {
    parseDate,
    formAddress,
    async fetchJoborderCandidates() {
      const {
        data: {
          joborderApplicantPipeline: { objects },
        },
      } = await loadJobOrderApplications({
        joborder: this.$route.params.jid,
        page: this.page,
        pageSize: this.pageSize,
      });
      if (objects) {
        this.candidates = objects;
      }
    },
    setDropt() {
      let fin: any = [];
      for (let i = 0; i < this.total; i++) {
        fin.push(`${i + 1}/${this.total}`);
      }
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
