<template>
  <div>
    <data-table
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
        <div>
          <p class="text-sm text-gray-500" v-text="0"></p>
        </div>
      </template>
      <template v-slot:[`o`]="{ item }">
        <div>
          <p class="text-sm text-gray-500" v-text="0"></p>
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
        <div>
          <chip
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
import { formAddress, parseDate } from "../utils/helpers";

export default defineComponent({
  components: { DataTable, Chip },
  async created() {
    await this.getCompanies();
  },
  methods: {
    parseDate,
    formAddress,
    async getCompanies() {
      const { data } = await this.$apollo.query({
        query: COMPANIES,
        variables: {
          page: this.page,
          pageSize: this.pageSize,
        },
      });
      if (data) {
        this.companies = JSON.parse(JSON.stringify(data.companies.objects));
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
    page: 1,
    pageSize: 1,
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
