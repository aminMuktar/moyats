<template>
  <div>
    <button
      class="
        flex
        justify-between
        bg-white
        hover:bg-gray-100 hover:shadow-sm hover:scale-105
        border-2
        p-1
        rounded-full
      "
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
      <p
        class="px-2 tracking-tight leading-3 pt-1"
        @click="openSlider"
        v-if="$store.state.core.activeSlideWindow == 'joborders'"
      >
        Job Order
      </p>
      <p
        @click="openSlider"
        class="px-2 tracking-tight leading-3 pt-1"
        v-if="$store.state.core.activeSlideWindow == 'candidates'"
      >
        Candidate
      </p>
      <p
        @click="openSlider"
        class="px-2 tracking-tight leading-3 pt-1"
        v-if="$store.state.core.activeSlideWindow == 'contacts'"
      >
        Contact
      </p>
      <p
        @click="openSlider"
        class="px-2 tracking-tight leading-3 pt-1"
        v-if="$store.state.core.activeSlideWindow == 'companies'"
      >
        Company
      </p>
    </button>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  setup() {},
  data: () => ({
    btnTitle: "",
  }),
  created() {
    const activeWindow = this.$store.state.core.activeSlideWindow;
    if (activeWindow === "joborders") {
      this.btnTitle = "Job Order";
    } else if (activeWindow === "candidates") {
      this.btnTitle = "Candidate";
    } else if (activeWindow === "companies") {
      this.btnTitle = "Company";
    } else if (activeWindow === "contacts") {
      this.btnTitle = "Contact";
    }
  },
  methods: {
    openSlider() {
      this.$store.commit("setActivateSlider", true);
    },
  },
});
</script>
