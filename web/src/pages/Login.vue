<template>
  <div
    class="
      min-h-full
      flex
      items-center
      justify-center
      py-12
      px-4
      sm:px-6
      lg:px-8
    "
  >
    <div class="max-w-md w-full space-y-8">
      <div>
        <img
          class="mx-auto h-12 w-auto"
          src="https://tailwindui.com/img/logos/workflow-mark-indigo-600.svg"
          alt="Workflow"
        />
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Sign in to your account
        </h2>
      </div>
      <div class="mt-8 space-y-6">
        <input type="hidden" name="remember" value="true" />
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="email-address" class="sr-only">Email address</label>
            <input
              id="email-address"
              name="email"
              type="email"
              autocomplete="email"
              required="true"
              class="
                appearance-none
                rounded-none
                relative
                block
                w-full
                px-3
                py-2
                border border-gray-300
                placeholder-gray-500
                text-gray-900
                rounded-t-md
                focus:outline-none
                focus:ring-indigo-500
                focus:border-indigo-500
                focus:z-10
                sm:text-sm
              "
              placeholder="Email address"
              v-model="email"
            />
          </div>
          <div>
            <label for="password" class="sr-only">Password</label>
            <input
              name="password"
              type="password"
              required="true"
              class="
                appearance-none
                rounded-none
                relative
                block
                w-full
                px-3
                py-2
                border border-gray-300
                placeholder-gray-500
                text-gray-900
                rounded-b-md
                focus:outline-none
                focus:ring-indigo-500
                focus:border-indigo-500
                focus:z-10
                sm:text-sm
              "
              placeholder="Password"
              v-model="password"
            />
          </div>
        </div>

        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <input
              id="remember-me"
              name="remember-me"
              type="checkbox"
              class="
                h-4
                w-4
                text-indigo-600
                focus:ring-indigo-500
                border-gray-300
                rounded
              "
            />
            <label for="remember-me" class="ml-2 block text-sm text-gray-900">
              Remember me
            </label>
          </div>

          <div class="text-sm">
            <a
              href="#"
              class="font-medium text-indigo-600 hover:text-indigo-500"
            >
              Forgot your password?
            </a>
          </div>
        </div>

        <div>
          <button
            class="p-3 bg-red-500 text-white w-full"
            @click="signInWithGoogle"
          >
            Google
          </button>
          <button
            class="p-3 bg-black text-white w-full mb-5"
            @click="signInWithGithub"
          >
            Github
          </button>
          <button
            type="submit"
            @click="login"
            class="
              group
              relative
              w-full
              flex
              justify-center
              py-2
              px-4
              border border-transparent
              text-sm
              font-medium
              rounded-md
              text-white
              bg-indigo-600
              hover:bg-indigo-700
              focus:outline-none
              focus:ring-2
              focus:ring-offset-2
              focus:ring-indigo-500
            "
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="w-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="2"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"
              />
            </svg>
            <p class="px-1 text-md">
              Sign in
            </p>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { loginMutation, logoutMutation } from "../scripts/gqlMutations";
import {
  GoogleAuthProvider,
  GithubAuthProvider,
  getAuth,
  signInWithPopup,
} from "firebase/auth";

export default defineComponent({
  data() {
    return {
      auth: false,
      email: "",
      password: "",
    };
  },
  methods: {
    signInWithGithub() {
      const auth = getAuth();
      const provider = new GithubAuthProvider();
      signInWithPopup(auth, provider).then(async (result) => {
        // TODO: send request to server to check account status
        console.warn("*************************");
        console.warn(result);
        console.warn("*************************");
      });
    },
    signInWithGoogle() {
      const auth = getAuth();
      const provider = new GoogleAuthProvider();
      signInWithPopup(auth, provider).then(async (result) => {
        // TODO: send request to server to check account status
        console.warn("*************************");
        console.warn(result);
        console.warn("*************************");
      });
    },
    async login(e: any) {
      e.preventDefault();
      const { data, errors } = await this.$apollo.mutate({
        mutation: loginMutation,
        variables: {
          username: this.email,
          password: this.password,
        },
      });

      if (!errors) {
        this.$store.commit("setToken", !!data.baseUserLogin.token);
        window.location.href = "http://" + window.location.host + "/dashboard";
      } else {
        console.log("errorrrr", errors);
      }
    },
  },
});
</script>
