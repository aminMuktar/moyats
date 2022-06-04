<template>
  <div>
    <data-table
      empty-message="you don't have any candidates yet"
      :items="candidates"
      :headers="headers"
      @checkedAll="allChecked"
      @selected="singleSelected"
    >
      <template v-slot:[`name`]="{ item }">
        <div>
          <p class="text-sm text-gray-500">
            {{ item.candidateProfile.firstName }}
            {{ item.candidateProfile.lastName }}
          </p>
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
            v-text="parseDate(item.updated)"
          ></p>
        </div>
      </template>
    </data-table>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DataTable from "../components/DataTable.vue";
import { CANDIDATES } from "../queries/candidates";
import { formAddress, parseDate } from "../utils/helpers";

export default defineComponent({
  components: { DataTable },
  methods: {
    parseDate,
    formAddress,
    singleSelected(e: any) {
      console.log(e);
    },
    allChecked(e: any) {
      console.log(`All Checked, ${e}`);
    },
    async getCandidates() {
      const { data } = await this.$apollo.query({
        query: CANDIDATES,
        variables: {
          page: this.page,
          pageSize: this.pageSize,
        },
      });
      if (data) {
        this.candidates = JSON.parse(JSON.stringify(data.candidtes.objects));
      }
    },
  },
  async created() {
    await this.getCandidates();
  },
  data: () => ({
    page: 1,
    pageSize: 1,
    headers: [
      { value: "name", label: "name" },
      { value: "location", label: "Location" },
      { value: "updated", label: "Updated" },
    ],
    candidates: [],
  }),
});
</script>
