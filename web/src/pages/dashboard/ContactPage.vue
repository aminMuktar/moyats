<template>
  <div class="" v-if="contact">
    <div class="bg-white m-0 w-full h-20 flex flex-row gap-20 px-2">
      <div>
        <p class="pb-2">Company</p>
        <div class="flex flex-row gap-2 mt-2" v-if="contact.company">
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
          <p v-text="contact.company.name"></p>
        </div>
        <p v-else>-</p>
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
          <!-- add other numbers in here in a list widget -->
          <p>{{ contact.phones.cellNumber }}</p>
        </div>
      </div>
      <div>
        <p class="pb-2">Email</p>
        <div class="flex flex-row gap-2 mt-2">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              fill-rule="evenodd"
              d="M14.243 5.757a6 6 0 10-.986 9.284 1 1 0 111.087 1.678A8 8 0 1118 10a3 3 0 01-4.8 2.401A4 4 0 1114 10a1 1 0 102 0c0-1.537-.586-3.07-1.757-4.243zM12 10a2 2 0 10-4 0 2 2 0 004 0z"
              clip-rule="evenodd"
            />
          </svg>
          <p>{{ contact.email }}</p>
        </div>
      </div>
    </div>
    <!-- start of tabs -->
    <div class="grid gap-3 lg:grid-cols-2 xl:grid-cols-2 m-5">
      <div class="flex flex-col">
        <div>
          <contacts-primary-card
            @updated="updatedContacts"
            :data="contact"
          ></contacts-primary-card>
          <contact-detail-card :data="contact"></contact-detail-card>
          <contact-company-card :data="contact"></contact-company-card>
          <contacts-notes-card></contacts-notes-card>
        </div>
      </div>
      <div>
        <contacts-activity-feed-card></contacts-activity-feed-card>
        <contacts-joborder-card></contacts-joborder-card>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import ContactCompanyCard from "../../components/contacts/ContactCompanyCard.vue";
import ContactDetailCard from "../../components/contacts/ContactDetailCard.vue";
import ContactsActivityFeedCard from "../../components/contacts/ContactsActivityFeedCard.vue";
import ContactsJoborderCard from "../../components/contacts/ContactsJoborderCard.vue";
import ContactsNotesCard from "../../components/contacts/ContactsNotesCard.vue";
import ContactsPrimaryCard from "../../components/contacts/ContactsPrimaryCard.vue";
import DashboardCardWidget from "../../components/DashboardCardWidget.vue";
import Chip from "../../components/widgets/Chip.vue";
import { CONTACT } from "../../queries/contact";

export default defineComponent({
  components: {
    Chip,
    DashboardCardWidget,
    ContactsPrimaryCard,
    ContactDetailCard,
    ContactCompanyCard,
    ContactsNotesCard,
    ContactsActivityFeedCard,
    ContactsJoborderCard,
  },
  setup() {},
  data: () => ({
    contact: null as any,
  }),
  async created() {
    await this.fetchContactData();
  },
  methods: {
    async updatedContacts() {
      await this.fetchContactData();
    },
    async fetchContactData() {
      const { data } = await this.$apollo.query({
        query: CONTACT,
        fetchPolicy: "network-only",
        variables: {
          cid: this.$route.params.cid,
        },
      });
      if (data) {
        this.contact = data.contact;
      }
    },
  },
});
</script>
