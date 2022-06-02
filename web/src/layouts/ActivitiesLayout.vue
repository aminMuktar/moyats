<template>
  <div>
    <data-table
      :items="activities"
      :headers="headers"
      @checkedAll="allChecked"
      @selected="singleSelected"
    >
      <template v-slot:[`date`]="{ item }">
        <div>
          <p v-text="parseDate(item.createdAt)"></p>
        </div>
      </template>
      <template v-slot:[`name`]="{ item }">
        <div>
          <p>
            {{ item.user.firstName }}
            {{ item.user.firstName }}
          </p>
        </div>
      </template>
      <template v-slot:[`regarding`]="{ item }">
        <div>
          <p
            v-if="item.activityType == 'OR'"
            v-text="item.contentObject.name"
          ></p>
          <p v-else-if="item.activityType == 'AC'">
            {{ item.contentObject.first_name }}
            {{ item.contentObject.last_name }}
          </p>
        </div>
      </template>
      <template v-slot:[`type`]="{ item }">
        <div>
          <p v-text="item.activityType"></p>
        </div>
      </template>
    </data-table>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DataTable from "../components/DataTable.vue";
import { ACTIVITIES } from "../queries/auth";
import { parseDate } from "../utils/helpers";

export default defineComponent({
  components: { DataTable },
  async created() {
    await this.fetchActivities();
  },
  methods: {
    singleSelected(e: any) {
      console.log(e);
    },
    parseDate,
    allChecked(e: any) {
      console.log(`All Checked, ${e}`);
    },
    async fetchActivities() {
      const { data } = await this.$apollo.query({
        query: ACTIVITIES,
        fetchPolicy: "network-only",
        variables: {
          page: this.page,
          pageSize: this.pageSize,
        },
      });
      if (data) {
        const objects = data.activities.objects;
        this.activities = objects;
      }
    },
  },
  data: () => ({
    page: 1,
    pageSize: 2,
    headers: [
      { value: "date", label: "Date" },
      { value: "name", label: "Name" },
      { value: "regarding", label: "Regarding" },
      { value: "type", label: "Type" },
      { value: "by", lablel: "By" },
    ],
    activities: [] as any,
  }),
});
</script>
