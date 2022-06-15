<template>
  <div>
    <dashboard-card-widget
      class="rounded pb-0.5"
      style="border: solid 0.5px #e3e3e3"
    >
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">
          <slot name="header"></slot>
        </p>
      </template>
      <template v-slot:body>
        <div>
          <div class="sm:col-span-1 md:flex lg:flex p-2">
            <div class="w-1/4 ml-4 text-sm text-blue-500">
              <slot name="path"></slot>
            </div>
            <div class="h-2"></div>
            <div class="text-sm ml-4">
              <slot name="bodyDesc"></slot>
            </div>
          </div>
          <div
            style="
              border-bottom: 1px solid rgb(218 218 218);
              width: 98%;
              margin-left: 1%;
            "
          ></div>
        </div>
      </template>
    </dashboard-card-widget>
    <div class="h-9"></div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import DashboardCardWidget from "../DashboardCardWidget.vue";

export default defineComponent({
  components: {
    DashboardCardWidget,
  },
});
</script>
