<template>
  <router-link v-bind:to="url">
    <div class="bg-white w-96 h-80 mt-10 rounded-lg shadow-md p-9">
      <div class="text-3xl capitalize">
        <slot name="header"></slot>
      </div>
      <div class="text-gray-400 text-lg capitalize">
        <slot name="subHeader"></slot>
      </div>
      <div class="flex justify-center mt-12 capitalize text-2xl">
        <slot name="body"></slot>
      </div>
    </div>
  </router-link>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  props: ["url"],
});
</script>
