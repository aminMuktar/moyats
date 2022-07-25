<template>
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
      empty-message="You don't have any registered companies"
      :items="companies"
      :headers="headers"
      @checkedAll="allChecked"
      @selected="singleSelected"
    >
      <template v-slot:[`name`]="{ item }">
        <div>
          <router-link
            class="text-sm text-blue-500 font-semibold"
            :to="`/companies/${item.companyId}`"
            v-text="item.name"
          ></router-link>
        </div>
      </template>
      <template v-slot:[`address`]="{ item }">
        <div>
          <p
            class="text-sm text-gray-500"
            v-text="formAddress(item.address)"
          ></p>
        </div>
      </template>
      <template v-slot:[`c`]="{ item }">
        <!-- contacts count -->
        <div>
          <p class="text-sm text-gray-500" v-text="item.contactsCount"></p>
        </div>
      </template>
      <template v-slot:[`o`]="{ item }">
        <!-- job orders count -->
        <div>
          <p class="text-sm text-gray-500" v-text="item.jobordersCount"></p>
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
      <template v-slot:[`status`]="{ item }">
        <div v-if="item.companyStatus">
          <chip
            @click="toggleStatusSlider('company', item.companyId)"
            :text="item.companyStatus.name"
            :color="item.companyStatus.color.hex"
          ></chip>
        </div>
      </template>
    </data-table>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DataTable from "../components/DataTable.vue";
import Chip from "../components/widgets/Chip.vue";
import { COMPANIES } from "../queries/company";
import {
  formAddress,
  parseDate,
  toggleStatusSlider,
  updateQparams,
} from "../utils/helpers";

export default defineComponent({
  components: { DataTable, Chip },
  async created() {
    this.page = this.$route.query.page ?? this.page;
    await this.getCompanies();
  },
  computed: {
    getFormupdateStatus() {
      this.getCompanies();
      return this.$store.getters.getFormupdateStatus;
    },
  },
  watch: {
    getFormupdateStatus(value) {
      if (value) {
        this.getCompanies();
      }
    },
  },
  methods: {
    parseDate,
    formAddress,
    updateQparams,
    toggleStatusSlider,
    async getCompanies() {
      const { data } = await this.$apollo.query({
        query: COMPANIES,
        fetchPolicy: "network-only",
        variables: {
          page: this.page,
          pageSize: this.pageSize,
        },
      });
      if (data) {
        this.companies = JSON.parse(JSON.stringify(data.companies.objects));
        this.total = data.companies.total;
        this.page = data.companies.page;
        this.pages = data.companies.pages;
        this.hasPrev = data.companies.hasPrev;
        this.hasNext = data.companies.hasNext;
        this.setDropt();
      }
    },
    singleSelected(e: any) {
      console.log(e);
    },
    allChecked(e: any) {
      console.log(`All Checked, ${e}`);
    },
    setDropt() {
      let fin: Array<any> = [];
      for (let i = 0; i < this.total; i++) {
        fin.push(`${i + 1}/${this.total}`);
      }
      this.dropts = fin;
    },
    async prev() {
      this.page--;
      await this.getCompanies();
      this.updateQparams(this.$route.path, this.page, this.pages);
    },
    async next() {
      this.page++;
      await this.getCompanies();
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
    dropts: [] as any,
    headers: [
      { value: "name", label: "Name" },
      { value: "address", label: "Address" },
      { value: "c", label: "C" },
      { value: "o", label: "O" },
      { value: "updated", label: "Updated" },
      { value: "status", label: "Status" },
    ],
    companies: [],
  }),
});
</script>
