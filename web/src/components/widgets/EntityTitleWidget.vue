<template>
  <div
    class="relative lg:mx-0 flex flex-row"
    v-if="$store.state.core.entityTitle"
  >
    <div class="flex flex-row gap-2">
      <p
        class="
          font-bold
          text-2xl
          px-3
          py-1
          cursor-pointer
          bg-red-600
          rounded-full
          border-4
          text-red-300
        "
      >
        <span v-if="$store.state.core.entityTitle.t == 'ca'">
          {{
            firsLetter(
              $store.state.core.entityTitle.d.candidateProfile.firstName
            )
          }}
        </span>
        <span v-else-if="$store.state.core.entityTitle.t == 'co'">
          {{ firsLetter($store.state.core.entityTitle.d.name) }}
        </span>
        <span v-else-if="$store.state.core.entityTitle.t == 'jo'">
          {{ firsLetter($store.state.core.entityTitle.d.jobDetail.title) }}
        </span>
        <span v-else-if="$store.state.core.entityTitle.t == 'ct'">
          {{ firsLetter($store.state.core.entityTitle.d.firstName) }}
        </span>
      </p>
      <div v-if="$store.state.core.entityTitle.t == 'ca'">
        <div v-if="editMode" class="flex flex-row gap-2">
          <input
            v-model="first"
            required
            class="
              w-32
              p-1
              text-xl
              font-bold
              border-gray-200 border-2
              rounded-md
              mt-1
            "
            placeholder="First Name"
            type="name"
            id="name"
          />
          <input
            v-model="last"
            required
            class="
              w-32
              p-1
              text-xl
              font-bold
              border-gray-200 border-2
              rounded-md
              mt-1
            "
            placeholder="First Name"
            type="name"
            id="name"
          />
        </div>

        <p class="font-bold text-2xl pt-2" v-else>
          {{ first }}
          {{ last }}
        </p>
      </div>
      <div v-else-if="$store.state.core.entityTitle.t == 'ct'">
        <div v-if="editMode" class="flex flex-row gap-2">
          <input
            v-model="first"
            required
            class="
              w-32
              p-1
              text-xl
              font-bold
              border-gray-200 border-2
              rounded-md
              mt-1
            "
            placeholder="First Name"
            type="name"
            id="name"
          />
          <input
            v-model="last"
            required
            class="
              w-32
              p-1
              text-xl
              font-bold
              border-gray-200 border-2
              rounded-md
              mt-1
            "
            placeholder="First Name"
            type="name"
            id="name"
          />
        </div>

        <p class="font-bold text-2xl pt-2" v-else>
          {{ first }}
          {{ last }}
        </p>
      </div>
      <div v-else-if="$store.state.core.entityTitle.t == 'co'">
        <input
          v-model="name"
          required
          class="
            w-full
            p-1
            text-xl
            font-bold
            border-gray-200 border-2
            rounded-md
            mt-1
          "
          placeholder="First Name"
          type="name"
          id="name"
          v-if="editMode"
        />
        <p class="font-bold text-2xl pt-2" v-else>
          {{ name }}
        </p>
      </div>
      <div
        class="font-bold text-2xl pt-1"
        v-else-if="$store.state.core.entityTitle.t == 'jo'"
      >
        <input
          v-model="name"
          required
          class="
            w-full
            p-1
            text-xl
            font-bold
            border-gray-200 border-2
            rounded-md
            mt-1
          "
          placeholder="First Name"
          type="name"
          id="name"
          v-if="editMode"
        />
        <p class="font-bold text-2xl pt-2" v-else>
          {{ name }}
        </p>
      </div>
    </div>

    <button
      v-if="!editMode"
      @click="editMode = true"
      class="
        text-gray-700
        bg-gray-100
        focus:ring-4 focus:outline-none focus:ring-blue-300
        font-medium
        rounded-lg
        text-sm
        p-0.5
        w-6
        border-2
        h-6
        mx-2
        mt-3
        text-center
        inline-flex
        items-center
      "
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-full w-full"
        viewBox="0 0 20 20"
        fill="currentColor"
      >
        <path
          d="M17.414 2.586a2 2 0 00-2.828 0L7 10.172V13h2.828l7.586-7.586a2 2 0 000-2.828z"
        />
        <path
          fill-rule="evenodd"
          d="M2 6a2 2 0 012-2h4a1 1 0 010 2H4v10h10v-4a1 1 0 112 0v4a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"
          clip-rule="evenodd"
        />
      </svg>
    </button>
    <button
      v-else
      @click="updateEntityTitle"
      class="
        text-gray-700
        bg-gray-100
        focus:ring-4 focus:outline-none focus:ring-blue-300
        font-medium
        rounded-lg
        text-sm
        p-0.5
        w-6
        border-2
        h-6
        mx-2
        mt-3
        text-center
        inline-flex
        items-center
      "
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-full w-full"
        viewBox="0 0 20 20"
        fill="currentColor"
      >
        <path
          fill-rule="evenodd"
          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
          clip-rule="evenodd"
        />
      </svg>
    </button>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { mapState } from "vuex";
import { updateJobOrderPrimary } from "../../services";
import {
  updateCandidatePrimary,
  updateCompanyPrimary,
  updateContactPrimary,
} from "../../services/candidates";

export default defineComponent({
  data: () => ({
    editMode: false,
    name: "",
    first: "",
    last: "",
  }),
  created() {
    if (this.$store.state.core.entityTitle) {
      // alert("sheesh");
    }
  },
  computed: mapState(["entityTitle"]),
  watch: {
    "$store.state.core.entityTitle": function () {
      if (this.$store.state.core.entityTitle) {
        const type = this.$store.state.core.entityTitle.t;
        // check type for copmany, contact,job or candidate profile and set name accordingly
        if (type === "co") {
          this.name = this.$store.state.core.entityTitle.d.name;
        } else if (type === "ct") {
          this.first = this.$store.state.core.entityTitle.d.firstName;
          this.last = this.$store.state.core.entityTitle.d.lastName;
        } else if (type === "jo") {
          this.name = this.$store.state.core.entityTitle.d.jobDetail.title;
        } else if (type === "ca") {
          this.first =
            this.$store.state.core.entityTitle.d.candidateProfile.firstName;
          this.last =
            this.$store.state.core.entityTitle.d.candidateProfile.lastName;
        }
      }
    },
  },
  methods: {
    // get first letter of string
    firsLetter(str: string) {
      return str.charAt(0);
    },
    updateCompanyTitle() {},
    async updateEntityTitle() {
      const type = this.$store.state.core.entityTitle.t;
      console.log(type, "ty");
      // check if type is company, contact, job or candidate profile
      if (type === "co") {
        await this.updateCompanyEntityTitle();
      } else if (type === "ct") {
        await this.updateContactEntityName();
      } else if (type === "jo") {
        await this.updateJobOrderEntityTitle();
      } else if (type === "ca") {
        await this.updateCandidateEntityName();
      }
    },
    async updateContactEntityName() {
      let contact = this.$store.state.core.entityTitle.d;
      const { data, errors }: any = await updateContactPrimary({
        input: {
          name: {
            firstName: this.first,
            lastName: this.last,
          },
          contact: contact.companyContactId,
          phones: {
            cellPhone: contact.phones.cellNumber,
            homePhone: contact.phones.homeNumber,
            workPhone: contact.phones.workNumber,
          },
          city: contact.address.city,
          country: contact.address.country,
          state: contact.address.state,
        },
      });
      if (data) {
        this.editMode = false;
      }
    },
    async updateCandidateEntityName() {
      let candidate = this.$store.state.core.entityTitle.d;
      const { data, errors } = await updateCandidatePrimary({
        candidate: candidate.candidateId,
        input: {
          phones: {
            cellNumber: candidate.phones.cellNumber,
            homeNumber: candidate.phones.homeNumber,
            workNumber: candidate.phones.workNumber,
          },
          candidateProfile: {
            firstName: this.first,
            lastName: this.last,
            email: candidate.candidateProfile.email,
          },
          country: candidate.address.country,
          city: candidate.address.city,
        },
      });
      if (data) {
        this.editMode = false;
      }
    },
    async updateJobOrderEntityTitle() {
      let joborder = this.$store.state.core.entityTitle.d;
      console.log(joborder, "job order");
      const { data, errors } = await updateJobOrderPrimary({
        input: {
          title: this.name,
          city: joborder.jobDetail.location.city,
          country: joborder.jobDetail.location.country,
          recruiter: joborder.jobDetail.recruiter.orgMemberId,
        },
        joborder: joborder.joborderId,
      });
      if (data) {
        this.editMode = false;
      }
    },
    async updateCompanyEntityTitle() {
      let company = this.$store.state.core.entityTitle.d;
      const { data } = await updateCompanyPrimary({
        input: {
          phones: {
            cellPhone: company.phones.cellNumber,
            homePhone: company.phones.homeNumber,
            workPhone: company.phones.workNumber,
          },
          city: company.address.city,
          country: company.address.country,
          state: company.address.state,
          company: company.companyId,
          name: this.name,
          website: company.website,
        },
      });
      if (data) {
        this.editMode = false;
      }
    },
  },
});
</script>
