<template>
  <div>
    <nav-header class="w-full fixed" />
    <div
      class="w-full bg-gray-200 bottom-0 top-0 absolute flex justify-center overflow-auto"
    >
      <div
        class="w-4/6 lg:w-full lg:p-56 lg:pt-0 xl:w-full xl:p-56 xl:pt-0 items-center"
      >
        <div class="mt-28 text-4xl">Your Companies</div>
        <div
          class="grid 2xl:grid-cols-3 xl:grid-cols-2 sm:grid-cols-1 md:grid-cols-1 items-center gap-8"
          v-if="listOfCompanies"
        >
          <company-management-widget :url="'/dashboard'">
            <template v-slot:body>
              <div
                class="h-full w-full top-0 m-0 flex justify-center items-center text-4xl absolute gap-4 text-blue-500"
              >
                <div class="w-8">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-6 w-6"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    strokeWidth="{2}"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      d="M12 4v16m8-8H4"
                    />
                  </svg>
                </div>
                Add Company
              </div>
            </template>
          </company-management-widget>
          <div v-for="(i, j) in listOfCompanies" :key="j">
            <company-management-widget :url="'/dashboard'">
              <template v-slot:header> {{ i.name }} </template>
              <template v-slot:subHeader>
                {{ i.owner.firstName }}
                {{ i.owner.lastName }}
              </template>
              <template v-slot:body> {{ i.des }} </template>
            </company-management-widget>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import NavHeader from "../../components/NavHeader.vue";
import CompanyManagementWidget from "../../components/widgets/CompanyManagementWidget.vue";
import { COMPANIES } from "../../queries/company";

export default defineComponent({
  components: {
    NavHeader,
    CompanyManagementWidget,
  },
  data() {
    return {
      listOfCompanies: null as any,
    };
  },
  async created() {
    await this.companiesList();
    console.log(this.listOfCompanies);
  },
  methods: {
    async companiesList() {
      const { data, errors } = await this.$apollo.query({
        query: COMPANIES,
        variables: {
          page: 100,
          pageSize: 100,
        },
      });

      if (!errors) {
        this.listOfCompanies = JSON.parse(
          JSON.stringify(data.companies.objects)
        );
      }
    },
  },
});
</script>
