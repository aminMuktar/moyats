<template>
  <menu-drop-down :active="active" width="w-52">
    <template v-slot:button>
      <button
        @click="active = !active"
        class="bg-black text-white border-2 border-gray-500 rounded-full"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-7 w-7 p-1"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path
            fill-rule="evenodd"
            d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-6-3a2 2 0 11-4 0 2 2 0 014 0zm-2 4a5 5 0 00-4.546 2.916A5.986 5.986 0 0010 16a5.986 5.986 0 004.546-2.084A5 5 0 0010 11z"
            clip-rule="evenodd"
          />
        </svg>
      </button>
    </template>
    <template v-slot:list>
      <div class="py-1">
        <a
          v-if="!empty"
          href="#"
          :class="[
            'hover:bg-gray-100 cursor-pointer',
            selected ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
            'block px-4 py-2 text-sm',
          ]"
          >Account settings</a
        >
        <a
          v-if="!empty"
          href="#"
          :class="[
            'hover:bg-gray-100 cursor-pointer',
            selected ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
            'block px-4 py-2 text-sm',
          ]"
          >Support</a
        >
        <a
          @click="logout"
          :class="[
            'hover:bg-gray-100 cursor-pointer',
            selected ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
            'block px-4 py-2 text-sm',
          ]"
          >Logout</a
        >
      </div>
    </template>
  </menu-drop-down>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { LOGOUT } from "../queries/auth";
import MenuDropDown from "./MenuDropDown.vue";

export default defineComponent({
  components: { MenuDropDown },
  setup() {},
  props: {
    empty: Boolean,
  },
  data: () => ({
    active: false,
    selected: false,
  }),
  methods: {
    logout() {
      this.$apollo
        .mutate({
          mutation: LOGOUT,
        })
        .then(({ data }) => {
          if (data) {
            this.$store.commit("clearToken");
            location.assign("/login");
          }
        });
    },
  },
});
</script>

