<template>
  <div class="">
    <div class="bg-white m-0 w-full h-20 flex flex-row gap-20 px-2">
      <div class="flex flex-row p-2 gap-4">
        <div>
          <p class="pb-2">Activity</p>
          <div class="flex flex-row gap-3">
            <div class="flex flex-row gap-1">
              <span
                class="
                  text-white
                  p-1
                  h-6
                  w-6
                  text-center text-xs
                  rounded-full
                  bg-orange-500
                "
                v-text="1"
              ></span>
              <p>pipeline</p>
            </div>
            <div class="flex flex-row gap-1">
              <span
                class="
                  text-white
                  p-1
                  h-6
                  w-6
                  text-center text-xs
                  rounded-full
                  bg-orange-500
                "
                v-text="12"
              ></span>
              <p>Submitted</p>
            </div>
          </div>
        </div>
      </div>
      <div>
        <p class="pb-2">Phones</p>
        <div class="flex flex-row gap-2 mt-2">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z"
            />
          </svg>
          <p>+251911359586</p>
        </div>
      </div>
      <div>
        <p class="pb-2">E-mail</p>
        <div class="flex flex-row gap-2 mt-2">
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
              d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207"
            />
          </svg>
          <p>bdere12345@gmail.com</p>
        </div>
      </div>
    </div>
    <!-- start of tabs -->
    <div class="grid gap-3 lg:grid-cols-2 xl:grid-cols-2 m-5">
      <div class="flex flex-col">
        <div>
          <company-primary-card></company-primary-card>
          <company-details-card></company-details-card>
        </div>
      </div>
      <div>
        <company-activity-feed></company-activity-feed>
        <company-joborder-card></company-joborder-card>
        <companies-attachments-card></companies-attachments-card>
      </div>
    </div>
    <div class="m-5 xl:w-3/4 lg:w-3/4">
      <company-contacts-card></company-contacts-card>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import CompaniesAttachmentsCard from "../../components/companies/CompaniesAttachmentsCard.vue";
import CompanyActivityFeed from "../../components/companies/CompanyActivityFeed.vue";
import CompanyContactsCard from "../../components/companies/CompanyContactsCard.vue";
import CompanyDetailsCard from "../../components/companies/CompanyDetailsCard.vue";
import CompanyJoborderCard from "../../components/companies/CompanyJoborderCard.vue";
import CompanyPrimaryCard from "../../components/companies/CompanyPrimaryCard.vue";
import DashboardCardWidget from "../../components/DashboardCardWidget.vue";
import Chip from "../../components/widgets/Chip.vue";

export default defineComponent({
  components: {
    Chip,
    DashboardCardWidget,
    CompanyPrimaryCard,
    CompanyDetailsCard,
    CompanyActivityFeed,
    CompanyJoborderCard,
    CompaniesAttachmentsCard,
    CompanyContactsCard,
  },
  setup() {},
  data: () => ({}),
});
</script>