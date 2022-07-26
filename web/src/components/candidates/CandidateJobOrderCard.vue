<template>
  <div>
    <dashboard-card-widget>
      <template v-slot:header>
        <p class="p-3 font-semibold text-lg">Job Orders</p>
      </template>
      <template v-slot:body>
        <div class="z-auto">
          <div
            class="sm:col-span-1 md:flex lg:flex p-2"
            v-if="candJoborders.length"
          >
            <div
              class="text-sm w-full lg:w-3/4 xl:w-3/4"
              v-for="(cand, ix) in candJoborders"
              :key="ix"
            >
              <div class="flex">
                <div class="flex flex-row gap-10">
                  <div class="bg-gray-100 w-8 h-8 m-2">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-full w-full"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                    >
                      <path
                        fill-rule="evenodd"
                        d="M4 4a2 2 0 012-2h8a2 2 0 012 2v12a1 1 0 110 2h-3a1 1 0 01-1-1v-2a1 1 0 00-1-1H9a1 1 0 00-1 1v2a1 1 0 01-1 1H4a1 1 0 110-2V4zm3 1h2v2H7V5zm2 4H7v2h2V9zm2-4h2v2h-2V5zm2 4h-2v2h2V9z"
                        clip-rule="evenodd"
                      />
                    </svg>
                  </div>
                  <div class="flex flex-col">
                    <router-link
                      :to="`/joborders/${cand.joborder.joborderId}`"
                      class="font-bold text-blue-500"
                    >
                      {{ cand.joborder.jobDetail.title }}
                    </router-link>
                    <router-link
                      :to="`/companies/${cand.joborder.company.companyId}`"
                      class="text-blue-500"
                    >
                      {{ cand.joborder.company.name }}
                    </router-link>
                  </div>
                  <div>
                    <chip
                      class="mt-2"
                      :text="cand.status.statusName"
                      :color="cand.status.color.hex"
                    ></chip>
                  </div>
                </div>
              </div>
              <!-- {{ cand }} -->
            </div>
          </div>
          <p class="text-center py-5" v-else>
            Candidate hasn't applied to any job orders
          </p>
        </div>
      </template>
    </dashboard-card-widget>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { candidateApplicationJoborders } from "../../services/candidates";
import DashboardCardWidget from "../DashboardCardWidget.vue";
import Chip from "../widgets/Chip.vue";

export default defineComponent({
  components: { DashboardCardWidget, Chip },
  props: ["data"],
  async created() {
    await this.fetchCandidateApplicationJoborderss();
  },
  data: () => ({
    page: 1,
    pageSize: 10,
    candJoborders: [] as any,
  }),
  methods: {
    async fetchCandidateApplicationJoborderss() {
      const {
        data: {
          candidateApplicantJoborders: { objects },
        },
      } = await candidateApplicationJoborders({
        candidate: this.data.candidateId,
        page: this.page,
        pageSize: this.pageSize,
      });
      this.candJoborders = objects;
    },
  },
});
</script>
