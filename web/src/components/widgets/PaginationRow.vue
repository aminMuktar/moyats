<template>
  <div class="flex justify-end">
    <button
      @click="$emit('prev')"
      class="p-1 h-11 border-2 hover:bg-gray-200 border-gray-200 m-1"
      :class="{ 'cursor-not-allowed text-gray-300': !hasPrev }"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-5 w-5"
        viewBox="0 0 20 20"
        fill="currentColor"
      >
        <path
          fill-rule="evenodd"
          d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z"
          clip-rule="evenodd"
        />
      </svg>
    </button>
    <select
      class="
        block
        appearance-none
        cursor-pointer
        hover:bg-gray-200
        bg-white
        border border-gray-200
        px-2
        py-2
        w-12
        text-center
        h-11
        my-1
        rounded
        shadow
        leading-tight
        focus:outline-none focus:shadow-outline
      "
    >
      <option v-for="(opt, x) in dropts" :key="x">{{ opt }}</option>
    </select>
    <button
      @click="$emit('next')"
      class="p-1 h-11 border-2 hover:bg-gray-200 border-gray-200 m-1"
      :class="{ 'cursor-not-allowed text-gray-300': !hasNext }"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-5 w-5"
        viewBox="0 0 20 20"
        fill="currentColor"
      >
        <path
          fill-rule="evenodd"
          d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
          clip-rule="evenodd"
        />
      </svg>
    </button>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  props: ["page", "pages", "pageSize", "total", "hasNext", "hasPrev", "dropts"],
  created(){},
  methods: {},
});
</script>
