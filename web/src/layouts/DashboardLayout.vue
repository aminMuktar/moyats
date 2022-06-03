<template>
  <div class="flex h-screen bg-gray-200 font-roboto">
    <Sidebar />

    <div class="flex-1 flex flex-col overflow-hidden">
      <NavHeader />

      <main
        class="flex-1 overflow-x-hidden overflow-y-auto bg-gray-100 relative"
      >
        <div>
          <FormNavWidget />
        </div>
        <div class="container mx-auto px-6 py-8">
          <slot />
        </div>
      </main>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Sidebar from "../components/Sidebar.vue";
import NavHeader from "../components/NavHeader.vue";
import FormNavWidget from "../components/widgets/FormNavWidget.vue";

export default defineComponent({
  components: {
    Sidebar,
    NavHeader,
    FormNavWidget,
  },
});
</script>
