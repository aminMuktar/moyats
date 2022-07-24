<template>
  <div
    class="flex right-0 z-50 mr-0 mt-1 absolute w-1/2 h-full justify-end"
    :class="{ 'z-0': !$store.state.core.activateSlider }"
  >
    <button
      v-if="showBtn"
      class="
        w-10
        h-10
        bg-white
        shadow-xl
        rounded
        flex
        justify-center
        items-center
        fixed
      "
      @click="sliderActivator()"
    >
      <svg
        v-if="$store.state.core.activeSlideWindow === 'joborders'"
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
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-5 w-5"
        viewBox="0 0 20 20"
        fill="currentColor"
        v-else-if="$store.state.core.activeSlideWindow === 'candidates'"
      >
        <path
          d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z"
        />
      </svg>

      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-5 w-5"
        viewBox="0 0 20 20"
        fill="currentColor"
        v-else-if="$store.state.core.activeSlideWindow === 'contacts'"
      >
        <path
          d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z"
        />
      </svg>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-5 w-5"
        viewBox="0 0 20 20"
        fill="currentColor"
        v-else-if="$store.state.core.activeSlideWindow === 'companies'"
      >
        <path
          fill-rule="evenodd"
          d="M4 4a2 2 0 012-2h8a2 2 0 012 2v12a1 1 0 110 2h-3a1 1 0 01-1-1v-2a1 1 0 00-1-1H9a1 1 0 00-1 1v2a1 1 0 01-1 1H4a1 1 0 110-2V4zm3 1h2v2H7V5zm2 4H7v2h2V9zm2-4h2v2h-2V5zm2 4h-2v2h2V9z"
          clip-rule="evenodd"
        />
      </svg>
    </button>
    <transition name="nested">
      <div
        class="
          w-full
          sm:w-1/2
          md:w-1/2
          lg:w-1/2
          xl:w-1/2
          h-screen
          bg-white
          shadow-lg shadow-black-500/50
          fixed
        "
        v-show="$store.state.core.activateSlider"
      >
        <div class="flex justify-between bg-gray-100">
          <p
            class="pt-3 px-2 border-b"
            v-if="$store.state.core.activeSlideWindow === 'joborders'"
          >
            Create a JobOrder
          </p>
          <p
            class="pt-3 px-2 border-b"
            v-if="$store.state.core.activeSlideWindow === 'candidates'"
          >
            Add a Candidate
          </p>
          <p
            class="pt-3 px-2 border-b"
            v-if="$store.state.core.activeSlideWindow === 'contacts'"
          >
            Add a new Contact
          </p>
          <p
            class="pt-3 px-2 border-b"
            v-if="$store.state.core.activeSlideWindow === 'companies'"
          >
            Add a new company
          </p>
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
        <div class="overflow-y-scroll" style="height: 100%">
          <job-order-form
            @close="closeSlider"
            v-if="$store.state.core.activeSlideWindow === 'joborders'"
            @joborderadded="closeSlider"
          ></job-order-form>
          <candidates-form
            @joborderadded="closeSlider"
            @close="closeSlider"
            v-else-if="$store.state.core.activeSlideWindow === 'candidates'"
          ></candidates-form>
          <companies-form
            @companyAdded="closeSlider"
            @close="closeSlider"
            v-else-if="$store.state.core.activeSlideWindow === 'companies'"
          ></companies-form>
          <contacts-form
            @contactAdded="closeSlider"
            @close="closeSlider"
            v-else-if="$store.state.core.activeSlideWindow === 'contacts'"
          ></contacts-form>
        </div>
      </div>
    </transition>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import JobOrderForm from "../joborders/JobOrderForm.vue";
import CompaniesForm from "../companies/CompaniesForm.vue";
import CandidatesForm from "../candidates/CandidatesForm.vue";
import ContactsForm from "../contacts/ContactsForm.vue";

export default defineComponent({
  data() {
    return {
      showBtn: true,
      title: "",
    };
  },
  cretated() {
    console.log(this.title);
  },
  methods: {
    cleanUp() {
      this.$store.commit("setScompany", null);
    },
    closeSlider() {
      this.$store.commit("setActivateSlider", false);
      this.cleanUp();
      setTimeout(() => {
        this.showBtn = true;
      }, 150);
    },
    sliderActivator() {
      const sliderStat = this.$store.state.core.activateSlider;
      this.$store.commit("setActivateSlider", !sliderStat);
      if (sliderStat) this.showBtn = false;
    },
  },
  components: { JobOrderForm, CompaniesForm, CandidatesForm, ContactsForm },
});
</script>

<style scoped>
.nested-enter-active,
.nested-leave-active {
  transition: all 0.3s ease-in-out;
}
/* delay leave of parent element */
.nested-leave-active {
  transition-delay: 0.002s;
}

.nested-enter-from,
.nested-leave-to {
  transform: translateX(50px);
  opacity: 0;
}

/* we can also transition nested elements using nested selectors */
.nested-enter-active .inner,
.nested-leave-active .inner {
  transition: all 0.003s ease-in-out;
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
