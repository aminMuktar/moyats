<template>
  <div>
    <main-header class="fixed w-full" />
    <div>
      <section class="bg-white">
        <div class="max-w-screen-xl px-4 py-16 mx-auto sm:px-6 lg:px-8">
          <center>
            <div
              class="
                p-8
                mt-10
                bg-white
                rounded-lg
                border-2 border-gray-100
                lg:p-12 lg:col-span-3
                xl:w-1/2
                lg:w-1/2
                md:w-3/4
              "
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-14 w-14 text-blue-700"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fill-rule="evenodd"
                  d="M4 4a2 2 0 012-2h8a2 2 0 012 2v12a1 1 0 110 2h-3a1 1 0 01-1-1v-2a1 1 0 00-1-1H9a1 1 0 00-1 1v2a1 1 0 01-1 1H4a1 1 0 110-2V4zm3 1h2v2H7V5zm2 4H7v2h2V9zm2-4h2v2h-2V5zm2 4h-2v2h2V9z"
                  clip-rule="evenodd"
                />
              </svg>
              <p class="text-xl lg:text-3xl xl:text-3xl py-10">
                Register your organization
              </p>
              <form @submit="formSubmitted" class="space-y-4">
                <div
                  class="
                    grid grid-cols-1
                    gap-4
                    lg:grid-cols-3
                    md:grid-cols-3
                    xl:grid-cols-3
                  "
                >
                  <div>
                    <label class="sr-only" for="name">First Name</label>
                    <input
                      v-model="firstName"
                      required
                      class="
                        w-full
                        p-3
                        text-sm
                        border-gray-200 border-2
                        rounded-lg
                      "
                      placeholder="First Name"
                      type="text"
                      id="name"
                    />
                  </div>
                  <div>
                    <label class="sr-only" for="name">Middle Name</label>
                    <input
                      v-model="middleName"
                      required
                      class="
                        w-full
                        p-3
                        text-sm
                        border-gray-200 border-2
                        rounded-lg
                      "
                      placeholder="Middle Name"
                      type="text"
                      id="name"
                    />
                  </div>

                  <div>
                    <label class="sr-only" for="name">Last Name</label>
                    <input
                      v-model="lastName"
                      required
                      class="
                        w-full
                        p-3
                        text-sm
                        border-gray-200 border-2
                        rounded-lg
                      "
                      placeholder="LastName"
                      type="text"
                      id="name"
                    />
                  </div>
                </div>

                <div>
                  <label class="sr-only" for="phone">Phone</label>
                  <vue-tel-input
                    v-bind="bindProps"
                    v-model="phone"
                  ></vue-tel-input>
                </div>
                <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
                  <div>
                    <label class="sr-only" for="orgname"
                      >Organization Name</label
                    >
                    <input
                      v-model="orgName"
                      required
                      class="
                        w-full
                        p-3
                        text-sm
                        border-gray-200
                        rounded-lg
                        border-2
                      "
                      placeholder="Organization Name"
                      type="tel"
                      id="orgname"
                    />
                  </div>
                  <div>
                    <label class="sr-only" for="phone">Organization Type</label>
                    <select
                      v-model="orgType"
                      required
                      class="
                        w-full
                        p-3
                        text-sm
                        border-gray-200
                        rounded-lg
                        border-2
                      "
                    >
                      <option value="" class="text-gray-400" disabled selected>
                        Company type
                      </option>
                      <option
                        :value="ty.v"
                        v-for="(ty, idx) in types"
                        :key="idx"
                      >
                        {{ ty.lbl }}
                      </option>
                    </select>
                  </div>
                </div>

                <div>
                  <label class="sr-only" for="subdomain">Subdomain</label>
                  <input
                    v-model="subdomain"
                    required
                    class="
                      w-full
                      p-3
                      text-sm
                      border-gray-200
                      rounded-lg
                      border-2
                    "
                    placeholder="Subdomain"
                    type="text"
                  />
                </div>

                <div class="mt-4">
                  <button
                    type="submit"
                    class="
                      inline-flex
                      items-center
                      justify-center
                      w-full
                      px-5
                      py-3
                      text-white
                      bg-black
                      rounded-lg
                      sm:w-auto
                    "
                  >
                    <span class="font-medium"> Finish Registration </span>

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
import { ACCOUNT_SETUP } from "../queries/auth";

export default defineComponent({
  components: { MainHeader },
  data: () => ({
    phone: null,
    firstName: "",
    lastName: "",
    middleName: "",
    subdomain: "",
    orgName: "",
    orgType: "",
    bindProps: {
      mode: "international",
      defaultCountry: "ET",
      disabledFetchingCountry: false,
      disabled: false,
      disabledFormatting: false,
    },
    types: [
      { v: "hr", lbl: "Hr Recruitment Firm" },
      { v: "cm", lbl: "Company" },
      { v: "st", lbl: "Startup" },
    ],
  }),
  methods: {
    phoneInputInvalid(e: any) {
      e.target.setCustomValidity("Phone number is incorrect");
    },
    formSubmitted(e: any) {
      e.preventDefault();
      if (this.phone == "") {
        alert("bitch about it");
        return;
      }
      this.setupAccount();
      console.log(this.phone);
    },
    setupAccount() {
      this.$apollo
        .mutate({
          mutation: ACCOUNT_SETUP,
          variables: {
            input: {
              firstName: this.firstName,
              lastName: this.lastName,
              middleName: this.middleName,
              phoneNumber: this.phone,
              orgType: this.orgType,
              orgName: this.orgName,
              subdomain: this.subdomain,
            },
          },
        })
        .then(({ data, errors }) => {
          if (data) {
            let nstate = this.$store.state.core.u;
            nstate.setupComplete = true;
            this.$store.commit("saveUdata", nstate);
            setTimeout(() => {
              this.$router.push("/dashboard");
            }, 100);
          }
        })
        .catch((e) => {
          alert(e.message)
        });
    },
  },
  setup() {},
});
</script>
