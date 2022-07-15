<template>
  <dialog-modal :show="show" @close="$emit('close')">
    <div>
      <transition name="slide-form">
        <center>
          <div class="overflow-y-auto overflow-x-hidden w-full mx-10">
            <!-- Modal content -->
            <div class="bg-white rounded-lg shadow">
              <!-- Modal header -->
              <div
                class="flex justify-between items-center p-5 rounded-t border-b"
              >
                <h3 class="text-xl font-medium">Update Work History</h3>
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
              <div class="text-base leading-relaxed text-gray-800 mx-2">
                <form class="mx-2" @submit="submitWorkHistory">
                  <div>
                    <input
                      v-model="title"
                      type="text"
                      class="
                        bg-gray-50
                        mt-2
                        mx-2
                        border border-gray-300
                        text-gray-900 text-sm
                        rounded-lg
                        focus:ring-blue-500 focus:border-blue-500
                        block
                        w-full
                        p-2.5
                      "
                      placeholder="Title"
                      required
                    />
                  </div>
                  <div>
                    <input
                      v-model="employeer"
                      placeholder="Employeer"
                      type="text"
                      class="
                        mx-2
                        mt-2
                        bg-gray-50
                        border border-gray-300
                        text-gray-900 text-sm
                        rounded-lg
                        focus:ring-blue-500 focus:border-blue-500
                        block
                        w-full
                        p-2.5
                      "
                      required
                    />
                  </div>
                  <div class="grid grid-cols-2 gap-2 my-2">
                    <date-picker
                      placeholder="Start Date"
                      class="
                        mx-2
                        bg-gray-50
                        border border-gray-300
                        text-gray-900 text-sm
                        rounded-lg
                        focus:ring-blue-500 focus:border-blue-500
                        w-full
                        p-2.5
                      "
                      locale="en,fa"
                      format="YYYY-M-D"
                      v-model="startDate"
                    ></date-picker>
                    <date-picker
                      placeholder="End Date"
                      class="
                        mx-2
                        bg-gray-50
                        border border-gray-300
                        text-gray-900 text-sm
                        rounded-lg
                        focus:ring-blue-500 focus:border-blue-500
                        w-full
                        p-2.5
                      "
                      locale="en,fa"
                      format="YYYY-M-D"
                      v-model="endDate"
                    ></date-picker>
                  </div>
                  <textarea
                    v-model="leavingReason"
                    id="message"
                    rows="4"
                    class="
                      block
                      p-2.5
                      w-full
                      m-2
                      bg-gray-100
                      text-sm text-gray-900
                      rounded-lg
                      border border-gray-300
                      focus:ring-blue-500 focus:border-blue-500
                    "
                    placeholder="Reason for leaving..."
                  ></textarea>
                  <!-- Modal footer -->
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
import { updateCandidateWorkhistory } from "../../services/candidates";

export default defineComponent({
  components: { DialogModal, DatePicker },
  props: ["show", "wh"],
  data: () => ({
    startDate: null,
    endDate: null,
    title: null,
    employeer: null,
    currentlyWorking: false,
    leavingReason: "",
  }),
  created() {
    console.log(this.wh);
    this.title = this.wh.title;
    this.employeer = this.wh.employeer;
    this.startDate = this.wh.startDate;
    this.endDate = this.wh.endDate;
    this.leavingReason = this.wh.reasonForLeaving;
  },
  methods: {
    async submitWorkHistory(e) {
      e.preventDefault();
      const { data, errors } = await updateCandidateWorkhistory({
        candidiate: this.$route.params.cid,
        input: {
          title: this.title,
          startDate: this.startDate,
          endDate: this.endDate,
          employeer: this.employeer,
          currentlyWorking: this.currentlyWorking,
          leavingReason: this.leavingReason,
        },
        whistory: this.wh.id,
      });
      if (data) {
        this.$emit("updated");
      }
    },
  },
});
</script>
