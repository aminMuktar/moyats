<template>
  <header
    class="
      flex
      items-center
      border-gray-200
      justify-between
      px-3
      py-4
      h-16
      bg-white
      border-t-2
      border-b-1
      z-50
      border-b-2
    "
  >
    <div class="flex items-center">
      <div
        class="relative mx-4 lg:mx-0"
        v-if="$route.path === '/company-management'"
      >
        <a href="/">
          <div class="flex items-start mx-7 mt-5 gap-1 mb-5">
            <img src="../assets/icon.png" class="w-8" alt="" />
            <span class="mx-2 text-2xl font-semibold text-black font-sans"
              >Moyats</span
            >
          </div>
        </a>
      </div>
      <button
        v-if="$route.path !== '/company-management'"
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
      <entity-title-widget></entity-title-widget>
    </div>
    <div class="flex items-center">
      <quick-action-button v-if="$route.path !== '/company-management'" />
      <notificaiton-dropdown />
      <account-dropdown />
    </div>
  </header>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import AccountDropdown from "../components/AccountDropdown.vue";
import NotificaitonDropdown from "../components/NotificationDropdown.vue";
import QuickActionButton from "./QuickActionButton.vue";
import EntityTitleWidget from "./widgets/EntityTitleWidget.vue";

export default defineComponent({
  components: {
    NotificaitonDropdown,
    AccountDropdown,
    QuickActionButton,
    EntityTitleWidget,
  },
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
