<template>
  <div class="flex col-span-2 w-full p-2 z-auto">
    <div class="w-52">
      <span class="m-3">Recruiter* </span>
    </div>
    <div>
      <div class="bg-blue-400 rounded-md" v-if="selectedVal">
        <div class="flex">
          <a
            class="
              h-full
              w-full
              flex
              justify-center
              items-center
              p-2
              text-gray-700
              font-semibold
            "
          >
            {{ selectedVal.firstName }} {{ selectedVal.lastName }}
          </a>
          <button type="button" class="gap-2" @click="clear">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5 mx-2"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="2"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>
      </div>
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
              {{ value.firstName }} {{ value.lastName }}
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
import { searchRecruiter } from "../../services";

export default defineComponent({
  setup() {},
  components: {
    Autocomplete,
  },
  data: () => ({
    selectedVal: null as any,
    value: "",
    showOptions: false,
    data: [] as any,
  }),
  async created() {
    this.data = await this.searchFilter();
    this.showOptions = false;
  },
  methods: {
    async runSearch() {
      this.showOptions = true;
      this.data = await this.searchFilter();
    },
    clear() {
      this.selectedVal = null;
      this.value = "";
    },
    async searchFilter() {
      if (this.value) {
        const { data, errors } = await searchRecruiter(this.value);
        if (!errors) {
          return data.searchRecruiter;
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
    },
  },
});
</script>
