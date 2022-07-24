<template>
  <div class="" v-if="company">
    <div class="bg-white m-0 w-full h-20 flex flex-row gap-20 px-2">
      <div class="flex flex-row p-2 gap-4">
        <div>
          <p class="pb-2">Activity</p>
          <div class="flex flex-row gap-3">
            <div class="flex flex-row gap-1">
              <chip
                :text="company.companyStatus.name"
                :color="company.companyStatus.color.hex"
              ></chip>
            </div>
          </div>
        </div>
      </div>
      <div>
        <p class="pb-2">Website</p>
        <div class="flex flex-row gap-2 mt-2">
          <p v-if="company.website">
            <a target="_blank" class="text-blue-500" :href="company.website">{{
              company.website
            }}</a>
          </p>
        </div>
      </div>
      <div>
        <p class="pb-2">Address</p>
        <div class="flex flex-row gap-2 mt-2">
          <p>{{ formAddress(company.address) }}</p>
        </div>
      </div>
      <div>
        <p class="pb-2">owner</p>
        <div class="flex flex-row gap-2 mt-2">
          <p>{{ company.owner.firstName }} {{ company.owner.lastName }}</p>
        </div>
      </div>
    </div>
    <!-- start of tabs -->
    <div class="grid gap-3 lg:grid-cols-2 xl:grid-cols-2 m-5">
      <div class="flex flex-col">
        <div>
          <company-primary-card
            @updated="companyPrimaryUpdated"
            :data="company"
          ></company-primary-card>
          <company-details-card :data="company"></company-details-card>
        </div>
      </div>
      <div>
        <company-activity-feed></company-activity-feed>
        <company-joborder-card></company-joborder-card>
        <companies-attachments-card></companies-attachments-card>
      </div>
    </div>
    <div class="m-5 xl:w-3/4 lg:w-3/4">
      <company-contacts-card :data="company"></company-contacts-card>
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
import { COMPANY } from "../../queries/company";
import { formAddress } from "../../utils/helpers";

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
  data: () => ({
    company: null as any,
  }),
  async created() {
    await this.fetchCompany();
  },
  methods: {
    formAddress,
    async fetchCompany() {
      const { data } = await this.$apollo.query({
        query: COMPANY,
        fetchPolicy: "network-only",
        variables: {
          cid: this.$route.params.cpid,
        },
      });
      if (data) {
        this.company = data.company;
      }
    },
    async companyPrimaryUpdated() {
      await this.fetchCompany();
    },
  },
});
</script>