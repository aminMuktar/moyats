<template>
  <div>
    <table class="w-full text-sm text-left text-gray-500">
      <thead class="text-xs uppercase bg-gray-50">
        <tr>
          <th scope="col" class="p-4">
            <div class="flex items-center">
              <input
                @change="tableSelected"
                v-model="selectAll"
                id="checkbox-all-search"
                type="checkbox"
                class="
                  w-4
                  h-4
                  text-blue-600
                  bg-gray-100
                  border-gray-300
                  rounded
                  focus:ring-blue-500
                  dark:focus:ring-blue-600 dark:ring-offset-gray-800
                  focus:ring-2
                  dark:bg-gray-700 dark:border-gray-600
                "
              />
              <label for="checkbox-all-search" class="sr-only">checkbox</label>
            </div>
          </th>
          <th
            scope="col"
            class="px-6 py-3"
            v-for="(head, idx) in headers"
            :key="idx"
            v-text="head"
          ></th>
        </tr>
      </thead>
      <tbody>
        <tr
          class="bg-white border-b hover:bg-gray-50"
          v-for="(item, idx) in items"
          :key="idx"
        >
          <td class="w-4 p-4">
            <div class="flex items-center">
              <input
                v-model="item.checked"
                id="checkbox-table-search-1"
                type="checkbox"
                class="
                  w-4
                  h-4
                  text-blue-600
                  bg-gray-100
                  border-gray-300
                  rounded
                  focus:ring-blue-500
                  dark:focus:ring-blue-600 dark:ring-offset-gray-800
                  focus:ring-2
                  dark:bg-gray-700 dark:border-gray-600
                "
              />
              <label for="checkbox-table-search-1" class="sr-only"
                >checkbox</label
              >
            </div>
          </td>
          <th
            v-for="(k, ix) in getkeys(item)"
            :key="ix"
            scope="row"
            class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap"
          >
            <slot :name="k" v-bind="{ item }"> </slot>
          </th>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  props: ["items", "headers"],
  methods: {
    getkeys(item: any) {
      return Object.keys(item);
    },
    tableSelected(e: any) {
      this.items.forEach((e: any) => (e.checked = this.selectAll));
      this.selectedTable = true;
    },
  },
  data: () => ({
    selectAll: false,
    selectedTable: false,
  }),
});
</script>
