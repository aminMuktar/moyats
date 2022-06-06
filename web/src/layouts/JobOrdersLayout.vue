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
      :emptyMessage="emptyMesasge"
      :items="joborders"
      :headers="headers"
      @checkedAll="allChecked"
      @selected="singleSelected"
    >
      <template v-slot:[`title`]="{ item }">
        <div>
          <router-link
            class="text-sm text-blue-500 font-semibold"
            :to="`/joborders/${item.joborderId}`"
            v-text="item.jobDetail.title"
          ></router-link>
        </div>
      </template>
      <template v-slot:[`organization`]="{ item }">
        <div>
          <a class="text-sm text-gray-500" v-text="item.organization.name"></a>
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
      <template v-slot:[`c`]>
        <div>
          <!-- candidates submitted -->
          <p class="text-sm text-gray-500">12</p>
        </div>
      </template>
      <template v-slot:[`s`]>
        <div>
          <!-- candidates in pipeline -->
          <p class="text-sm text-gray-500">100</p>
        </div>
      </template>
      <template v-slot:[`status`]="{ item }">
        <div>
          <chip
            :color="item.jobOrderStatus.color.hex"
            :text="item.jobOrderStatus.statusName"
          ></chip>
        </div>
      </template>
    </data-table>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DataTable from "../components/DataTable.vue";
import { JOB_ORDERS } from "../queries/joborder";
import { parseDate } from "../utils/helpers";
import Chip from "../components/widgets/Chip.vue";

export default defineComponent({
  components: { DataTable, Chip },
  async created() {
    await this.getJobOrders();
  },
  methods: {
    parseDate,
    async getJobOrders() {
      const { data } = await this.$apollo.query({
        query: JOB_ORDERS,
        variables: {
          page: this.page,
          pageSize: this.pageSize,
        },
      });
      if (data) {
        this.joborders = JSON.parse(JSON.stringify(data.jobOrders.objects));
        this.total = data.jobOrders.total;
        this.page = data.jobOrders.page;
        this.pages = data.jobOrders.pages;
        this.hasPrev = data.jobOrders.hasPrev;
        this.hasNext = data.jobOrders.hasNext;
        this.setDropt();
      }
    },
    setDropt() {
      let fin = [];
      for (let i = 0; i < this.total; i++) {
        fin.push(`${i + 1}/${this.total}`);
      }
      console.clear();
      console.warn(this.total);
      this.dropts = fin;
    },
    singleSelected(e: any) {
      console.log(e);
    },
    allChecked(e: any) {
      console.log(`All Checked, ${e}`);
    },
    async prev() {
      this.page--;
      await this.getJobOrders();
    },
    async next() {
      this.page++;
      await this.getJobOrders();
    },
  },
  data: () => ({
    total: 0,
    pages: 1,
    hasNext: false,
    hasPrev: false,
    page: 1,
    pageSize: 2,
    dropts: [] as any,
    emptyMesasge: "You don't have any job orders yet.",
    headers: [
      { value: "title", label: "Title" },
      { value: "organization", label: "Organization" },
      { value: "updated", label: "Updated" },
      { value: "c", label: "C" },
      { value: "s", label: "S" },
      { value: "status", label: "Status" },
    ],
    joborders: [],
  }),
});
</script>
