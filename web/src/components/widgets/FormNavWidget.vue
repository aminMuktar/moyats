<template>
  <div class="flex right-0 z-50 mr-0 mt-1 absolute w-1/2 h-full justify-end">
    <button
      class="w-10 h-10 bg-white rounded flex justify-center items-center"
      @click="sliderActivator()"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-5 w-5"
        viewBox="0 0 20 20"
        fill="currentColor"
      >
        <path
          fill-rule="evenodd"
          d="M6 6V5a3 3 0 013-3h2a3 3 0 013 3v1h2a2 2 0 012 2v3.57A22.952 22.952 0 0110 13a22.95 22.95 0 01-8-1.43V8a2 2 0 012-2h2zm2-1a1 1 0 011-1h2a1 1 0 011 1v1H8V5zm1 5a1 1 0 011-1h.01a1 1 0 110 2H10a1 1 0 01-1-1z"
          clip-rule="evenodd"
        />
        <path
          d="M2 13.692V16a2 2 0 002 2h12a2 2 0 002-2v-2.308A24.974 24.974 0 0110 15c-2.796 0-5.487-.46-8-1.308z"
        />
      </svg>
    </button>
    <div
      class="w-full h-full bg-white shadow-lg shadow-black-500/50"
      v-if="display"
    ></div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  data() {
    return {
      display: false,
    };
  },
  methods: {
    sliderActivator() {
      console.log("hello");
      !this.display ? (this.display = true) : (this.display = false);
    },
  },
});
</script>
