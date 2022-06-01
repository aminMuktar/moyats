<template>
  <div>
    <data-table-widget></data-table-widget>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DataTableWidget from "../components/widgets/DataTableWidget.vue";

export default defineComponent({
  components: {
    DataTableWidget,
  },
});
</script>
