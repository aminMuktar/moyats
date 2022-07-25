<template>
  <div>
    <data-table
      @prev="prev"
      @next="next"
      :dropts="dropts"
      :hasNext="hasNext"
      :hasPrev="hasPrev"
      :total="total"
      :page="$route.query.page"
      :pageSize="pageSize"
      :pages="pages"
      empty-message="You don't have any activities yet."
      :items="activities"
      :headers="headers"
      @checkedAll="allChecked"
      @selected="singleSelected"
    >
      <template v-slot:[`date`]="{ item }">
        <div>
          <p v-text="parseDate(item.createdAt)"></p>
        </div>
      </template>
      <template v-slot:[`name`]="{ item }">
        <div>
          <!-- <pre>
            {{ item.contentObject }}
          </pre> -->
          <p>
            {{ item.user.firstName }}
            {{ item.user.firstName }}
          </p>
        </div>
      </template>
      <template v-slot:[`regarding`]="{ item }">
        <div>
          <!-- <pre>
            {{ item.contentObject }}
          </pre> -->
          <p
            v-if="item.activityType == 'OR'"
            v-text="item.contentObject.name"
          ></p>
          <router-link
            v-else-if="item.activityType == 'JO'"
            class="font-semibold text-blue-500"
            :to="`/joborders/${item.contentObject.joborder_id}`"
            v-text="item.contentObject.job_detail.title"
          ></router-link>
          <router-link
            v-else-if="item.activityType == 'CA'"
            class="font-semibold text-blue-500"
            :to="`/candidates/${item.contentObject.candidate_id}`"
            v-text="
              `${item.contentObject.candidate_profile.first_name} ${item.contentObject.candidate_profile.last_name}`
            "
          ></router-link>

          <p v-else-if="item.activityType == 'AC'">
            {{ item.contentObject.first_name }}
            {{ item.contentObject.last_name }}
          </p>
        </div>
      </template>
      <template v-slot:[`annotation`]="{ item }">
        <div>
          <p v-text="item.annotation"></p>
        </div>
      </template>
    </data-table>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DataTable from "../components/DataTable.vue";
import { ACTIVITIES } from "../queries/auth";
import { parseDate, updateQparams } from "../utils/helpers";

export default defineComponent({
  components: { DataTable },
  async created() {
    this.page = this.$route.query.page ?? this.page;
    await this.fetchActivities();
    this.$store.commit("setActivities", this.activities);
    // console.log(this.$store.state.core.activities[0].activityId);
  },
  methods: {
    parseDate,
    updateQparams,
    singleSelected(e: any) {
      console.log(e);
    },
    allChecked(e: any) {
      console.log(`All Checked, ${e}`);
    },
    async fetchActivities() {
      const { data } = await this.$apollo.query({
        query: ACTIVITIES,
        fetchPolicy: "network-only",
        variables: {
          page: this.page,
          pageSize: this.pageSize,
        },
      });
      if (data) {
        const objects = data.activities.objects;
        this.activities = JSON.parse(JSON.stringify(objects));
        this.total = data.activities.total;
        this.page = data.activities.page;
        this.pages = data.activities.pages;
        this.hasPrev = data.activities.hasPrev;
        this.hasNext = data.activities.hasNext;
        this.setDropt();
      }
    },
    setDropt() {
      let fin = [] as any;
      for (let i = 0; i < this.total; i++) {
        fin.push(`${i + 1}/${this.total}`);
      }
      this.dropts = fin;
    },
    async prev() {
      this.page--;
      await this.fetchActivities();
      this.updateQparams(this.$route.path, this.page, this.pages);
    },
    async next() {
      this.page++;
      await this.fetchActivities();
      this.updateQparams(this.$route.path, this.page, this.pages);
    },
  },
  data: () => ({
    total: 0,
    pages: 1,
    hasNext: false,
    hasPrev: false,
    page: 1 as any,
    pageSize: 10,
    dropts: [] as any,
    headers: [
      { value: "date", label: "Date" },
      { value: "regarding", label: "Regarding" },
      { value: "annotation", label: "Notes" },
      { value: "name", label: "Entered By" },
    ],
    activities: [] as any,
  }),
});
</script>
