<template>
  <menu-drop-down :active="active" width="w-96">
    <template v-slot:button>
      <button
        @click="active = !active"
        class="mx-2 bg-black text-white border-2 border-gray-500 rounded-full"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-7 w-7 p-1"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path
            d="M10 2a6 6 0 00-6 6v3.586l-.707.707A1 1 0 004 14h12a1 1 0 00.707-1.707L16 11.586V8a6 6 0 00-6-6zM10 18a3 3 0 01-3-3h6a3 3 0 01-3 3z"
          />
        </svg>
      </button>
    </template>
    <template v-slot:list>
      <div class="py-1">
        <ul>
          <li class="p-5 hover:bg-gray-100 cursor-pointer">
            <div>
              <p class="text-md font-bold">
                Here is some long notification text long long
              </p>
              <p>some infor about this notification</p>
            </div>
          </li>
        </ul>
      </div>
    </template>
  </menu-drop-down>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import MenuDropDown from "./MenuDropDown.vue";

export default defineComponent({
  components: { MenuDropDown },
  setup() {},
  data: () => ({
    active: false,
    selected: false,
  }),
});
</script>

