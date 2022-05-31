<template>
  <div :class="[`h-${height}`]" class="w-full bg-white">
    <div class="border-b-2 border-gray-200">
      <slot name="header"></slot>
    </div>
    <div>
      <slot name="body"></slot>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  props: {
    height: Number,
  },
});
</script>
