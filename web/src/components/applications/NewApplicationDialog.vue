<template>
  <dialog-modal :show="show" @close="$emit('close')">
    <div style="width: 600px">
      <transition name="slide-form">
        <center>
          <div class="overflow-y-auto overflow-x-hidden mx-10">
            <!-- Modal content -->
            <div class="bg-white rounded-lg shadow">
              <!-- Modal header -->
              <div
                class="flex justify-between items-center p-5 rounded-t border-b"
              >
                <h3 class="text-xl font-medium">Add Application</h3>
                <button
                  @click="$emit('close')"
                  type="button"
                  class="
                    text-gray-400
                    bg-transparent
                    hover:bg-gray-200 hover:text-gray-900
                    rounded-lg
                    text-sm
                    p-1.5
                    ml-auto
                    inline-flex
                    items-center
                  "
                  data-modal-toggle="medium-modal"
                >
                  <svg
                    class="w-5 h-5"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                      clip-rule="evenodd"
                    ></path>
                  </svg>
                </button>
              </div>
              <!-- Modal body -->
              <div class="text-base leading-relaxed text-gray-800 w-full">
                <form
                  @submit="submitForm"
                  class="mx-5 gap-y-3 flex flex-col my-2"
                >
                  <small class="text-left m-1">Description *</small>
                  <div>
                    <input
                      v-model="description"
                      id="description"
                      required
                      rows="4"
                      class="
                        block
                        p-2.5
                        w-full
                        bg-gray-100
                        text-sm text-gray-900
                        rounded-lg
                        border border-gray-300
                        focus:ring-blue-500 focus:border-blue-500
                      "
                      placeholder="Description"
                    />
                  </div>
                  <small class="text-left m-1">Header</small>
                  <textarea
                    v-model="header"
                    id="message"
                    rows="4"
                    class="
                      block
                      p-2.5
                      w-full
                      bg-gray-100
                      text-sm text-gray-900
                      rounded-lg
                      border border-gray-300
                      focus:ring-blue-500 focus:border-blue-500
                    "
                    placeholder="Header that goes on top of the application form"
                  ></textarea>
                  <div class="flex items-center mb-4">
                    <input
                      v-model="required"
                      id="default-checkbox"
                      type="checkbox"
                      value=""
                      class="
                        w-4
                        h-4
                        text-blue-600
                        rounded
                        focus:ring-blue-500 focus:ring-2
                      "
                    />
                    <label
                      for="default-checkbox"
                      class="ml-2 text-sm font-medium text-gray-900"
                      >Required</label
                    >
                  </div>
                  <!-- Modal footer -->
                  <div
                    class="
                      flex
                      items-center
                      px-1
                      pt-3
                      pb-5
                      space-x-2
                      rounded-b
                      border-gray-200
                    "
                  >
                    <button
                      data-modal-toggle="medium-modal"
                      type="submit"
                      class="
                        text-white
                        bg-green-700
                        hover:bg-green-800
                        focus:ring-4 focus:outline-none focus:ring-blue-300
                        font-medium
                        rounded-lg
                        text-sm
                        px-5
                        py-2.5
                        text-center
                      "
                    >
                      Save Changes
                    </button>
                    <button
                      data-modal-toggle="medium-modal"
                      type="button"
                      @click="$emit('close')"
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
                    >
                      Cancel
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </center>
      </transition>
    </div>
  </dialog-modal>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DialogModal from "../DialogModal.vue";
import DatePicker from "vue3-persian-datetime-picker";
import {
  addApplication,
} from "../../services";

export default defineComponent({
  components: { DialogModal, DatePicker },
  props: ["show", "application"],
  data: () => ({
    title: "",
    saveTo: null,
    required: false,
    description: "",
    header: "",
  }),
  created() {},
  methods: {
    async submitForm(e) {
      e.preventDefault();

      const { data } = await addApplication({
        desc: this.description,
        header: this.header,
      });
      if (data) {
        this.$emit("updated");
      }
    },
  },
});
</script>
