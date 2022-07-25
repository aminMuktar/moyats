<template>
  <div class="flex w-full flex-col">
    <div
      class="flex flex-col rounded-lg overflow-hidden bg-white shadow relative"
    >
      <!-- loading overlay -->

      <div
        v-if="loadingState"
        class="
          absolute
          bg-white bg-opacity-60
          z-10
          h-full
          w-full
          flex
          items-start
          justify-center
        "
      >
        <spinner style="margin-top: 40%"></spinner>
      </div>
      <div class="flex p-2 border-b-2 flex-row w-full fixed gap-2 bg-white">
        <button
          @click="changeStat"
          type="button"
          class="
            bg-green-500
            p-2
            text-white
            rounded-md
            tracking-wider
            hover:bg-green-600
          "
        >
          Save Changes
        </button>
        <button
          @click="$emit('close')"
          type="button"
          class="
            border-red-500
            p-2
            border-2
            text-red-700
            rounded-md
            tracking-wider
            hover:bg-red-100
          "
        >
          Cancel
        </button>
      </div>
      <div class="mt-16"></div>
      <div class="flex flex-row">
        <contact-status-change-form
          ref="form"
          @status-selected="statSelected"
          v-if="getFirstWord($store.state.core.activeSlideWindow) == 'contact'"
        ></contact-status-change-form>
        <div class="w-2 h-2" v-if="selected">
          <button
            @click="$refs.form.fetchStatuses()"
            type="button"
            class="
              text-blue-700
              border border-blue-700
              hover:bg-blue-700 hover:text-white
              focus:ring-4 focus:outline-none focus:ring-blue-300
              font-medium
              rounded-full
              text-sm
              p-1.5
              my-3
              text-center
              inline-flex
              items-center
            "
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="2"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"
              />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import Spinner from "../Spinner.vue";
import ContactStatusChangeForm from "../contacts/ContactStatusChangeForm.vue";
import { updateContactStatus } from "../../services";
import { uuid } from "vue-uuid";

export default defineComponent({
  components: { Spinner, ContactStatusChangeForm },
  methods: {
    // get first word in string separated by minus
    getFirstWord(str) {
      return str.split("-")[0];
    },
    statSelected(st) {
      this.st = st;
      this.selected = true;
    },
    async changeStat() {
      await updateContactStatus({
        contact: this.$store.state.core.statusItemId,
        status: parseInt(this.st.id),
      }).then(() => {
        this.$emit("statChanged");
        this.$store.commit("updateFormupdateStatus", uuid.v4());
      });
    },
  },
  data: () => ({
    loadingState: false,
    st: null as any,
    selected: false,
  }),
});
</script>
