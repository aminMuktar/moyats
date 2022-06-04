<template>
  <div>
    <data-table
      empty-message="you don't have any contacts yet"
      :items="contacts"
      :headers="headers"
      @checkedAll="allChecked"
      @selected="singleSelected"
    >
      <template v-slot:[`name`]="{ item }">
        <div>
          <p class="text-sm text-gray-500">
            {{ item.firstName }} {{ item.lastName }}
          </p>
        </div>
      </template>
      <template v-slot:[`company`]="{ item }">
        <div>
          <p class="text-sm text-gray-500">
            {{ item.company.name }}
          </p>
        </div>
      </template>
      <template v-slot:[`status`]="{ item }">
        <div>
          <chip :color="item.status.color.hex" :text="item.status.name"></chip>
        </div>
      </template>
      <template v-slot:[`companyStatus`]="{ item }">
        <div>
          <chip
            :color="item.company.companyStatus.color.hex"
            :text="item.company.companyStatus.name"
          ></chip>
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
    </data-table>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DataTable from "../components/DataTable.vue";
import { CONTACTS } from "../queries/contact";
import { parseDate } from "../utils/helpers";
import Chip from "../components/widgets/Chip.vue";

export default defineComponent({
  components: { DataTable, Chip },
  async created() {
    await this.fetchContacts();
  },
  methods: {
    parseDate,
    async fetchContacts() {
      const { data } = await this.$apollo.query({
        query: CONTACTS,
        variables: {
          page: this.page,
          pageSize: this.pageSize,
        },
      });
      if (data) {
        this.contacts = JSON.parse(JSON.stringify(data.contacts.objects));
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
      { value: "company", label: "Company" },
      { value: "updated", label: "Updated" },
      { value: "status", label: "Status" },
      { value: "companyStatus", label: "Company Status" },
    ],
    contacts: [],
  }),
});
</script>
