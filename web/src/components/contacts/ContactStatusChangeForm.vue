<template>
  <div class="flex flex-row">
    <p class="py-2 px-5 text-xl">Status</p>
    <div>
      <transition-group name="list" tag="p">
        <button
          class="flex flex-col col-span-2 w-full my-3 border-none"
          v-for="(st, ix) in statuses"
          :key="ix"
          @click="statSelected(st)"
        >
          <div class="mx-7 my-1">
            <span
              :style="{ 'background-color': getOpacity(st.color.hex) }"
              class="
                px-4
                py-2
                border-2
                hover:bg-gray-200
                rounded-lg
                tracking-wide
                text-xs text-black
                font-medium
                min-w-[100px]
                text-center
              "
              >{{ st.name }}</span
            >
          </div>
        </button>
      </transition-group>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { mapState } from "vuex";
import { loadCompanyContactStatuses } from "../../services";

export default defineComponent({
  async created() {
    await this.fetchStatuses();
  },
  computed: mapState(["activeSlideWindow"]),
  watch: {
    "$store.state.core.activeSlideWindow": function () {
      this.fetchStatuses();
    },
  },
  data: () => ({
    statuses: [] as Array<any>,
    statcpy: [] as Array<any>,
  }),
  methods: {
    // decrease color opacity by 40% from hex color
    getOpacity(hex: string) {
      const rgb = hex.match(/^#?([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i);
      if (rgb) {
        const r = parseInt(rgb[1], 16);
        const g = parseInt(rgb[2], 16);
        const b = parseInt(rgb[3], 16);
        return `rgba(${r}, ${g}, ${b}, 0.4)`;
      }
      return "";
    },
    statSelected(st) {
      this.statuses = [st];
      this.$emit("status-selected", st);
      this.statcpy = this.statuses;
    },
    resetStats() {
      this.statuses = this.statcpy;
    },
    async fetchStatuses() {
      const {
        data: { contactStatuses },
      } = await loadCompanyContactStatuses();
      this.statuses = contactStatuses;
    },
  },
});
</script>

<style>
.list-item {
  display: inline-block;
  margin-right: 10px;
}
.list-enter-active,
.list-leave-active {
  transition: all 1s;
}
.list-enter, .list-leave-to /* .list-leave-active below version 2.1.8 */ {
  opacity: 0;
  transform: translateY(30px);
}
</style>