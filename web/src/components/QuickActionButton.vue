<template>
  <div>
    <button
      class="flex m-10 justify-between bg-white hover:bg-gray-100 hover:shadow-sm hover:scale-105 border-2 p-2 rounded-full"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-6 w-6 rounded-full bg-black text-white"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
        stroke-width="2"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M12 6v6m0 0v6m0-6h6m-6 0H6"
        />
      </svg>
      <p class="px-2 tracking-tight leading-3 pt-1">Job Order</p>
    </button>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  setup() {},
});
</script>
