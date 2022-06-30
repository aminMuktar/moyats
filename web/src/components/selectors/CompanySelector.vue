<template>
  <div class="flex col-span-2 w-full p-2 z-auto">
    <div class="w-52" v-if="showHeader">
      <span class="m-3">Company* </span>
    </div>
    <div>
      <pill :clearable="true" v-if="selectedVal" :text="selectedVal.name" @clear="clear"></pill>
      <div v-else>
        <div class="relative overflow-hidden">
          <input
            id="email"
            @keyup="runSearch"
            v-model="value"
            class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
            autocomplete="off"
            placeholder="search for companies"
          />
        </div>
        <div
          v-show="showOptions && data.length"
          class="
            relative
            w-full
            max-h-52
            overflow-y-scroll
            z-50
            bg-white
            border border-gray-300
            mt-1
            max-height-48
            overflow-hidden
            rounded-md
            shadow-md
          "
        >
          <ul class="py-1">
            <li
              :key="index"
              v-for="(value, index) in data"
              @click="setInput(value)"
              class="px-3 py-2 cursor-pointer hover:bg-gray-200"
            >
              {{ value.name }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import Autocomplete from "../../components/Autocomplete.vue";
import { searchCompany } from "../../services";
import Pill from "../pill.vue";

export default defineComponent({
  setup() {},
  props: ["showHeader"],
  components: {
    Autocomplete,
    Pill,
  },
  data: () => ({
    selectedVal: null as any,
    value: "",
    showOptions: false,
    data: [] as any,
  }),
  async created() {
    this.data = await this.searchCompanyFilter();
    this.showOptions = false;
  },
  methods: {
    async runSearch() {
      this.showOptions = true;
      this.data = await this.searchCompanyFilter();
    },
    clear() {
      this.selectedVal = null;
      this.value = "";
      this.$emit("cleared");
    },
    async searchCompanyFilter() {
      if (this.value) {
        const { data, errors } = await searchCompany(this.value);
        if (!errors) {
          return data.searchCompany;
        } else {
          return [] as any;
        }
      } else {
        return [] as any;
      }
    },
    async setInput(value) {
      this.value = value.name;
      this.showOptions = false;
      this.selectedVal = value;
      this.$emit("itemClicked", value);
    },
  },
});
</script>
