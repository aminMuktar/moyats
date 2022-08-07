<template>
    <div class="w-full flex justify-center">
        <div class="w-1/2 flex justify-center m-5 bg-white">
            <div class="grid grid-cols-1 w-full relative">
                <div
                  v-if="loadingState"
                  class="
                    absolute
                    bg-white bg-opacity-60
                    z-10
                    h-full
                    w-full
                    flex
                    items-start
                    justify-center
                  "
                >
                  <spinner style="margin-top: 40%"></spinner>
                </div>
                <div class="flex col-span-2 w-full p-4 mt-16 ">
                    <div class="w-56">
                        <span class="m-1">Name </span>
                    </div>

                    <div class="relative w-full">
                        <div v-if="!nEditMode" class="w-full grid lg:grid-cols-3 xl:grid-cols-3 gap-2 pl-8">
                            <div class="w-full">
                                {{ firstName }}
                            </div>
                            <div class="w-full">
                                {{ lastName }}
                            </div>
                            <button @click="nEditMode = true" class="w-5 text-blue-500">
                                Edit
                            </button>
                        </div>
                        <div v-if="nEditMode"
                            class="w-full absolute justify-start grid lg:grid-cols-4 xl:grid-cols-4 gap-2 pl-7">
                            <input required class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                                placeholder="First Name" type="text" id="name" v-model="firstName" />
                            <input required class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                                placeholder="Last Name" type="text" id="name" v-model="lastName" />

                            <button @click="setData(() => nEditMode = false)" class="w-5 text-blue-500">
                                Finish
                            </button>
                        </div>
                    </div>
                </div>

                <div class="flex col-span-2 p-2">
                    <div class="w-56">
                        <label class="sr-only" for="name">Username</label>
                        <span class="m-3 w-full">Username </span>
                    </div>
                    <div v-if="!uEditMode" class="w-full inline-flex gap-4 pl-10">
                        <div>
                            {{ username }}
                        </div>
                        <button @click="uEditMode = true" class="w-5 text-blue-500">
                            Edit
                        </button>
                    </div>
                    <div v-if="uEditMode" class="w-full inline-flex gap-4 pl-9">
                        <input required class="w-2/3 p-2 text-sm border-gray-200 border-2 rounded-md"
                            placeholder="Email" type="email" id="email" v-model="username" />
                        <button @click="setData(() => uEditMode = false)" class="w-5 text-blue-500">
                            Finish
                        </button>
                    </div>

                </div>

                <div class="flex col-span-2 p-2">
                    <div class="w-56">
                        <label class="sr-only" for="name">Email</label>
                        <span class="m-3 w-full">Email</span>
                    </div>
                    <div v-if="!eEditMode" class="w-full inline-flex gap-4 pl-10">
                        <div>
                            {{ email }}
                        </div>
                        <button @click="eEditMode = true" class="w-5 text-blue-500">
                            Edit
                        </button>
                    </div>
                    <div v-if="eEditMode" class="w-full inline-flex gap-4 pl-9">
                        <input pattern="^[w-.]+@([w-]+.)+[w-]{2,4}$" required
                            class="w-2/3 p-2 text-sm border-gray-200 border-2 rounded-md" placeholder="Email"
                            type="email" id="email" v-model="email" />
                        <button @click="setData(() => eEditMode = false)" class="w-5 text-blue-500">
                            Finish
                        </button>
                    </div>

                </div>

                <div class="flex col-span-2 w-full p-4">
                    <div class="w-48">
                        <label class="sr-only" for="name">Phones</label>
                        <span class="m-1">Phones* </span>
                    </div>
                    <div v-if="!cEditMode" class="flex gap-4 pl-3">
                        <div class="w-full grid lg:grid-cols-1 xl:grid-cols-1 gap-3">
                            <div class="grid grid-cols-2">
                                <span class="text-gray-400 pr-7">Cell Number:</span>
                                <div class="">{{ cellNumber }}</div>
                            </div>
                            <div class="grid grid-cols-2">
                                <span class="text-gray-400 pr-7">Home Number:</span>
                                <div class="">{{ homeNumber }}</div>
                            </div>
                            <div class="grid grid-cols-2">
                                <span class="text-gray-400 pr-7">Work Number:</span>
                                <div class="">{{ workNumber }}</div>
                            </div>
                        </div>
                        <button @click="cEditMode = true" class="w-5 text-blue-500">
                            Finish
                        </button>
                    </div>
                    <div v-if="cEditMode" class="flex gap-4 pl-3">
                        <div class="w-full grid lg:grid-cols-1 xl:grid-cols-1 gap-3">
                            <div class="grid grid-cols-2">
                                <span class="text-gray-400">Cell Number:</span>
                                <input required class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                                    type="tel"
                                    pattern="(\+\s*2\s*5\s*1\s*9\s*(([0-9]\s*){8}\s*))|(0\s*9\s*(([0-9]\s*){8}))"
                                    placeholder="Cell Number" id="name" v-model="cellNumber" />
                            </div>

                            <div class="grid grid-cols-2">
                                <span class="text-gray-400">Home Number:</span>
                                <input class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                                    placeholder="Home Number" type="tel"
                                    pattern="(\+\s*2\s*5\s*1\s*9\s*(([0-9]\s*){8}\s*))|(0\s*9\s*(([0-9]\s*){8}))"
                                    id="name" v-model="homeNumber" />
                            </div>

                            <div class="grid grid-cols-2">
                                <span class="text-gray-400">Work Number:</span>
                                <input class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                                    placeholder="Work Number" type="tel"
                                    pattern="(\+\s*2\s*5\s*1\s*9\s*(([0-9]\s*){8}\s*))|(0\s*9\s*(([0-9]\s*){8}))"
                                    id="name" v-model="workNumber" />
                            </div>
                        </div>
                        <button @click="setData(() => cEditMode = false)" class="w-5 text-blue-500">
                            Finish
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">

import { defineComponent } from "vue"
import { ACCOUNT_DATA, UPDATE_USER } from "../../../queries/auth"

export default defineComponent({
    data() {
        return {
            firstName: String,
            lastName: String,
            username: String,
            email: String,
            cellNumber: String,
            homeNumber: String,
            workNumber: String,
            nEditMode: false,
            uEditMode: false,
            eEditMode: false,
            cEditMode: false,
            loadingState: false,
        }
    },
    created() {
        this.getUserData()
    },
    methods: {
        async getUserData() {
            this.loadingState = true
            const { data, error } = await this.$apollo.query({
                query: ACCOUNT_DATA,
            })
            if (data) {
                const storedData = data.accountUser
                this.firstName = storedData.firstName
                this.lastName = storedData.lastName
                this.username = storedData.username
                this.email = storedData.email
                this.cellNumber = storedData.baseContact.cellNumber
                this.homeNumber = storedData.baseContact.homeNumber
                this.workNumber = storedData.baseContact.workNumber
                console.log(storedData)
                this.loadingState = false
            }
            if(error){
                this.loadingState = false
            }
        },
        async setUserData() {
            this.loadingState = true
            const { data, errors } = await this.$apollo.mutate({
                mutation: UPDATE_USER,
                variables: {
                    input: {
                        firstName: this.firstName,
                        lastName: this.lastName,
                        username: this.username,
                        email: this.email,
                        cellNumber: this.cellNumber,
                        homeNumber: this.homeNumber,
                        workNumber: this.workNumber,
                    }
                }
            })
            if (data) {
                const storedData = data.updateUser.response[0]
                this.firstName = storedData.firstName
                this.lastName = storedData.lastName
                this.username = storedData.username
                this.email = storedData.email
                this.cellNumber = storedData.baseContact.cellNumber
                this.homeNumber = storedData.baseContact.homeNumber
                this.workNumber = storedData.baseContact.workNumber
                console.log(storedData, 'stored data')
                this.loadingState = false
            }
            if(errors){
                this.loadingState = false
            }
        },
        async setData(close: any) {
            this.setUserData()
            close()
        }
    }
})

</script>