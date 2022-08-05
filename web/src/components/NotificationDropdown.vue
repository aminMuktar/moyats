<template>
  <menu-drop-down :active="active" width="w-96">
    <template v-slot:button>
      <button
        @click="active = !active"
        class="mx-2 bg-black text-white border-2 border-gray-500 rounded-full"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-7 w-7 p-1"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path
            d="M10 2a6 6 0 00-6 6v3.586l-.707.707A1 1 0 004 14h12a1 1 0 00.707-1.707L16 11.586V8a6 6 0 00-6-6zM10 18a3 3 0 01-3-3h6a3 3 0 01-3 3z"
          />
        </svg>
      </button>
    </template>
    <template v-slot:list>
      <div class="float-right p-3">
        <button @click="clearNotification">Clear</button>
      </div>
      <div class="py-9">
        <div class="py-1" v-for="i, j in showNotifications" :key="j">
          <ul>
            <li class="p-5 hover:bg-gray-100 cursor-pointer">
              <div>
                <p class="text-md font-bold">
                  {{ i.action }}
                </p>
                <p>{{ i.aFrom.email }}</p>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </template>
  </menu-drop-down>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import MenuDropDown from "./MenuDropDown.vue";
import {NOTIFICATION, UPDATENOTIFICATION, UPDATENOTIFICATIONS} from "./../queries/Notifications"

export default defineComponent({
  components: { MenuDropDown },
  setup() {},
  data: () => ({
    active: false,
    selected: false,
    notifications: [] as any,
    showNotifications: [] as any
  }),
  created(){
    this.getNotifications()
    this.checkNotifications()
    // setTimeout(a=>{
    //   this.checkNotifications()
    //   console.log(this.showNotifications)
    //   }, 1000)
  },
  methods: {
    async getNotifications(){
      const {data, error} = await this.$apollo.query({
        query: NOTIFICATION
      })
      if(data){
        this.notifications = JSON.parse(JSON.stringify(data.notification))
      }
    },

    async clearNotification(){
      await this.$apollo.mutate({
        mutation: UPDATENOTIFICATIONS,
        variables: {
          cleared: true
        }
      })
      this.showNotifications = []
    },

    checkNotifications(){
      this.notifications.forEach( e => {
        if(!e.cleared && !e.seen){
          this.showNotifications.push(e)
        }
      });
    }

  },
});
</script>

