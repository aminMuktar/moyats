<template>
  <div class="font-sans gap-y-3 flex flex-col">
    <div>
      <p class="text-3xl pb-5 font-semibold">Contacts</p>
    </div>
    <contacts-layout></contacts-layout>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import ActivitiesLayout from "../../layouts/ActivitiesLayout.vue";
import CompaniesLayout from "../../layouts/CompaniesLayout.vue";
import ContactsLayout from "../../layouts/ContactsLayout.vue";

export default defineComponent({
  components: {
    ActivitiesLayout,
    CompaniesLayout,
    ContactsLayout,
  },
});
</script>
