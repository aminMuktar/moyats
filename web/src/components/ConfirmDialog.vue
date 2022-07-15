<template>
  <div>
    <dialog-modal :show="show" @close="$emit('close')">
      <div>
        <transition name="slide-form">
          <center>
            <div class="overflow-y-auto overflow-x-hidden w-full mx-10">
              <!-- Modal content -->
              <div class="bg-white rounded-lg shadow">
                <!-- Modal header -->
                <div
                  class="
                    flex
                    justify-between
                    items-center
                    p-5
                    rounded-t
                    border-b
                  "
                >
                  <h3 class="text-xl font-medium" v-text="confirmMessage"></h3>
                </div>
                <div class="text-base leading-relaxed text-gray-800 mx-2">
                  <div
                    class="
                      flex
                      items-center
                      px-3
                      pt-3
                      pb-5
                      space-x-2
                      rounded-b
                      border-gray-200
                    "
                  >
                    <button
                      @click="$emit('confirm')"
                      data-modal-toggle="medium-modal"
                      type="submit"
                      class="
                        text-white
                        bg-red-700
                        hover:bg-red-800
                        focus:ring-4 focus:outline-none focus:ring-blue-300
                        font-medium
                        rounded-lg
                        text-sm
                        px-5
                        py-2.5
                        text-center
                      "
                      v-text="confirmBtnText"
                    ></button>
                    <button
                      @click="$emit('decline')"
                      data-modal-toggle="medium-modal"
                      type="button"
                      class="
                        text-gray-500
                        bg-white
                        hover:bg-gray-100
                        focus:ring-4 focus:outline-none focus:ring-gray-200
                        rounded-lg
                        border border-gray-200
                        text-sm
                        font-medium
                        px-5
                        py-2.5
                        hover:text-gray-900
                        focus:z-10
                      "
                      v-text="cancelBtnText"
                    ></button>
                  </div>
                </div>
              </div>
            </div>
          </center>
        </transition>
      </div>
    </dialog-modal>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DialogModal from "./DialogModal.vue";

export default defineComponent({
  components: { DialogModal },
  props: ["show", "confirmMessage", "cancelBtnText", "confirmBtnText"],
  data: () => ({}),
});
</script>
