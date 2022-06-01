<template>
  <header
    class="flex items-center border-t-4 border-gray-600 justify-between px-6 py-4 h-16 bg-white border-b-1"
  >
    <div class="flex items-center">
      <button
        @click="isOpen = true"
        class="text-gray-500 focus:outline-none lg:hidden"
      >
        <svg
          class="w-6 h-6"
          viewBox="0 0 24 24"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M4 6H20M4 12H20M4 18H11"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          />
        </svg>
      </button>
      <div class="relative mx-4 lg:mx-0">
        <button class="text-gray-800 rounded-full hover:bg-gray-300 p-2 mx-2">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            stroke-width="2"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M17 14v6m-3-3h6M6 10h2a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v2a2 2 0 002 2zm10 0h2a2 2 0 002-2V6a2 2 0 00-2-2h-2a2 2 0 00-2 2v2a2 2 0 002 2zM6 20h2a2 2 0 002-2v-2a2 2 0 00-2-2H6a2 2 0 00-2 2v2a2 2 0 002 2z"
            />
          </svg>
        </button>
      </div>
    </div>

    <div class="flex items-center">
      <button
        v-if="jobOrderButton"
        class="flex m-10 justify-between bg-slate-400 p-3 w-36 rounded-full"
      >
        <div class="bg-gray-700 rounded-full ml-2">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6"
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
        </div>
        <div>Job Order</div>
      </button>
      <notificaiton-dropdown />
      <account-dropdown />
    </div>
  </header>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import AccountDropdown from "../components/AccountDropdown.vue";
import NotificaitonDropdown from "../components/NotificationDropdown.vue";

export default defineComponent({
  components: { NotificaitonDropdown, AccountDropdown },
  data: () => ({
    isOpen: false,
    dropdownOpen: false,
    jobOrderButton: window.location.pathname === "/joborders" ? true : false,
  }),
  created() {
    console.log(window.location.pathname);
  },
});
</script>
