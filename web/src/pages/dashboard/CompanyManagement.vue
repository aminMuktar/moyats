<template>
  <div>
    <nav-header class="w-full fixed" />
    <div
      class="w-full bg-gray-200 bottom-0 top-0 absolute flex justify-center overflow-auto"
    >
      <div class="w-4/6">
        <div class="mt-28">Your Companies</div>
        <div class="grid grid-cols-3 items-center">
          <company-management-widget :url="'/dashboard'">
            <template v-slot:header> something </template>
            <template v-slot:subHeader> something </template>
            <template v-slot:body> something </template>
          </company-management-widget>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import NavHeader from "../../components/NavHeader.vue";
import CompanyManagementWidget from "../../components/widgets/CompanyManagementWidget.vue";

export default defineComponent({
  components: {
    NavHeader,
    CompanyManagementWidget,
  },
});
</script>
