<template>
  <div class="md:w-full sm:w-full lg:w-1/2 xl:w-1/2">
    <account-setting-widgets>
      <template v-slot:header> Feature Settiings </template>
      <template v-slot:path> <router-link to="/change-user-data"> Edit your information </router-link> </template>
      <template v-slot:bodyDesc>
        Edit your name email and other informations
      </template>
    </account-setting-widgets>
    <account-setting-widgets>
      <template v-slot:header> Site Management </template>
      <template v-slot:path> <router-link to="/change-social"> Change Password </router-link> </template>
      <template v-slot:bodyDesc>
        Change your password 
      </template>
    </account-setting-widgets>
    <account-setting-widgets>
      <template v-slot:header> Interface Customization </template>
      <template v-slot:path> <a href="#"> Workflow </a> </template>
      <template v-slot:bodyDesc>
        something something something something something something something...
      </template>
    </account-setting-widgets>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import AccountSettingWidgets from "../components/widgets/AccountSettingWidgets.vue";

export default defineComponent({
  components: {
    AccountSettingWidgets,
  },
});
</script>
