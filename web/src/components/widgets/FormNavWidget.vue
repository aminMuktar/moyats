<template>
  <div
    class="flex right-0 z-50 mr-0 mt-1 absolute w-1/2 h-full justify-end"
    :class="{ 'z-0': !display }"
  >
    <button
      v-if="showBtn"
      class="w-10 h-10 bg-white shadow-xl rounded flex justify-center items-center fixed"
      @click="sliderActivator()"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-5 w-5"
        viewBox="0 0 20 20"
        fill="currentColor"
      >
        <path
          fill-rule="evenodd"
          d="M6 6V5a3 3 0 013-3h2a3 3 0 013 3v1h2a2 2 0 012 2v3.57A22.952 22.952 0 0110 13a22.95 22.95 0 01-8-1.43V8a2 2 0 012-2h2zm2-1a1 1 0 011-1h2a1 1 0 011 1v1H8V5zm1 5a1 1 0 011-1h.01a1 1 0 110 2H10a1 1 0 01-1-1z"
          clip-rule="evenodd"
        />
        <path
          d="M2 13.692V16a2 2 0 002 2h12a2 2 0 002-2v-2.308A24.974 24.974 0 0110 15c-2.796 0-5.487-.46-8-1.308z"
        />
      </svg>
    </button>
    <transition name="nested">
      <div
        class="w-full sm:w-1/2 md:w-1/2 lg:w-1/2 xl:w-1/2 h-screen bg-white shadow-lg shadow-black-500/50 fixed"
        v-show="display"
      >
        <div class="flex justify-between bg-gray-100">
          <p class="pt-3 px-2 border-b">Create a job order</p>
          <button @click="closeSlider" class="p-2 hover:bg-gray-100 m-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M10.293 15.707a1 1 0 010-1.414L14.586 10l-4.293-4.293a1 1 0 111.414-1.414l5 5a1 1 0 010 1.414l-5 5a1 1 0 01-1.414 0z"
                clip-rule="evenodd"
              />
              <path
                fill-rule="evenodd"
                d="M4.293 15.707a1 1 0 010-1.414L8.586 10 4.293 5.707a1 1 0 011.414-1.414l5 5a1 1 0 010 1.414l-5 5a1 1 0 01-1.414 0z"
                clip-rule="evenodd"
              />
            </svg>
          </button>
        </div>
        <div class="flex p-2 w-full">
          <form class="w-full">
            <div class="grid grid-cols-1 w-full">
              <div class="flex col-span-2 w-full p-4">
                <div class="w-52">
                  <label class="sr-only" for="name">Title</label>
                  <span class="m-3">Title* </span>
                </div>
                <div class="w-full ml-10">
                  <input
                    required
                    class="w-full p-1 text-sm border-gray-200 border-2 rounded-lg"
                    placeholder="Title"
                    type="text"
                    id="name"
                  />
                </div>
              </div>
              <div class="flex col-span-2 p-2">
                <div class="w-52">
                  <label class="sr-only" for="name">Location</label>
                  <span class="m-3 w-full">Location*</span>
                </div>
                <div class="flex gap-2">
                  <input
                    required
                    class="w-full p-1 text-sm border-gray-200 border-2 rounded-lg"
                    placeholder="City"
                    type="text"
                    id="name"
                  />
                  <input
                    required
                    class="w-full p-1 text-sm border-gray-200 border-2 rounded-lg"
                    placeholder="State"
                    type="text"
                    id="name"
                  />
                  <input
                    required
                    class="w-full p-1 text-sm border-gray-200 border-2 rounded-lg"
                    placeholder="Zip Code"
                    type="text"
                    id="name"
                  />
                </div>
              </div>
              <div class="flex col-span-2 w-full p-2">
                <label class="sr-only" for="name">Job Type</label>
                <div class="w-52">
                  <span class="m-3">Job Type*</span>
                </div>
                <select
                  required
                  class="w-1/3 p-1 text-sm border-gray-200 border-2 rounded-lg text-gray-600"
                  placeholder="Title"
                  type="selector"
                  id="name"
                >
                  <option value="">Something</option>
                  <option value="">Something</option>
                  <option value="">Something</option>
                  <option value="">Something</option>
                  <option value="">Something</option>
                </select>
              </div>
              <div class="flex col-span-2 w-full p-2">
                <div class="w-52">
                  <span class="m-3">Recruiter* </span>
                </div>
                <div>
                  <div class="bg-blue-300 rounded-lg flex left-0">
                    <a
                      href=""
                      class="h-full w-full flex justify-center items-center pl-4 pr-4 text-gray-600"
                    >
                      Someone</a
                    >
                  </div>
                </div>
              </div>
              <div class="flex col-span-2 w-full p-2">
                <div class="w-52">
                  <label class="sr-only" for="name">Owner</label>
                  <span class="m-3">Owner* </span>
                </div>
                <div>
                  <div class="bg-blue-300 rounded-lg">
                    <a
                      href=""
                      class="h-full w-full flex justify-center items-center pl-4 pr-4 text-gray-600"
                    >
                      Someone</a
                    >
                  </div>
                </div>
              </div>
              <div class="col-span-2 flex p-2">
                <div class="w-52">
                  <label class="sr-only" for="name"></label>
                  <span class="m-3">Source* </span>
                </div>
                <div>
                  <input
                    required
                    class="w-full p-1 text-sm border-gray-200 border-2 rounded-lg"
                    placeholder="Source"
                    type="text"
                    id="name"
                  />
                </div>
              </div>
              <div class="col-span-2 flex p-2">
                <div class="w-52">
                  <label class="sr-only" for="name">Title</label>
                  <span class="m-3">Sourcer* </span>
                </div>
                <div>
                  <input
                    required
                    class="w-full p-1 text-sm border-gray-200 border-2 rounded-lg"
                    placeholder="Sourcer"
                    type="text"
                    id="name"
                  />
                </div>
              </div>
              <div class="col-span-2 flex p-2">
                <div class="w-52">
                  <label class="sr-only" for="name">Group</label>
                  <span class="m-3">Group* </span>
                </div>
                <div>
                  <input
                    required
                    class="w-full p-1 text-sm border-gray-200 border-2 rounded-lg"
                    placeholder="Group"
                    type="text"
                    id="name"
                  />
                </div>
              </div>

              <!-- second section start -->
              <div class="w-full border-2"></div>

              <div class="col-span-2 flex p-2">
                <div class="w-52">
                  <label class="sr-only" for="name">Hot</label>
                  <span class="m-3">Hot* </span>
                </div>
                <div>
                  <input
                    required
                    class="p-1 text-sm border-gray-200 border-2 rounded-lg"
                    type="checkbox"
                  />
                </div>
              </div>
              <div class="col-span-2 flex p-2">
                <div class="w-52">
                  <label class="sr-only" for="name">Start Date</label>
                  <span class="m-3">Start Date* </span>
                </div>
                <div>
                  <input
                    required
                    class="w-full p-1 text-sm border-gray-200 border-2 rounded-lg"
                    placeholder="Start date"
                    type="text"
                    id="name"
                  />
                </div>
              </div>
              <div class="col-span-2 flex p-2">
                <div class="w-52">
                  <label class="sr-only" for="name">Salery</label>
                  <span class="m-3">Salery* </span>
                </div>
                <div>
                  <input
                    required
                    class="w-full p-1 text-sm border-gray-200 border-2 rounded-lg"
                    placeholder="Salery"
                    type="text"
                    id="name"
                  />
                </div>
              </div>
              <div class="col-span-2 flex p-2">
                <div class="w-52">
                  <label class="sr-only" for="name">Duration</label>
                  <span class="m-3">Duration* </span>
                </div>
                <div>
                  <input
                    required
                    class="w-full p-1 text-sm border-gray-200 border-2 rounded-lg"
                    placeholder="Duration"
                    type="text"
                    id="name"
                  />
                </div>
              </div>
              <div class="col-span-2 flex p-2">
                <div class="w-52">
                  <label class="sr-only" for="name">Maximum Rate</label>
                  <span class="m-3">Maximum Rate* </span>
                </div>
                <div>
                  <input
                    required
                    class="w-full p-1 text-sm border-gray-200 border-2 rounded-lg"
                    placeholder="Maximum Rate"
                    type="text"
                    id="name"
                  />
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </transition>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  data() {
    return {
      display: false,
      showBtn: true,
      title: "",
    };
  },
  cretated() {
    console.log(this.title);
  },
  methods: {
    closeSlider() {
      this.display = false;
      setTimeout(() => {
        this.showBtn = true;
      }, 700);
    },
    sliderActivator() {
      this.display = !this.display;
      if (this.display) this.showBtn = false;
    },
  },
});
</script>

<style scoped>
.nested-enter-active,
.nested-leave-active {
  transition: all 0.3s ease-in-out;
}
/* delay leave of parent element */
.nested-leave-active {
  transition-delay: 0.25s;
}

.nested-enter-from,
.nested-leave-to {
  transform: translateX(50px);
  opacity: 0;
}

/* we can also transition nested elements using nested selectors */
.nested-enter-active .inner,
.nested-leave-active .inner {
  transition: all 0.3s ease-in-out;
}
/* delay enter of nested element */
.nested-enter-active .inner {
  transition-delay: 0.25s;
}

.nested-enter-from .inner,
.nested-leave-to .inner {
  transform: translateX(50px);
  /*
  	Hack around a Chrome 96 bug in handling nested opacity transitions.
    This is not needed in other browsers or Chrome 99+ where the bug
    has been fixed.
  */
  opacity: 0.001;
}
</style>
