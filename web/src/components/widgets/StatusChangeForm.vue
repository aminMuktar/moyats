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
      <div>
        <p>
          Change Status of
          {{
            uppercaseFirstLetter(
              $store.state.core.activeSlideWindow.split("-")[0]
            )
          }}
        </p>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  methods: {
    // change first letter of string to uppercase
    uppercaseFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
  },
});
</script>
