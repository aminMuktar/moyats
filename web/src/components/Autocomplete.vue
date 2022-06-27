<template>
  <div>
    <div class="relative overflow-hidden">
      <input
        id="email"
        @keyup="showOptions = true"
        v-model="value"
        class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
        autocomplete="off"
        :placeholder="placeholder"
      />
    </div>
    <div
      v-show="resultQuery().length && showOptions"
      class="
        relative
        w-full
        max-h-52
        overflow-y-scroll
        z-50
        bg-white
        border border-gray-300
        mt-1
        max-height-48
        overflow-hidden
        rounded-md
        shadow-md
      "
    >
      <ul class="py-1">
        <li
          :key="index"
          v-for="(value, index) in resultQuery()"
          @click="setInput(value)"
          class="px-3 py-2 cursor-pointer hover:bg-gray-200"
        >
          <!-- {{ index }}{{ value }} -->
          <slot name="list" v-bind="value"></slot>
        </li>
      </ul>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  props: ["data", "setkey", "setname", "placeholder"],
  data() {
    return {
      show: false,
      value: "",
      showOptions: false,
    };
  },
  created() {
    this.$emit("init");
  },
  methods: {
    setInput(value) {
      console.log(value[this.setname], "asdf");
      this.value = value[this.setname];
      this.showOptions = false;
      this.$emit("itemClicked", value);
    },
    resultQuery() {
      this.$emit("init");
      if (this.value) {
        let data = this.data.filter((item) => {
          return this.value
            .toLowerCase()
            .split(" ")
            .every((v) => item[this.setname].toLowerCase().includes(v));
        });

        return data as any;
      } else {
        return [] as any;
      }
    },
  },
});
</script>
