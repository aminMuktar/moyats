<template>
  <article
    class="
      relative
      px-6
      pt-12
      pb-6
      bg-white
      border border-gray-100
      rounded-lg
      shadow-sm
    "
  >
    <p class="text-sm font-medium text-gray-500">Profit</p>

    <p class="inline-flex items-end mt-1">
      <span class="text-2xl font-medium leading-none">240.94</span>
    </p>

    <p
      class="
        absolute
        inline-flex
        p-1
        text-red-600
        bg-red-100
        rounded
        top-4
        right-4
      "
    >
    <slot name="icon"></slot>
    </p>
  </article>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  setup() {},
});
</script>
