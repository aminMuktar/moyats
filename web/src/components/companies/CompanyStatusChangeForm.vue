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
                text-xs
                font-medium
                min-w-[100px]
                text-center
              "
              :class="{
                'text-white': isDark(st.color.hex),
                'text-gray-500': !isDark(st.color.hex),
              }"
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
import { loadCompanyContactStatuses, loadCompanyStatuses } from "../../services";
import { getOpacity, isDark } from "../../utils/helpers";

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
    isDark,
    getOpacity,
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
        data: { companyStatuses },
      } = await loadCompanyStatuses();
      this.statuses = companyStatuses;
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