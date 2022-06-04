<template>
  <div class="w-1/2">
    <dashboard-card-widget
      class="rounded pb-0.5"
      style="border: solid 0.5px #e3e3e3"
    >
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">Feature Settiings</p>
      </template>
      <template v-slot:body>
        <div>
          <div class="flex p-2">
            <div class="w-1/4 ml-4 text-sm text-blue-500">
              <a href="#">Workflow</a>
            </div>
            <div class="text-sm">
              something something something something something something
              something...
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
    <dashboard-card-widget
      class="rounded pb-0.5"
      style="border: solid 0.5px #e3e3e3"
    >
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">Site Management</p>
      </template>
      <template v-slot:body>
        <div>
          <div class="flex p-2">
            <div class="w-1/4 ml-4 text-sm text-blue-500">
              <a href="#">Workflow</a>
            </div>
            <div class="text-sm">
              something something something something something something
              something...
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

    <dashboard-card-widget
      class="rounded pb-0.5"
      style="border: solid 0.5px #e3e3e3"
    >
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">Interface Customization</p>
      </template>
      <template v-slot:body>
        <div>
          <div class="flex p-2">
            <div class="w-1/4 ml-4 text-sm text-blue-500">
              <a href="#">Workflow</a>
            </div>
            <div class="text-sm">
              something something something something something something
              something...
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
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DashboardCardWidget from "../../components/DashboardCardWidget.vue";

export default defineComponent({
  components: {
    DashboardCardWidget,
  },
});
</script>
