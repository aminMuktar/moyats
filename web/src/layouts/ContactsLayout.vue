<template>
  <div>
    <data-table
      :items="activities"
      :headers="headers"
      @checkedAll="allChecked"
      @selected="singleSelected"
    >
      <template v-slot:[`${h}`]="{ item }" v-for="(h, ix) in headers" :role="h">
        <div :key="ix">
          <p class="text-sm text-gray-500">{{ item[h] }}</p>
        </div>
      </template>
    </data-table>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DataTable from "../components/DataTable.vue";
interface Activities {
  Date: any;
  Name: any;
  Regarding: any;
  ActivityType: any;
  Notes: any;
  EnteredBy: any;
  Source: any;
  JobOrder: any;
  Company: any;
  checked: boolean;
}
export default defineComponent({
  components: { DataTable },
  methods: {
    singleSelected(e: any) {
      console.log(e);
    },
    allChecked(e: any) {
      console.log(`All Checked, ${e}`);
    },
  },
  data: () => ({
    headers: [
      "Date",
      "Name",
      "Regarding",
      "ActivityType",
      "Notes",
      "Source",
      "JobOrder",
      "EnteredBy",
      "Company",
    ],
    activities: <Activities[]>[
      {
        Date: "Mon 12, 2021",
        Name: "Activity Name",
        Regarding: "Regarding something",
        ActivityType: "Some Type",
        Notes: "Here goes some notes",
        EnteredBy: "Amen Abe",
        Source: "Email",
        JobOrder: "Mechanic",
        Company: "Moyats Corp",
      },
      {
        Date: "Mon 12, 2021",
        Name: "Activity Name",
        Regarding: "Regarding something",
        ActivityType: "Some Type",
        Notes: "Here goes some notes",
        EnteredBy: "Amen Abe",
        Source: "Email",
        JobOrder: "Mechanic",
        Company: "Moyats ORg",
      },
      {
        Date: "Mon 12, 2021",
        Name: "Activity Name",
        Regarding: "Regarding something",
        ActivityType: "Some Type",
        Notes: "Here goes some notes",
        EnteredBy: "Amen Abe",
        Source: "Email",
        JobOrder: "Mechanic",
        Company: "Moyats Nation",
      },
      {
        Date: "Mon 12, 2021",
        Name: "Activity Name",
        Regarding: "Regarding something",
        ActivityType: "Some Type",
        Notes: "Here goes some notes",
        EnteredBy: "Amen Abe",
        Source: "Email",
        JobOrder: "Mechanic",
        Company: "Moyats Nation",
      },
      {
        Date: "Mon 12, 2021",
        Name: "Activity Name",
        Regarding: "Regarding something",
        ActivityType: "Some Type",
        Notes: "Here goes some notes",
        EnteredBy: "Amen Abe",
        Source: "Email",
        JobOrder: "Mechanic",
        Company: "Moyats Nation",
      },
      {
        Date: "Mon 12, 2021",
        Name: "Activity Name",
        Regarding: "Regarding something",
        ActivityType: "Some Type",
        Notes: "Here goes some notes",
        EnteredBy: "Amen Abe",
        Source: "Email",
        JobOrder: "Mechanic",
        Company: "Moyats Nation",
      },
    ],
  }),
});
</script>
