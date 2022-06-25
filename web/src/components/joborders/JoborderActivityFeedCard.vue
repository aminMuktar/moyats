<template>
  <div>
    <dashboard-card-widget slot="body">
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">Activity Feed</p>
      </template>
      <template v-slot:body>
        <div>
          <div
            class="
              sm:col-span-1
              md:flex
              lg:flex
              p-2
              scroll-smooth
              hover:scroll-auto
              overflow-y-scroll
            "
            style="height: 30rem"
          >
            <div class="w-full ml-4 text-sm">
              <ol class="relative border-l border-gray-200">
                <li class="mb-10 ml-6">
                  <span
                    class="
                      flex
                      absolute
                      -left-3
                      justify-center
                      items-center
                      w-6
                      h-6
                      bg-blue-200
                      rounded-full
                      ring-8 ring-white
                    "
                  >
                    <svg
                      class="w-3 h-3 text-blue-600"
                      fill="currentColor"
                      viewBox="0 0 20 20"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        fill-rule="evenodd"
                        d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z"
                        clip-rule="evenodd"
                      ></path>
                    </svg>
                  </span>
                  <h3
                    class="
                      flex
                      items-center
                      mb-1
                      text-lg
                      font-semibold
                      text-gray-900
                    "
                  >
                    Flowbite Application UI v2.0.0
                    <span
                      class="
                        bg-blue-100
                        text-blue-800 text-sm
                        font-medium
                        mr-2
                        px-2.5
                        py-0.5
                        rounded
                        ml-3
                      "
                      >Latest</span
                    >
                  </h3>
                  <time
                    class="
                      block
                      mb-2
                      text-sm
                      font-normal
                      leading-none
                      text-gray-400
                      dark:text-gray-500
                    "
                    >Released on January 13th, 2022</time
                  >
                  <p class="mb-4 text-base font-normal text-gray-500">
                    Get access to over 20+ pages including a dashboard layout,
                    charts, kanban board, calendar, and pre-order E-commerce &
                    Marketing pages.
                  </p>
                  <a
                    href="#"
                    class="
                      inline-flex
                      items-center
                      py-2
                      px-4
                      text-sm
                      font-medium
                      text-gray-900
                      bg-white
                      rounded-lg
                      border border-gray-200
                      hover:bg-gray-100 hover:text-blue-700
                      focus:z-10
                      focus:ring-4
                      focus:outline-none
                      focus:ring-gray-200
                      focus:text-blue-700
                    "
                    ><svg
                      class="mr-2 w-4 h-4"
                      fill="currentColor"
                      viewBox="0 0 20 20"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        fill-rule="evenodd"
                        d="M6 2a2 2 0 00-2 2v12a2 2 0 002 2h8a2 2 0 002-2V7.414A2 2 0 0015.414 6L12 2.586A2 2 0 0010.586 2H6zm5 6a1 1 0 10-2 0v3.586l-1.293-1.293a1 1 0 10-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 11.586V8z"
                        clip-rule="evenodd"
                      ></path>
                    </svg>
                    Download ZIP</a
                  >
                </li>
                <li class="mb-10 ml-6" v-for="x in 10" :key="x">
                  <span
                    class="
                      flex
                      absolute
                      -left-3
                      justify-center
                      items-center
                      w-6
                      h-6
                      bg-blue-200
                      rounded-full
                      ring-8 ring-white
                    "
                  >
                    <svg
                      class="w-3 h-3 text-blue-600"
                      fill="currentColor"
                      viewBox="0 0 20 20"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        fill-rule="evenodd"
                        d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z"
                        clip-rule="evenodd"
                      ></path>
                    </svg>
                  </span>
                  <h3 class="mb-1 text-lg font-semibold text-gray-900">
                    Flowbite Figma v1.3.0
                  </h3>
                  <time
                    class="
                      block
                      mb-2
                      text-sm
                      font-normal
                      leading-none
                      text-gray-400
                    "
                    >Released on December 7th, 2021</time
                  >
                  <p class="text-base font-normal text-gray-500">
                    All of the pages and components are first designed in Figma
                    and we keep a parity between the two versions even as we
                    update the project.
                  </p>
                </li>
              </ol>
            </div>
          </div>
        </div>
      </template>
    </dashboard-card-widget>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DashboardCardWidget from "../DashboardCardWidget.vue";

export default defineComponent({
  components: { DashboardCardWidget },
  setup() {},
});
</script>
