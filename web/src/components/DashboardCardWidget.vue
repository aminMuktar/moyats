<template>
  <div class="w-full bg-white">
    <div class="border-b-2 border-gray-200">
      <slot name="header"></slot>
    </div>
    <div class="mb-10">
      <slot name="body"></slot>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({});
</script>
