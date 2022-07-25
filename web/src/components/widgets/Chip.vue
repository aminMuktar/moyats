<template>
  <div>
    <span
      class="text-sm p-2 text-white rounded-full cursor-pointer"
      :class="{
        'text-white': isDark(color),
        'text-gray-500': !isDark(color),
      }"
      :style="{
        'background-color': getOpacity(color),
      }"
      v-text="text"
    ></span>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { getOpacity, isDark } from "../../utils/helpers";

export default defineComponent({
  methods: {
    isDark,
    getOpacity,
  },
  setup() {},
  props: ["text", "color"],
});
</script>
