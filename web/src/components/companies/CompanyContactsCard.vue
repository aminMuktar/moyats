<template>
  <div>
    <dashboard-card-widget>
      <template v-slot:header>
        <div>
          <div class="flex flex-row justify-between">
            <p class="p-3 font-semibold text-lg">Contacts</p>
            <div class="flex flex-row">
              <button
                class="
                  py-2
                  px-
                  mx-2
                  text-xs
                  my-3
                  font-medium
                  text-center text-white
                  bg-white-700
                  rounded-lg
                  focus:ring-4 focus:outline-none focus:ring-blue-300
                "
                @click="openContactWindow()"
              >
                <span
                  class="
                    relative
                    px-5
                    py-2.5
                    transition-all
                    ease-in
                    duration-75
                    bg-white
                    dark:bg-gray-900
                    rounded-md
                    group-hover:bg-opacity-0
                  "
                >
                  Add Contact
                </span>
              </button>
            </div>
          </div>
        </div>
      </template>
      <template v-slot:body>
        <div>
          <data-table
            @prev="prev"
            @next="next"
            :dropts="dropts"
            :hasNext="hasNext"
            :hasPrev="hasPrev"
            :total="total"
            :page="page"
            :pages="pages"
            :emptyMessage="'No candidates added yet'"
            :items="contacts"
            :headers="headers"
            @checkedAll="allChecked"
            @selected="singleSelected"
          >
            <template v-slot:[`name`]="{ item }">
              <div>
                <router-link
                  :to="`/contacts/${item.companyContactId}`"
                  class="text-sm text-blue-500 font-semibold"
                >
                  {{ item.firstName }} {{ item.lastName }}
                </router-link>
              </div>
            </template>
            <template v-slot:[`department`]="{ item }">
              <div>
                <p>{{ item.department }}</p>
              </div>
            </template>
            <template v-slot:[`status`]="{ item }">
              <div>
                <chip
                  @click="toggleStatusSlider('contact')"
                  :color="item.status.color.hex"
                  :text="item.status.name"
                ></chip>
              </div>
            </template>

            <template v-slot:[`updated`]="{ item }">
              <div>
                <p
                  class="text-sm text-gray-500"
                  v-text="parseDate(item.updatedAt)"
                ></p>
              </div> </template
          ></data-table>
        </div>
      </template>
    </dashboard-card-widget>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { loadCompanyContacts } from "../../services";
import { parseDate, toggleStatusSlider } from "../../utils/helpers";
import DashboardCardWidget from "../DashboardCardWidget.vue";
import DataTable from "../DataTable.vue";
import Chip from "../widgets/Chip.vue";

export default defineComponent({
  components: { DashboardCardWidget, DataTable, Chip },
  setup() {},
  props: ["data"],
  computed: {
    getFormupdateStatus() {
      this.fetchContacts();
      return this.$store.getters.getFormupdateStatus;
    },
  },
  watch: {
    getFormupdateStatus(value) {
      if (value) {
        this.fetchContacts();
      }
    },
  },
  data: () => ({
    total: 0,
    pages: 1,
    hasNext: false,
    hasPrev: false,
    page: 1,
    pageSize: 5,
    dropts: [] as any,
    contacts: [],
    headers: [
      {
        value: "name",
        label: "Name",
      },
      {
        value: "updated",
        label: "Updated",
      },
      {
        value: "department",
        label: "Department",
      },
      {
        value: "status",
        label: "Status",
      },
      {
        value: "action",
        label: "Action",
      },
    ],
  }),
  async created() {
    await this.fetchContacts();
  },
  methods: {
    toggleStatusSlider,
    async fetchContacts() {
      const {
        data: {
          companyContacts: { objects },
        },
      } = await loadCompanyContacts({
        company: this.$route.params.cpid,
        page: this.page,
        size: this.pageSize,
      });
      this.contacts = objects;
    },
    parseDate,
    setDropt() {
      let fin: Array<any> = [];
      for (let i = 0; i < this.total; i++) {
        fin.push(`${i + 1}/${this.total}`);
      }
      console.warn(this.total);
      this.dropts = fin;
    },
    async fetchPipelineCandidates() {},
    singleSelected(e: any) {
      console.log(e);
    },
    allChecked(e: any) {
      console.log(`All Checked, ${e}`);
    },
    openContactWindow() {
      console.log(this.data, "dawg");
      this.$store.commit("setScompany", this.data);
      this.$store.commit("setActiveSlideWindow", "contacts");
      this.$store.commit("setActivateSlider", true);
    },
    async prev() {
      this.page--;
      await this.fetchPipelineCandidates();
    },
    async next() {
      this.page++;
      await this.fetchPipelineCandidates();
    },
  },
});
</script>
