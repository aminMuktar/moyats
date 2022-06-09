<template>
  <div class="font-sans gap-y-3 flex flex-col m-5">
    <div>
      <p class="text-3xl pb-5 font-semibold">Account Settings</p>
    </div>
    <account-setting-layout></account-setting-layout>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import AccountSettingLayout from "../../layouts/AccountSettingLayout.vue";

export default defineComponent({
  components: {
    AccountSettingLayout,
  },
});
</script>
