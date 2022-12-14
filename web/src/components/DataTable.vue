<template>
  <div
    class="overflow-x-auto bg-white rounded-lg shadow overflow-y-auto relative"
  >
    <div
      class="flex flex-col rounded-lg overflow-hidden bg-white shadow relative"
    >
      <!-- loading overlay -->

      <div
        v-if="loadingState"
        class="
          absolute
          bg-white bg-opacity-60
          z-10
          h-full
          w-full
          flex
          items-center
          justify-center
        "
      >
        <spinner></spinner>
      </div>
      <!-- end of loader -->
      <table-filter-section @searched="searched"></table-filter-section>
      <p
        class="text-center py-5 text-gray-500"
        v-if="items.length === 0 && !loadingState"
        v-text="emptyMessage"
      ></p>
      <table
        v-else
        class="
          border-collapse
          table-auto
          w-full
          whitespace-no-wrap
          bg-white
          table-striped
          relative
        "
      >
        <thead class="text-xs text-left uppercase bg-gray-50">
          <tr>
            <th scope="col" class="p-4">
              <div class="flex items-start">
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
                <label for="checkbox-all-search" class="sr-only"
                  >checkbox</label
                >
              </div>
            </th>
            <th
              scope="col"
              class="px-2 py-3"
              v-for="(head, idx) in headers"
              :key="idx"
              v-text="head.label"
            ></th>
          </tr>
        </thead>
        <tbody class="text-left">
          <tr
            :class="{ 'bg-gray-200': item.checked }"
            class="border-b hover:bg-gray-200"
            v-for="(item, idx) in items"
            :key="idx"
          >
            <td class="w-4 p-4">
              <div class="flex items-center">
                <input
                  @change="singleItemSelected"
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
              v-for="(k, ix) in headers"
              :key="ix"
              scope="row"
              class="px-2 py-4 font-normal text-gray-900 whitespace-nowrap"
            >
              <slot :name="k.value" v-bind="{ item }"> </slot>
            </th>
          </tr>
        </tbody>
      </table>
      <pagination-row
        @prev="$emit('prev')"
        @next="$emit('next')"
        :page="page"
        :pageSize="pageSize"
        :pages="pages"
        :total="total"
        :hasNext="hasNext"
        :hasPrev="hasPrev"
        :dropts="dropts"
      ></pagination-row>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import PaginationRow from "./widgets/PaginationRow.vue";
import TableFilterSection from "./widgets/TableFilterSection.vue";
import Spinner from "./Spinner.vue";

export default defineComponent({
  components: {
    PaginationRow,
    TableFilterSection,
    Spinner,
  },
  props: [
    "items",
    "total",
    "page",
    "pageSize",
    "pages",
    "hasNext",
    "hasPrev",
    "dropts",
    "headers",
    "emptyMessage",
    "loadingState",
  ],
  methods: {
    getkeys(item: any) {
      return Object.keys(item).filter((x: any) => x !== "checked");
    },
    searched(e) {
      this.$emit("searched", e);
    },
    singleItemSelected() {
      this.$emit(
        "selected",
        this.items.filter((e: any) => e.checked === true)
      );
    },
    tableSelected(e: any) {
      this.$emit("checkedAll", this.selectAll);
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
