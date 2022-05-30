<template>
  <div class="flex flex-row">
    <Sidebar />
    <Content />
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import Sidebar from "../components/Sidebar.vue";
import Content from "../components/Content.vue";

export default defineComponent({
  setup() {},
  components: { Sidebar, Content },
});
</script>
