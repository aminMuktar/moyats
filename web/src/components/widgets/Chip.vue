<template>
  <div>
    <span
      class="text-sm p-2 text-white rounded-full cursor-pointer"
      :style="{'background-color': color}"
      v-text="text"
    ></span>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  setup() {},
  props: ["text", "color"],
});
</script>
