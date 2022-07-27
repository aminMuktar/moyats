<template>
  <div class="flex flex-row justify-between">
    <div class="flex flex-row w-full">
      <input
        class="
          w-2/5
          py-2
          m-2
          pl-3
          pr-16
          text-sm
          rounded-md
          border-2 border-gray-200
        "
        v-model="query"
        id="search"
        type="search"
        placeholder="Search Items"
      />
      <button
        class="border-2 my-2 px-2 bg-black text-white rounded-md"
        @click="searched"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-8 w-8 py-2"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          stroke-width="2"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
          />
        </svg>
      </button>
    </div>
    <div class="mx-2 flex flex-row gap-1">
      <div class="flex my-2 rounded-l flex-row border border-gray-200">
        <select
          class="
            block
            hover:bg-gray-200
            bg-white
            appearance-none
            cursor-pointer
            px-2
            py-2
            w-32
            text-center
            rounded-l
            leading-tight
            focus:outline-none focus:shadow-outline
          "
        >
          <option v-for="(opt, x) in items" :key="x">{{ opt }}</option>
        </select>
        <button>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              fill-rule="evenodd"
              d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
              clip-rule="evenodd"
            />
          </svg>
        </button>
      </div>
      <div class="flex my-2 rounded-l flex-row border border-gray-200">
        <select
          class="
            block
            hover:bg-gray-200
            bg-white
            appearance-none
            cursor-pointer
            px-2
            py-2
            w-32
            text-center
            rounded-l
            leading-tight
            focus:outline-none focus:shadow-outline
          "
        >
          <option v-for="(opt, x) in items" :key="x">{{ opt }}</option>
        </select>
        <button>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              fill-rule="evenodd"
              d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
              clip-rule="evenodd"
            />
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  setup() {},
  data: () => ({
    query: "",
    items: ["First Filter", "Second Filter", "Third Filter", "Fourth Filter"],
  }),
  methods: {
    searched() {
      this.$emit("searched", this.query);
    },
  },
});
</script>
