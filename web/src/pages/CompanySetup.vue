<template>
  <div>
    <main-header class="fixed w-full" />
    <div>
      <section class="bg-white">
        <div class="max-w-screen-xl px-4 py-16 mx-auto sm:px-6 lg:px-8">
          <center>
            <div
              class="p-8 mt-10 bg-white rounded-lg border-2 border-gray-100 lg:p-12 lg:col-span-3 w-3/4"
            >
              <p class="text-3xl py-10">Reigster your organization</p>
              <form action="" class="space-y-4">
                <div>
                  <label class="sr-only" for="name">Name</label>
                  <input
                    class="w-full p-3 text-sm border-gray-200 border-2 rounded-lg"
                    placeholder="Name"
                    type="text"
                    id="name"
                  />
                </div>

                <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
                  <div>
                    <label class="sr-only" for="email">Email</label>
                    <input
                      class="w-full p-3 text-sm border-gray-200 rounded-lg border-2"
                      placeholder="Email address"
                      type="email"
                      id="email"
                    />
                  </div>

                  <div>
                    <label class="sr-only" for="phone">Phone</label>
                    <input
                      class="w-full p-3 text-sm border-gray-200 rounded-lg border-2"
                      placeholder="Phone Number"
                      type="tel"
                      id="phone"
                    />
                  </div>
                </div>

                <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
                  <div>
                    <label class="sr-only" for="subdomain">Subdomain</label>
                    <input
                      class="w-full p-3 text-sm border-gray-200 rounded-lg border-2"
                      placeholder="Subdomain"
                      type="text"
                    />
                  </div>
                </div>

                <div class="grid grid-cols-1 gap-4 text-center sm:grid-cols-3">
                  <div>
                    <input
                      class="sr-only"
                      id="option1"
                      type="radio"
                      tabindex="-1"
                    />
                    <label
                      for="option1"
                      class="block w-full p-3 border border-gray-200 rounded-lg"
                      tabindex="0"
                    >
                      <span class="text-sm font-medium"> Option 1 </span>
                    </label>
                  </div>

                  <div>
                    <input
                      class="sr-only"
                      id="option2"
                      type="radio"
                      tabindex="-1"
                    />
                    <label
                      for="option2"
                      class="block w-full p-3 border border-gray-200 rounded-lg"
                      tabindex="0"
                    >
                      <span class="text-sm font-medium"> Option 2 </span>
                    </label>
                  </div>

                  <div>
                    <input
                      class="sr-only"
                      id="option3"
                      type="radio"
                      tabindex="-1"
                    />
                    <label
                      for="option3"
                      class="block w-full p-3 border border-gray-200 rounded-lg"
                      tabindex="0"
                    >
                      <span class="text-sm font-medium"> Option 3 </span>
                    </label>
                  </div>
                </div>

                <div>
                  <label class="sr-only" for="message">Message</label>
                  <textarea
                    class="w-full p-3 text-sm border-gray-200 rounded-lg border-2"
                    placeholder="Message"
                    rows="8"
                    id="message"
                  ></textarea>
                </div>

                <div class="mt-4">
                  <button
                    type="submit"
                    class="inline-flex items-center justify-center w-full px-5 py-3 text-white bg-black rounded-lg sm:w-auto"
                  >
                    <span class="font-medium"> Register Now </span>

                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="w-5 h-5 ml-3"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M14 5l7 7m0 0l-7 7m7-7H3"
                      />
                    </svg>
                  </button>
                </div>
              </form>
            </div>
          </center>
        </div>
      </section>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import MainHeader from "../components/MainHeader.vue";

export default defineComponent({
  components: { MainHeader },
  setup() {},
});
</script>
