<template>
  <div class="">
    <nav-header class="w-full fixed" />
    <div class="w-full bg-gray-200 absolute flex justify-center">
      <div class="w-4/6 grid grid-cols-3 items-center">
        <div class="bg-white w-96 h-96 mt-28 rounded-lg shadow-md">
          something
        </div>
        <div class="bg-white w-96 h-96 mt-28 rounded-lg shadow-md">
          something
        </div>
        <div class="bg-white w-96 h-96 mt-28 rounded-lg shadow-md">
          something
        </div>
        <div class="bg-white w-96 h-96 mt-28 rounded-lg shadow-md">
          something
        </div>
        <div class="bg-white w-96 h-96 mt-28 rounded-lg shadow-md">
          something
        </div>
        <div class="bg-white w-96 h-96 mt-28 rounded-lg shadow-md">
          something
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import NavHeader from "../../components/NavHeader.vue";

export default defineComponent({
  components: {
    NavHeader,
  },
});
</script>
