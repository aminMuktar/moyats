<template>
    <div class="w-full flex justify-center">
        <div class="w-1/2 flex justify-center m-5 bg-white">
            <div class="grid grid-cols-1 w-full relative">
                <div v-if="loadingState" class="
                    absolute
                    bg-white bg-opacity-60
                    z-10
                    h-full
                    w-full
                    flex
                    items-start
                    justify-center
                  ">
                    <spinner style="margin-top: 40%"></spinner>
                </div>
                <div class="grid grid-row-2 w-full p-4 justify-center">
                    <div class="flex gap-4 pl-3">
                        <div class="w-full grid lg:grid-cols-1 xl:grid-cols-1 gap-3 ">
                            <div class="grid grid-cols-2">
                                <span class="text-gray-400">Old Password:</span>
                                <input required class="w-full p-2 text-sm border-2 border-gray-200 rounded-md"
                                    :class="correctOldPass ? 'border-green-300' : 'border-red-500'" type="password"
                                    pattern="(\+\s*2\s*5\s*1\s*9\s*(([0-9]\s*){8}\s*))|(0\s*9\s*(([0-9]\s*){8}))"
                                    placeholder="Old Password" v-model="oldPassword" @focusout="checkOldPassword" />
                            </div>

                            <div class="grid grid-cols-2">
                                <span class="text-gray-400">New Password:</span>
                                <input class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                                    placeholder="New Password" type="password"
                                    pattern="(\+\s*2\s*5\s*1\s*9\s*(([0-9]\s*){8}\s*))|(0\s*9\s*(([0-9]\s*){8}))"
                                    id="name" v-model="newPassword" />
                            </div>

                            <div class="grid grid-cols-2">
                                <span class="text-gray-400">Confirm Password:</span>
                                <input class="w-full p-2 text-sm border-gray-200 border-2 rounded-md"
                                    placeholder="Confirm Password" type="password"
                                    pattern="(\+\s*2\s*5\s*1\s*9\s*(([0-9]\s*){8}\s*))|(0\s*9\s*(([0-9]\s*){8}))"
                                    id="name" v-model="confirmPassword" />
                            </div>
                            <div class="ml-56 text-red-500">
                                {{ errorText }}
                            </div>
                        </div>
                    </div>
                    <div class="mt-10 ml-56 pl-3">
                        <button class="w-5 text-blue-500" @click="changePassword">
                            Confirm
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">

import { defineComponent } from "vue"
import { CHECKUSER_PASSWORD, CHANGEUSER_PASSWORD } from "../../../queries/auth"

export default defineComponent({
    data() {
        return {
            loadingState: false,
            correctOldPass: true,
            oldPassword: "",
            newPassword: "",
            confirmPassword: "",
            showOld: false,
            showNew: false,
            showConf: false,
            errorText: "",
        }
    },
    created() {
    },
    methods: {
        async checkOldPassword(e: any) {
            const { data } = await this.$apollo.mutate({
                mutation: CHECKUSER_PASSWORD,
                variables: {
                    password: this.oldPassword
                }
            })
            if (data) {
                this.correctOldPass = data.checkUserPassword.response
            }
        },
        compareNewPasswords() {
            return this.newPassword === this.confirmPassword ? true : false
        },
        async changePassword() {
            if (this.compareNewPasswords()) {
                await this.$apollo.mutate({
                    mutation: CHANGEUSER_PASSWORD,
                    variables: {
                        password: this.newPassword
                    }
                })
                this.loadingState = true
                setTimeout(() => {
                    this.loadingState = false
                    alert("you have successfully changed your password")
                    this.$router.push('/dashboard')
                }, 2000)

            } else if (!this.correctOldPass) {
                this.errorText = "Incorrect old password!"
            } else {
                this.errorText = "Passwords doesn't match!"
            }
        }
    }
})

</script>