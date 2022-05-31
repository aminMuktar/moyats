<template>
  <Menu as="div" class="relative inline-block text-left">
    <div>
      <slot name="button"></slot>
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
        :class="[width]"
        class="
          origin-top-right
          absolute
          right-0
          rounded-md
          shadow-lg
          z-10
          bg-white
          ring-1 ring-black ring-opacity-5
          focus:outline-none
        "
      >
        <slot name="list"></slot>
      </div>
    </transition>
  </Menu>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { LOGOUT } from "../queries/auth";

export default defineComponent({
  props: {
    width: String,
    active: Boolean,
  },
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
