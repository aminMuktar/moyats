<template>
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
      empty-message="you don't have any contacts yet"
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
      <template v-slot:[`company`]="{ item }">
        <div v-if="item.company">
          <router-link
            :to="`/companies/${item.company.companyId}`"
            class="text-sm text-blue-500 font-semibold"
          >
            {{ item.company.name }}
          </router-link>
        </div>
      </template>
      <template v-slot:[`status`]="{ item }">
        <div>
          <chip
            @click="toggleStatusSlider('contact', item.companyContactId)"
            :color="item.status.color.hex"
            :text="item.status.name"
          ></chip>
        </div>
      </template>
      <template v-slot:[`companyStatus`]="{ item }">
        <div>
          <chip
            @click="toggleStatusSlider('company', item.company.companyId)"
            v-if="item.company"
            :color="item.company.companyStatus.color.hex"
            :text="item.company.companyStatus.name"
          ></chip>
          <p v-else>-</p>
        </div>
      </template>

      <template v-slot:[`updated`]="{ item }">
        <div>
          <p
            class="text-sm text-gray-500"
            v-text="parseDate(item.updatedAt)"
          ></p>
        </div>
      </template>
    </data-table>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import DataTable from "../components/DataTable.vue";
import { CONTACTS } from "../queries/contact";
import { parseDate, toggleStatusSlider, updateQparams } from "../utils/helpers";
import Chip from "../components/widgets/Chip.vue";

export default defineComponent({
  components: { DataTable, Chip },
  async created() {
    this.page = this.$route.query.page ?? this.page;
    await this.fetchContacts();
  },
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

  methods: {
    parseDate,
    updateQparams,
    toggleStatusSlider,
    async fetchContacts() {
      const { data } = await this.$apollo.query({
        query: CONTACTS,
        fetchPolicy: "network-only",
        variables: {
          page: this.page,
          pageSize: this.pageSize,
        },
      });
      if (data) {
        this.contacts = JSON.parse(JSON.stringify(data.contacts.objects));
        this.total = data.contacts.total;
        this.page = data.contacts.page;
        this.pages = data.contacts.pages;
        this.hasPrev = data.contacts.hasPrev;
        this.hasNext = data.contacts.hasNext;
      }
    },
    setDropt() {
      let fin: Array<any> = [];
      for (let i = 0; i < this.total; i++) {
        fin.push(`${i + 1}/${this.total}`);
      }
      this.dropts = fin;
    },
    async prev() {
      this.page--;
      await this.fetchContacts();
      this.updateQparams(this.$route.path, this.page, this.pages);
    },
    async next() {
      this.page++;
      await this.fetchContacts();
      this.updateQparams(this.$route.path, this.page, this.pages);
    },
    singleSelected(e: any) {
      console.log(e);
    },
    allChecked(e: any) {
      console.log(`All Checked, ${e}`);
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
      { value: "name", label: "Name" },
      { value: "company", label: "Company" },
      { value: "updated", label: "Updated" },
      { value: "status", label: "Status" },
      { value: "companyStatus", label: "Company Status" },
    ],
    contacts: [],
  }),
});
</script>
