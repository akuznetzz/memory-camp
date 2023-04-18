<template>
    <v-dialog v-model="dialog" width="400">
        <template v-slot:activator="{ props }">
            <v-btn icon color="primary" v-bind="props">
                <v-icon>mdi-account-outline</v-icon>
            </v-btn>
        </template>

        <v-card overflow-auto>
            <v-form ref="form" @submit.prevent v-model="valid">
                <v-window class="overflow-auto">
                    <v-window-item :value="!reg">
                        <v-card-text class="px-6 pt-6">
                            <v-text-field label="Email" variant="outlined" v-model="userData.email"
                                :rules="[rules.required, rules.email]"></v-text-field>
                            <v-text-field label="Password" variant="outlined"
                                :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                                @click:append="showPassword = !showPassword" :type="showPassword ? 'text' : 'password'"
                                :rules="[rules.required]" v-model="userData.password"></v-text-field>
                            <small class="text-center">Забыли пароль?</small>
                        </v-card-text>
                    </v-window-item>
                    <v-window-item :value="registration">
                        <v-card-text class="px-6 pt-6 pb-0">
                            <v-text-field label="First name*" variant="outlined" v-model="userData.first_name"
                                :rules="[rules.required]"></v-text-field>
                            <v-text-field label="Last name*" variant="outlined" v-model="userData.last_name"
                                :rules="[rules.required]"></v-text-field>
                            <v-text-field label="Email" variant="outlined" v-model="userData.email"
                                :rules="[rules.required, rules.email]"></v-text-field>
                            <v-text-field label="Password" variant="outlined"
                                :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                                @click:append="showPassword = !showPassword" :type="showPassword ? 'text' : 'password'"
                                :rules="[rules.required]" v-model="userData.password"></v-text-field>
                        </v-card-text>
                        <div v-if="errors.length" class="px-6 mt-0">
                            <div v-for="e in err"> <small class="text-red">{{ e }}</small> </div>
                        </div>
                    </v-window-item>
                </v-window>


                <v-card-actions class="px-6 pb-6" v-if="!reg">
                    <v-btn color="blue-darken-1" variant="outlined" @click="reg = true">
                        Зарегистрироваться
                    </v-btn>
                    <v-spacer></v-spacer>

                    <v-btn type="submit" color="blue-darken-1" variant="flat" @click="login">
                        Войти
                    </v-btn>
                </v-card-actions>
                <v-card-actions class="px-6 pb-6" v-else>
                    <v-btn color="blue-darken-1" variant="flat" @click="signin">
                        Зарегистрироваться
                    </v-btn>
                </v-card-actions>
            </v-form>
        </v-card>
    </v-dialog>
</template>

<script setup>
import { ref, watchEffect } from 'vue'

const dialog = ref(false)
const registration = ref(false)
const showPassword = ref(false)
const form = ref(null)
const valid = ref(true)
const errors = ref([])


const rules = ref({
    required: value => !!value || "Required",
    email: value => {
        const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        return pattern.test(value) || 'Invalid e-mail.'
    }
})

const userData = ref({
    email: null,
    password: null,
    first_name: null,
    last_name: null

})

const login = async () => {
    await form.value.validate()
    console.log(valid.value)

    // if (form.value.validate()) {
    //     console.log('true')
    // } else {
    //     console.log('false')

    // }
    // dialog.value = false

}

const signin = async () => {
    await form.value.validate()

    if (valid.value) {
        // dialog.value = false
        useFetch('http://127.0.0.1:8000/api/users/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: userData.value
        }).then(resp => {
            if (!resp.error.value) {
                console.log('success')
            } else {
                const e = resp.error.value.data
                for (let key in e) {
                    e[key].forEach(item => errors.value.push(item))
                }

            }

        }).catch(() => errors.value.push('Что-то пошло не так, попробуйте ещё раз'))

    }

}

watchEffect(() => {
    if (!dialog.value) { setTimeout(() => reg.value = false, 200) }
})

</script>

<style lang="scss" scoped></style>