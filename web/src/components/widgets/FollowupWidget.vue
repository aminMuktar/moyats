<template>
  <dashboard-card-widget>
    <template v-slot:header>
      <p class="p-3 font-semibold text-lg">Follow Ups</p>
    </template>
    <template v-slot:body>
      <p class="pt-10 text-center">you don't have any follow ups</p>
    </template>
  </dashboard-card-widget>
</template>
<script lang="ts">
import { defineComponent } from 'vue'
import DashboardCardWidget from '../DashboardCardWidget.vue'

export default defineComponent({
  components: { DashboardCardWidget },
    setup() {
        
    },
})
</script>
