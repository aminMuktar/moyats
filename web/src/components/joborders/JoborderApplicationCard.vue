<template>
  <div>
    <dashboard-card-widget slot="body">
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">Application</p>
      </template>
      <template v-slot:body>
        <div>
          <div
            class="sm:col-span-1 md:flex lg:flex p-2"
            v-for="(app, ix) in data.applications"
            :key="ix"
          >
            <router-link
              :to="`/applications/${app.applicationId}`"
              class="text-blue-600"
            >
              {{ app.header }}
            </router-link>
          </div>
        </div>
      </template>
    </dashboard-card-widget>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DashboardCardWidget from "../DashboardCardWidget.vue";

export default defineComponent({
  components: { DashboardCardWidget },
  props: ["data"],
  setup() {},
});
</script>
