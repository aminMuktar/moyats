<template>
  <header
    class="
      flex
      items-center
      border-t-4 border-gray-600
      justify-between
      px-6
      py-4
      h-14
      bg-gray-100
      border-b-1
    "
  >
    <div class="flex items-center">
      <div class="relative mx-4 lg:mx-0">
        <div class="flex items-start mx-7 mt-5 gap-1 mb-3">
          <img src="../assets/icon.png" class="w-7 mt-1" alt="" />
          <span class="mx-2 text-2xl font-semibold text-black font-sans"
            >Moyats</span
          >
        </div>
      </div>
    </div>

    <div class="flex items-center">
      <account-dropdown empty />
    </div>
  </header>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import AccountDropdown from "../components/AccountDropdown.vue";

export default defineComponent({
  components: { AccountDropdown },
  data: () => ({
    isOpen: false,
    dropdownOpen: false,
  }),
});
</script>
