<template>
  <div class="w-full h-40 bg-white">
    <div class="border-b-2 border-gray-200">
      <slot name="header"></slot>
    </div>
    <div>
        <slot name="body"></slot>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
})
</script>
