<template>
  <Menu as="div" class="relative inline-block text-left">
    <div>
      <slot></slot>
    </div>

    <transition
      v-show="active"
      enter-active-class="transition ease-out duration-100"
      enter-from-class="transform opacity-0 scale-95"
      enter-to-class="transform opacity-100 scale-100"
      leave-active-class="transition ease-in duration-75"
      leave-from-class="transform opacity-100 scale-100"
      leave-to-class="transform opacity-0 scale-95"
    >
      <div
        class="
          origin-top-right
          absolute
          right-0
          w-56
          rounded-md
          shadow-lg
          bg-white
          ring-1 ring-black ring-opacity-5
          focus:outline-none
        "
      >
        <div class="py-1">
          <a
            href="#"
            :class="[
              'hover:bg-gray-100 cursor-pointer',
              selected ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
              'block px-4 py-2 text-sm',
            ]"
            >Account settings</a
          >
          <a
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
      </div>
    </transition>
  </Menu>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { LOGOUT } from "../queries/auth";

export default defineComponent({
  props: {
    active: Boolean,
  },
  data: () => ({
    selected: false,
  }),
  methods: {
    async logout() {
      const { data } = await this.$apollo.mutate({
        mutation: LOGOUT,
      });
      if (data) {
        this.$store.commit("clearToken");
        location.assign("/login");
      }
    },
  },
});
</script>
