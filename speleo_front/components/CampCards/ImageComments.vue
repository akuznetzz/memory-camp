<template>
    <v-card flat>
        <v-card flat height="200">
            <v-card-text v-if="items.length == 0" class="text-center text-medium-emphasis">Оставьте первый
                комметарий...</v-card-text>
            <v-list v-else lines="two" class="d-flex flex-column-reverse overflow-auto">

                <v-list-item v-for="item, index in items" :key="index" :prepend-avatar="item.avatar">
                    <v-list-item-subtitle>
                        {{ item.title }}
                    </v-list-item-subtitle>
                    <v-card-text class="pa-0">
                        {{ item.message }}
                    </v-card-text>
                </v-list-item>

            </v-list>
        </v-card>
        <v-textarea rows="1" class="mx-4" density="compact" variant="outlined" append-icon="mdi-send" v-model="textcontent"
            @click:append="test()"></v-textarea>
    </v-card>
</template>

<script setup>
import { ref } from 'vue'


const items = ref([])

const textcontent = ref('')
const title = 'John, 11:50'
const avatar = 'https://cdn.vuetifyjs.com/images/john.jpg'

const test = () => {
    items.value.unshift({
        title,
        avatar,
        message: textcontent.value
    })

}

</script>

<style scoped></style>