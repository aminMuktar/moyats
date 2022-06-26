<template>
  <div class="flex w-full flex-col">
    <div class="flex p-2 border-b-2 flex-row w-full fixed gap-2 bg-white">
      <button
        @click="saveChanges($refs.form)"
        class="
          bg-green-500
          p-2
          text-white
          rounded-md
          tracking-wider
          hover:bg-green-600
        "
      >
        Save Changes
      </button>
      <button
        @click="$emit('close')"
        class="
          border-red-500
          p-2
          border-2
          text-red-700
          rounded-md
          tracking-wider
          hover:bg-red-100
        "
      >
        Cancel
      </button>
    </div>
    <form class="w-full mt-16" ref="form">
      <div class="grid grid-cols-1 w-full">
        <div class="flex col-span-2 w-full p-4">
          <div class="w-52">
            <label class="sr-only" for="name">Title</label>
            <span class="m-1">Title* </span>
          </div>
          <div class="w-full ml-10">
            <input
              required
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="Title"
              type="name"
              id="name"
            />
          </div>
        </div>
        <div class="flex col-span-2 p-2">
          <div class="w-52">
            <label class="sr-only" for="name">Location</label>
            <span class="m-3 w-full">Location*</span>
          </div>
          <div class="flex gap-2">
            <input
              required
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="City"
              type="text"
              id="name"
            />
            <input
              required
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="State"
              type="text"
              id="name"
            />
            <input
              required
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="Zip Code"
              type="text"
              id="name"
            />
          </div>
        </div>
        <div class="flex col-span-2 w-full p-2">
          <label class="sr-only" for="name">Job Type</label>
          <div class="w-52">
            <span class="m-3">Job Type*</span>
          </div>
          <select
            required
            class="
              w-1/3
              p-2
              text-sm
              border-gray-200 border-2
              rounded-md
              text-gray-600
            "
            placeholder="Title"
            type="selector"
            id="name"
          >
            <option value="">Something</option>
            <option value="">Something</option>
            <option value="">Something</option>
            <option value="">Something</option>
            <option value="">Something</option>
          </select>
        </div>
        <div class="flex col-span-2 w-full p-2">
          <div class="w-52">
            <span class="m-3">Recruiter* </span>
          </div>
          <div>
            <div class="bg-blue-300 rounded-md flex left-0">
              <a
                href=""
                class="
                  h-full
                  w-full
                  flex
                  justify-center
                  items-center
                  pl-4
                  pr-4
                  text-gray-600
                "
              >
                Someone</a
              >
            </div>
          </div>
        </div>
        <div class="flex col-span-2 w-full p-2">
          <div class="w-52">
            <label class="sr-only" for="name">Owner</label>
            <span class="m-3">Owner* </span>
          </div>
          <div>
            <div class="bg-blue-300 rounded-md">
              <a
                href=""
                class="
                  h-full
                  w-full
                  flex
                  justify-center
                  items-center
                  pl-4
                  pr-4
                  text-gray-600
                "
              >
                Someone</a
              >
            </div>
          </div>
        </div>
        <div class="col-span-2 flex p-2">
          <div class="w-52">
            <label class="sr-only" for="name"></label>
            <span class="m-3">Source* </span>
          </div>
          <div>
            <input
              required
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="Source"
              type="text"
              id="name"
            />
          </div>
        </div>
        <div class="col-span-2 flex p-2">
          <div class="w-52">
            <label class="sr-only" for="name">Title</label>
            <span class="m-3">Sourcer* </span>
          </div>
          <div>
            <input
              required
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="Sourcer"
              type="text"
              id="name"
            />
          </div>
        </div>
        <div class="col-span-2 flex p-2">
          <div class="w-52">
            <label class="sr-only" for="name">Group</label>
            <span class="m-3">Group* </span>
          </div>
          <div>
            <input
              required
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="Group"
              type="text"
              id="name"
            />
          </div>
        </div>

        <!-- second section start -->
        <div class="w-full border-t-2 my-2"></div>

        <div class="col-span-2 flex p-2">
          <div class="w-52">
            <label class="sr-only" for="name">Hot</label>
            <span class="m-3">Hot* </span>
          </div>
          <div>
            <input
              required
              class="p-1 text-sm border-gray-200 border-2 rounded-md"
              type="checkbox"
            />
          </div>
        </div>
        <div class="col-span-2 flex p-2">
          <div class="w-52">
            <label class="sr-only" for="name">Start Date</label>
            <span class="m-3">Start Date* </span>
          </div>
          <div>
            <input
              required
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="Start date"
              type="text"
              id="name"
            />
          </div>
        </div>
        <div class="col-span-2 flex p-2">
          <div class="w-52">
            <label class="sr-only" for="name">Salery</label>
            <span class="m-3">Salery* </span>
          </div>
          <div>
            <input
              required
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="Salery"
              type="text"
              id="name"
            />
          </div>
        </div>
        <div class="col-span-2 flex p-2">
          <div class="w-52">
            <label class="sr-only" for="name">Duration</label>
            <span class="m-3">Duration* </span>
          </div>
          <div>
            <input
              required
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="Duration"
              type="text"
              id="name"
            />
          </div>
        </div>
        <div class="col-span-2 flex p-2">
          <div class="w-52">
            <label class="sr-only" for="name">Maximum Rate</label>
            <span class="m-3">Maximum Rate* </span>
          </div>
          <div>
            <input
              required
              class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
              placeholder="Maximum Rate"
              type="text"
              id="name"
            />
          </div>
        </div>
        <div class="col-span-2 flex p-2 mb-52"></div>
      </div>
    </form>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  setup() {},
  methods: {
    saveChanges(e) {
      e.preventDefault();
      e.submit();
    },
  },
});
</script>
