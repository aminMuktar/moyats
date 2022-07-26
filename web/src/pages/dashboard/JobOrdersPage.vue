<template>
  <div class="">
    <div
      class="bg-white m-0 w-full h-20 flex flex-row gap-20 px-2 pt-2"
      v-if="joborder"
    >
      <div class="flex flex-row gap-4">
        <div>
          <p class="pb-2">status</p>
          <chip
            @click="toggleStatusSlider('joborder', joborder.joborderId)"
            :text="joborder.jobOrderStatus.statusName"
            :color="joborder.jobOrderStatus.color.hex"
          ></chip>
        </div>
      </div>
      <div>
        <p class="pb-2">Location</p>
        <div class="flex flex-row gap-2 mt-2">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"
            />
          </svg>
          <p>{{ formAddress(joborder.jobDetail.location) }}</p>
        </div>
      </div>
      <div>
        <p class="pb-2">Activity</p>
        <div class="flex flex-row gap-2 mt-2">
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
              >4</span
            >
            <p>Candidates</p>
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
              >4</span
            >
            <p>Submitted</p>
          </div>
        </div>
      </div>

      <div>
        <p class="pb-2">Company</p>
        <div class="flex flex-row gap-2 mt-2">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              fill-rule="evenodd"
              d="M4 4a2 2 0 012-2h8a2 2 0 012 2v12a1 1 0 110 2h-3a1 1 0 01-1-1v-2a1 1 0 00-1-1H9a1 1 0 00-1 1v2a1 1 0 01-1 1H4a1 1 0 110-2V4zm3 1h2v2H7V5zm2 4H7v2h2V9zm2-4h2v2h-2V5zm2 4h-2v2h2V9z"
              clip-rule="evenodd"
            />
          </svg>

          <p>{{ joborder.company.name }}</p>
        </div>
      </div>
      <div>
        <p class="pb-2">Owner</p>
        <div class="flex flex-row gap-2 mt-2">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              fill-rule="evenodd"
              d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
              clip-rule="evenodd"
            />
          </svg>
          <p>
            <span>{{ joborder.owner.firstName }}</span>
            <span>{{ joborder.owner.lastName }}</span>
          </p>
        </div>
      </div>
    </div>
    <div class="grid gap-3 lg:grid-cols-2 xl:grid-cols-2 m-5">
      <div class="flex flex-col">
        <div v-if="joborder">
          <joborder-primary-card
            :loading="loading"
            :data="joborder"
            @updated="parseJobOrder()"
          ></joborder-primary-card>
          <joborder-details
            :loading="loading"
            :data="joborder"
            @updated="parseJobOrder()"
          ></joborder-details>
          <joborder-company-card
            @updated="parseJobOrder()"
            :data="joborder"
          ></joborder-company-card>
          <job-order-description-card
            @updated="parseJobOrder()"
            :data="joborder"
          ></job-order-description-card>
          <joborder-notes
            :data="joborder"
            @updated="parseJobOrder()"
          ></joborder-notes>
          <joborder-application-card
            :data="joborder"
          ></joborder-application-card>
        </div>
      </div>
      <div>
        <joborder-activity-feed-card></joborder-activity-feed-card>
        <joborder-attachments></joborder-attachments>
        <joborder-review-process-card></joborder-review-process-card>
      </div>
    </div>
    <div class="m-5 xl:w-3/4 lg:w-3/4">
      <joborder-pipeline-card></joborder-pipeline-card>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import Chip from "../../components/widgets/Chip.vue";
import JoborderPrimaryCard from "../../components/joborders/JoborderPrimaryCard.vue";
import JoborderDetails from "../../components/joborders/JoborderDetails.vue";
import JoborderCompanyCard from "../../components/joborders/JoborderCompanyCard.vue";
import JobOrderDescriptionCard from "../../components/joborders/JobOrderDescriptionCard.vue";
import JoborderNotes from "../../components/joborders/JoborderNotes.vue";
import JoborderApplicationCard from "../../components/joborders/JoborderApplicationCard.vue";
import JoborderPipelineCard from "../../components/joborders/JoborderPipelineCard.vue";
import JoborderActivityFeedCard from "../../components/joborders/JoborderActivityFeedCard.vue";
import JoborderAttachments from "../../components/joborders/JoborderAttachments.vue";
import JoborderReviewProcessCard from "../../components/joborders/JoborderReviewProcessCard.vue";
import { JOB_ORDER } from "../../queries/joborder";
import { formAddress, toggleStatusSlider } from "../../utils/helpers";

export default defineComponent({
  components: {
    Chip,
    JoborderPrimaryCard,
    JoborderDetails,
    JoborderCompanyCard,
    JobOrderDescriptionCard,
    JoborderNotes,
    JoborderApplicationCard,
    JoborderPipelineCard,
    JoborderActivityFeedCard,
    JoborderAttachments,
    JoborderReviewProcessCard,
  },
  setup() {},
  data: () => ({
    joborder: null as any,
    loading: false,
  }),
  async created() {
    await this.parseJobOrder();
  },
  computed: {
    getFormupdateStatus() {
      this.parseJobOrder();
      return this.$store.getters.getFormupdateStatus;
    },
  },
  watch: {
    getFormupdateStatus(value) {
      if (value) {
        this.parseJobOrder();
      }
    },
  },
  methods: {
    formAddress,
    toggleStatusSlider,
    async parseJobOrder() {
      this.loading = true;
      const { data } = await this.$apollo.query({
        query: JOB_ORDER,
        fetchPolicy: "network-only",
        variables: {
          id: this.$route.params.jid,
        },
      });
      if (data) {
        this.loading = false;
        this.joborder = data.jobOrder;
        this.$store.commit("setEntityTitle", { t: "jo", d: data.jobOrder });
      } else {
        this.loading = false;
      }
    },
  },
});
</script>
