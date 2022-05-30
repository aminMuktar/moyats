<template>
  <nav class="border-gray-200 sm:px-4 py-2.5">
    <div class="container flex flex-wrap justify-between items-center mx-auto">
      <div class="flex items-center order-2">
        <div
          class="
            hidden
            z-50
            my-4
            text-base
            list-none
            bg-white
            rounded
            divide-y divide-gray-100
            shadow
            dark:bg-gray-700 dark:divide-gray-600
          "
          id="dropdown"
          data-popper-reference-hidden=""
          data-popper-escaped=""
          data-popper-placement="top"
          style="
            position: absolute;
            inset: auto auto 0px 0px;
            margin: 0px;
            transform: translate3d(1015px, 950.5px, 0px);
          "
        >
          <ul class="py-1" aria-labelledby="dropdown">
            <li>
              <a
                href="#"
                class="
                  block
                  py-2
                  px-4
                  text-sm text-gray-700
                  hover:bg-gray-100
                  dark:hover:bg-gray-600
                  dark:text-gray-200
                  dark:hover:text-white
                "
                >Dashboard</a
              >
            </li>
            <li>
              <a
                href="#"
                class="
                  block
                  py-2
                  px-4
                  text-sm text-gray-700
                  hover:bg-gray-100
                  dark:hover:bg-gray-600
                  dark:text-gray-200
                  dark:hover:text-white
                "
                >Settings</a
              >
            </li>
            <li>
              <a
                href="#"
                class="
                  block
                  py-2
                  px-4
                  text-sm text-gray-700
                  hover:bg-gray-100
                  dark:hover:bg-gray-600
                  dark:text-gray-200
                  dark:hover:text-white
                "
                >Earnings</a
              >
            </li>
            <li>
              <a
                href="#"
                class="
                  block
                  py-2
                  px-4
                  text-sm text-gray-700
                  hover:bg-gray-100
                  dark:hover:bg-gray-600
                  dark:text-gray-200
                  dark:hover:text-white
                "
                >Sign out</a
              >
            </li>
          </ul>
        </div>
        <div class="flex flex-row">
          <menu-drop-down :active="active">
            <button
              @click="active = !active"
              class="
                mx-2
                bg-black
                text-white
                border-2 border-gray-500
                rounded-full
              "
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"
                />
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                />
              </svg>
            </button>
          </menu-drop-down>
          <!-- <button
            type="button"
            class="
              flex
              mr-3
              text-sm
              bg-gray-800
              rounded-full
              md:mr-0
              text-white
              focus:ring-4 focus:ring-gray-300
              dark:focus:ring-gray-600
            "
            @click="logout"
            id="user-menu-button"
            aria-expanded="false"
            data-dropdown-toggle="dropdown"
          >
            <span>Logout</span>
          </button> -->
        </div>

        <button
          data-collapse-toggle="mobile-menu-2"
          type="button"
          class="
            inline-flex
            items-center
            p-2
            ml-1
            text-sm text-gray-500
            rounded-lg
            md:hidden
            hover:bg-gray-100
            focus:outline-none focus:ring-2 focus:ring-gray-200
            dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600
          "
          aria-controls="mobile-menu-2"
          aria-expanded="false"
        >
          <span class="sr-only">Open main menu</span>
          <svg
            class="w-6 h-6"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
              clip-rule="evenodd"
            ></path>
          </svg>
          <svg
            class="hidden w-6 h-6"
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
      <div
        class="
          hidden
          justify-between
          items-center
          w-full
          md:flex md:w-auto md:order-1
        "
        id="mobile-menu-2"
      >
        <ul
          class="
            flex flex-col
            mt-4
            md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium
          "
        ></ul>
      </div>
    </div>
  </nav>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { LOGOUT } from "../queries/auth";
import MenuDropDown from "./MenuDropDown.vue";

export default defineComponent({
  components: { MenuDropDown },
  setup() {},
  data: () => ({
    active: false,
  }),
  methods: {
    logout() {
      this.$apollo
        .mutate({
          mutation: LOGOUT,
        })
        .then(({ data }) => {
          if (data) {
            this.$store.commit("clearToken");
            location.assign("/login");
          }
        });
    },
  },
});
</script>
