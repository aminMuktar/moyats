<template>
  <div>
    <div class="p-4">
      <label for="table-search" class="sr-only">Search</label>
      <div class="relative mt-1">
        <div
          class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none"
        >
          <svg
            class="w-5 h-5 text-gray-500 dark:text-gray-400"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
              clip-rule="evenodd"
            ></path>
          </svg>
        </div>
        <input
          type="text"
          id="table-search"
          class="bg-gray-50 border border-gray-300 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-80 pl-10 p-2.5 dark:border-gray-300 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-400"
          placeholder="Search for items"
        />
      </div>
    </div>
    <table class="w-full text-sm text-left text-gray-500">
      <thead class="text-xs uppercase bg-gray-50">
        <tr>
          <th scope="col" class="p-4">
            <div class="flex items-center">
              <input
                id="checkbox-all-search"
                type="checkbox"
                class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
              />
              <label for="checkbox-all-search" class="sr-only">checkbox</label>
            </div>
          </th>
          <th
            scope="col"
            class="px-6 py-3"
            v-for="(i, j) in tableTitles()"
            :key="j"
            v-text="i"
          ></th>
        </tr>
      </thead>
      <tbody>
        <tr
          class="bg-white border-b hover:bg-gray-50"
          v-for="(i, j) in activities"
          :key="j"
        >
          <td class="w-4 p-4">
            <div class="flex items-center">
              <input
                id="checkbox-table-search-1"
                type="checkbox"
                class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
              />
              <label for="checkbox-table-search-1" class="sr-only"
                >checkbox</label
              >
            </div>
          </td>
          <th
            scope="row"
            class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap"
            v-text="i.Date"
          ></th>
          <td class="px-6 py-4" v-text="i.Name"></td>
          <td class="px-6 py-4" v-text="i.Regarding"></td>
          <td class="px-6 py-4" v-text="i.ActivityType"></td>
          <td class="px-6 py-4" v-text="i.Notes"></td>
          <td class="px-6 py-4" v-text="i.Source"></td>
          <td class="px-6 py-4" v-text="i.JobOrder"></td>
          <td class="px-6 py-4" v-text="i.EnteredBy"></td>
          <td class="px-6 py-4" v-text="i.Company"></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

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
}

// const keyofprops = keys<Activities>();

export default defineComponent({
  created() {
    // this.Titler();
  },
  data() {
    return {
      tableTitles: () => {
        let arr: (keyof Activities)[] = [
          "Date",
          "Name",
          "Regarding",
          "ActivityType",
          "Notes",
          "Source",
          "JobOrder",
          "EnteredBy",
          "Company",
        ];
        return arr;
      },
      activities: <Activities[]>[
        {
          Date: "2022-1-1:10:00 am",
          Name: "Amar",
          Regarding: "Something",
          Notes: "Some Notes",
          EnteredBy: "Someone",
          Source: "From Somewhere",
          JobOrder: "Just Something",
          Company: "Something",
        },
        {
          Date: "2022-1-1:10:00 am",
          Name: "Amar",
          Regarding: "Something",
          Notes: "Some Notes",
          EnteredBy: "Someone",
          Source: "From Somewhere",
          JobOrder: "Just Something",
          Company: "Something",
        },
        {
          Date: "2022-1-1:10:00 am",
          Name: "Amar",
          Regarding: "Something",
          Notes: "Some Notes",
          EnteredBy: "Someone",
          Source: "From Somewhere",
          JobOrder: "Just Something",
          Company: "Something",
        },
      ],
    };
  },

  methods: {
    // Titler() {
    //   this.tableTitles().map((e) => {
    //     console.log(e);
    //   });
    // },
  },
});
</script>
