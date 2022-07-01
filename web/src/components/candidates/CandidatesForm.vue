<template>
  <div class="flex w-full flex-col">
    <div
      class="flex flex-col rounded-lg overflow-hidden bg-white shadow relative"
    >
      <!-- loading overlay -->

      <div
        v-if="loadingState"
        class="
          absolute
          bg-white bg-opacity-60
          z-10
          h-full
          w-full
          flex
          items-start
          justify-center
        "
      >
        <spinner style="margin-top: 40%"></spinner>
      </div>
      <form class="w-full" ref="form" @submit="saveChanges">
        <div class="flex p-2 border-b-2 flex-row w-full fixed gap-2 bg-white">
          <button
            type="submit"
            class="
              bg-green-500
              p-2
              text-white
              rounded-md
              tracking-wider
              hover:bg-green-600
            "
          >
            Save Changes
          </button>
          <button
            @click="$emit('close')"
            class="
              border-red-500
              p-2
              border-2
              text-red-700
              rounded-md
              tracking-wider
              hover:bg-red-100
            "
          >
            Cancel
          </button>
        </div>
        <div class="grid grid-cols-1 w-full">
          <div class="flex col-span-2 w-full p-4 mt-16">
            <div class="w-56">
              <label class="sr-only" for="name">Title</label>
              <span class="m-1">Name* </span>
            </div>
            <div class="w-full grid lg:grid-cols-3 xl:grid-cols-3 gap-3 ml-9">
              <input
                required
                v-model="firstName"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="First Name"
                type="text"
                id="name"
              />
              <input
                required
                v-model="middleName"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="Middle Name"
                type="text"
                id="name"
              />
              <input
                required
                v-model="lastName"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="Last Name"
                type="text"
                id="name"
              />
            </div>
          </div>
          <div class="flex col-span-2 p-2">
            <div class="w-56">
              <label class="sr-only" for="name">Email</label>
              <span class="m-3 w-full">Email*</span>
            </div>
            <div class="flex gap-0 w-full ml-12 mr-2">
              <input
                pattern="^[w-.]+@([w-]+.)+[w-]{2,4}$"
                required
                v-model="email"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="Email"
                type="email"
                id="email"
              />
            </div>
          </div>
          <div class="flex col-span-2 w-full p-4">
            <div class="w-56">
              <label class="sr-only" for="name">Phones</label>
              <span class="m-1">Phones* </span>
            </div>
            <div class="w-full grid lg:grid-cols-2 xl:grid-cols-2 gap-3 ml-10">
              <input
                v-model="cellNumber"
                required
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                type="tel"
                pattern="(\+\s*2\s*5\s*1\s*9\s*(([0-9]\s*){8}\s*))|(0\s*9\s*(([0-9]\s*){8}))"
                placeholder="Cell Number"
                id="name"
              />
              <input
                v-model="homeNumber"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="Home Number"
                type="tel"
                pattern="(\+\s*2\s*5\s*1\s*9\s*(([0-9]\s*){8}\s*))|(0\s*9\s*(([0-9]\s*){8}))"
                id="name"
              />
              <input
                v-model="workNumber"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="Work Number"
                type="tel"
                pattern="(\+\s*2\s*5\s*1\s*9\s*(([0-9]\s*){8}\s*))|(0\s*9\s*(([0-9]\s*){8}))"
                id="name"
              />
            </div>
          </div>
          <div class="flex col-span-2 w-full p-4">
            <div class="w-56">
              <label class="sr-only" for="name">Social Medias</label>
              <span class="m-1">Social Medias </span>
            </div>
            <div class="w-full grid lg:grid-cols-2 xl:grid-cols-2 gap-3 ml-10">
              <input
                v-model="linkedin"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="LinkedIn"
                pattern="^((https?|ftp|smtp):\/\/)?(www.)?[a-z0-9]+\.[a-z]+(\/[a-zA-Z0-9#]+\/?)*$"
                id="name"
              />
              <input
                v-model="github"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="GitHub"
                pattern="^((https?|ftp|smtp):\/\/)?(www.)?[a-z0-9]+\.[a-z]+(\/[a-zA-Z0-9#]+\/?)*$"
                id="name"
              />
              <input
                v-model="twitter"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="Twitter"
                pattern="^((https?|ftp|smtp):\/\/)?(www.)?[a-z0-9]+\.[a-z]+(\/[a-zA-Z0-9#]+\/?)*$"
                type="text"
                id="name"
              />
            </div>
          </div>
          <div class="flex col-span-2 p-2">
            <div class="w-56">
              <label class="sr-only" for="name">Location</label>
              <span class="m-3 w-full">Location*</span>
            </div>
            <div class="grid grid-cols-3 gap-2">
              <input
                required
                v-model="city"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="City"
                type="text"
                id="name"
              />
              <input
                v-model="state"
                required
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="State"
                type="text"
                id="name"
              />
              <input
                required
                v-model="country"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="Country"
                type="text"
                id="name"
              />
            </div>
          </div>
          <div class="flex col-span-2 w-full p-2">
            <label class="sr-only" for="name">Source</label>
            <div class="w-52">
              <span class="m-3">Source*</span>
            </div>
            <select
              required
              class="
                p-2
                text-sm
                border-gray-200 border-2
                rounded-md
                text-gray-600
              "
              v-model="source"
              placeholder="Title"
              id="name"
            >
              <option
                :value="src.id"
                v-for="(src, ix) in candSources"
                :key="ix"
                v-text="src.name"
              ></option>
            </select>
          </div>
          <div class="col-span-1 flex flex-col p-2 border-t-2 mr-10">
            <label class="p-3" for="">Key Skills</label>
            <textarea
              v-model="keySkills"
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
              placeholder="Your message..."
            ></textarea>
          </div>
          <div class="col-span-2 flex p-2">
            <div class="w-52">
              <label class="sr-only" for="name"></label>
              <span class="m-3">Current Employeer </span>
            </div>
            <div>
              <input
                v-model="currentEmployeer"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="Current Employeer"
                type="text"
                id="name"
              />
            </div>
          </div>

          <div class="col-span-2 flex p-2">
            <div class="w-52">
              <label class="sr-only" for="name"></label>
              <span class="m-3">Current Pay </span>
            </div>
            <div>
              <input
                v-model="currentPay"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="Current Pay"
                type="text"
                id="name"
              />
            </div>
          </div>
          <div class="col-span-2 flex p-2">
            <div class="w-52">
              <label class="sr-only" for="name"></label>
              <span class="m-3">Desired Pay </span>
            </div>
            <div>
              <input
                v-model="desiredPay"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="Desired pay"
                type="text"
                id="name"
              />
            </div>
          </div>
          <div class="col-span-2 flex p-2">
            <div class="w-52">
              <label class="sr-only" for="name"></label>
              <span class="m-3">Best Time to Call </span>
            </div>
            <div>
              <input
                v-model="bestTimeToCall"
                class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                placeholder="Best Time to call"
                type="text"
                id="name"
              />
            </div>
          </div>
          <div class="col-span-1 flex flex-col p-2 border-t-2 mr-10">
            <label class="p-3" for="">Notes</label>
            <textarea
              v-model="notes"
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
              placeholder="Notes ..."
            ></textarea>
          </div>
          <div class="col-span-2 flex p-2">
            <div class="w-full flex flex-row mx-2 justify-between">
              <span class="m-3">Attachments</span>
              <button
                class="border-2 p-2"
                type="button"
                @click="$refs.attachment.click()"
              >
                Add Attachment
              </button>
            </div>
          </div>
          <div class="items col-span-2 mx-5">
            <input
              type="file"
              class="hidden"
              ref="attachment"
              @change="attachmentUploaded"
            />
            <ul
              class="
                w-full
                text-sm
                font-medium
                text-gray-900
                bg-white
                border-b border-gray-200
                rounded-lg
              "
            >
              <li
                class="w-full px-4 py-2 border-t border-gray-200"
                v-for="(att, ix) in attachments"
                :key="ix"
              >
                <p>
                  {{ att.file.name }}
                </p>
              </li>
            </ul>
          </div>
          <div class="col-span-2 flex p-2 mb-52"></div>
        </div>
      </form>
    </div>
  </div>
</template>
<script lang="ts">
import { uuid } from "vue-uuid";
import { defineComponent } from "vue";
import { addCandidate, candidateSources } from "../../services/candidates";

export default defineComponent({
  setup() {},
  created() {
    this.fetchCandidateSources();
  },
  data: () => ({
    firstName: "",
    middleName: "",
    lastName: "",
    email: "",
    cellNumber: "",
    homeNumber: "",
    workNumber: "",
    linkedin: "",
    github: "",
    twitter: "",
    city: "",
    state: "",
    country: "",
    source: "",
    keySkills: "",
    currentEmployeer: "",
    currentPay: "",
    desiredPay: "",
    dateAvailable: "",
    bestTimeToCall: "",
    loadingState: false,
    candSources: [] as any,
    notes: "",
    emailre: "^[w-.]+@([w-]+.)+[w-]{2,4}$",
    phonere: "(+s*2s*5s*1s*9s*(([0-9]s*){8}s*))|(0s*9s*(([0-9]s*){8}))",
    attachments: [] as any,
  }),
  methods: {
    attachmentUploaded(e) {
      const files = e.target.files;
      const fr = new FileReader();
      fr.readAsDataURL(files[0]);
      fr.addEventListener("load", () => {
        this.attachments.push({ img: fr.result, file: files[0] });
      });
    },
    async fetchCandidateSources() {
      const { data } = await candidateSources();
      this.candSources = data.candidateSources;
    },
    async saveChanges(e) {
      e.preventDefault();
      this.loadingState = true;
      const { data, errors } = await addCandidate({
        input: {
          firstName: this.firstName,
          middleName: this.middleName,
          lastName: this.lastName,
          email: this.email,
          cellPhone: this.cellNumber,
          homePhone: this.homeNumber,
          workPhone: this.workNumber,
          socialMedias: [
            {
              link: "https://google.com",
              type: "fb",
            },
          ],
          country: this.country,
          city: this.city,
          source: this.source,
          keySkills: this.keySkills,
          currentEmployeer: this.currentEmployeer,
          currentPay: this.currentPay,
          dateAvailable: this.dateAvailable,
          desiredPay: this.desiredPay,
          bestContactTime: this.bestTimeToCall,
          qualifications: "",
        },
        attachments: this.attachments.map((e) => e.file),
      });
      if (!errors) {
        this.loadingState = false;
        this.$emit("joborderadded");
        this.$store.commit("updateFormupdateStatus", uuid.v4());
        this.$emit("close");
      } else {
        this.loadingState = false;
      }
    },
  },
});
</script>
