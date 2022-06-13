<template>
  <div></div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { ACTIVITY_INFO } from "../../queries/auth";

export default defineComponent({
  async created() {
    await this.activityInfo();
  },
  methods: {
    async activityInfo() {
      const { data, errors } = await this.$apollo.query({
        query: ACTIVITY_INFO,
        variables: {
          activityId: this.$route.params.aid,
        },
      });
      if (!errors) {
        console.log(data.activities);
      }
    },
  },
});
</script>
