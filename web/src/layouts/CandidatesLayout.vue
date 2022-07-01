<template>
  <div>
    DAWG {{ $store.getters.getFormupdateStatus }}
    <data-table
      @prev="prev"
      @next="next"
      :dropts="dropts"
      :hasNext="hasNext"
      :hasPrev="hasPrev"
      :total="total"
      :page="page"
      :pages="pages"
      empty-message="you don't have any candidates yet"
      :items="candidates"
      :headers="headers"
      :loadingState="loading"
      @checkedAll="allChecked"
      @selected="singleSelected"
    >
      <template v-slot:[`name`]="{ item }">
        <div>
          <router-link
            class="text-sm text-blue-500 font-semibold"
            :to="`/candidates/${item.candidateId}`"
          >
            {{ item.candidateProfile.firstName }}
            {{ item.candidateProfile.lastName }}
          </router-link>
        </div>
      </template>
      <template v-slot:[`location`]="{ item }">
        <div>
          <p
            class="text-sm text-gray-500"
            v-text="formAddress(item.address)"
          ></p>
        </div>
      </template>
      <template v-slot:[`updated`]="{ item }">
        <div>
          <p
            class="text-sm text-gray-500"
            v-text="parseDate(item.updatedAt)"
          ></p>
        </div>
      </template>
      <template v-slot:[`recentStatus`]="{ item }">
        <div class="flex flex-row" v-if="item.latestJoborder">
          <chip
            :text="item.latestJoborder.jobOrderStatus.statusName"
            :color="item.latestJoborder.jobOrderStatus.color.hex"
          ></chip>
          <span class="px-3">-</span>
          <router-link
            class="text-sm text-blue-500 font-semibold"
            :to="`/joborders/${item.latestJoborder.joborderId}`"
            v-text="item.latestJoborder.jobDetail.title"
          ></router-link>
          <span class="px-3">-</span>
          <router-link
            class="text-sm text-blue-500 font-semibold"
            :to="`/companies/${item.latestJoborder.company.companyId}`"
            v-text="item.latestJoborder.company.name"
          ></router-link>
        </div>
        <div v-else>
          <p>No Status</p>
        </div>
      </template>
    </data-table>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DataTable from "../components/DataTable.vue";
import Chip from "../components/widgets/Chip.vue";
import { CANDIDATES } from "../queries/candidates";
import { formAddress, parseDate, updateQparams } from "../utils/helpers";
import { uuid } from "vue-uuid";

export default defineComponent({
  async created() {
    // this.$store.commit("updateFormupdateStatus", uuid.v4());
    this.page = this.$route.query.page ?? this.page;
    await this.getCandidates();
  },
  computed: {
    getFormupdateStatus() {
      this.getCandidates();
      return this.$store.getters.getFormupdateStatus;
    },
  },
  watch: {
    getFormupdateStatus(value) {
      if (value) {
        console.log(this.$store.getters.getFormupdateStatus, "dawgx");
        this.getCandidates();
      }
    },
  },
  components: { DataTable, Chip },

  methods: {
    parseDate,
    formAddress,
    updateQparams,
    singleSelected(e: any) {
      console.log(e);
    },
    allChecked(e: any) {
      console.log(`All Checked, ${e}`);
    },
    async getCandidates() {
      this.loading = true;
      const { data } = await this.$apollo.query({
        query: CANDIDATES,
        fetchPolicy: "network-only",
        variables: {
          page: this.page,
          pageSize: this.pageSize,
        },
      });
      if (data) {
        this.loading = false;
        this.candidates = JSON.parse(JSON.stringify(data.candidtes.objects));
        this.total = data.candidtes.total;
        this.page = data.candidtes.page;
        this.pages = data.candidtes.pages;
        this.hasPrev = data.candidtes.hasPrev;
        this.hasNext = data.candidtes.hasNext;
        this.setDropt();
      } else {
        this.loading = false;
      }
    },
    setDropt() {
      let fin = [] as any;
      for (let i = 0; i < this.total; i++) {
        fin.push(`${i + 1}/${this.total}`);
      }
      this.dropts = fin;
    },
    async prev() {
      this.page--;
      await this.getCandidates();
      this.updateQparams(this.$route.path, this.page, this.pages);
    },
    async next() {
      this.page++;
      await this.getCandidates();
      this.updateQparams(this.$route.path, this.page, this.pages);
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
      { value: "name", label: "name" },
      { value: "location", label: "Location" },
      { value: "updated", label: "Updated" },
      { value: "recentStatus", label: "Recent Status" },
    ],
    candidates: [],
  }),
});
</script>
