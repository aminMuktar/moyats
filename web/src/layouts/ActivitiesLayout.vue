<template>
  <div>
    <data-table :items="activities" :headers="headers">
      <template
        v-slot:[`${h}`]="{ item }"
        v-for="h in headers"
        :role="h"
      >
        {{ item[h] }}
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
    ],
  }),
});
</script>
