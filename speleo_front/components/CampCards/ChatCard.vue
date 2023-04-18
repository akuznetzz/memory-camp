<template>
    <LayoutsCardWrapper class="sticky-top">
        <v-card flat>
            <v-toolbar title="Обсуждение"></v-toolbar>
            <v-card flat height="400">
                <v-card-text v-if="items.length == 0" class="text-center text-medium-emphasis">Здесь пока никто ничего не
                    писал...</v-card-text>
                <v-list v-else lines="two" height="400" class="d-flex flex-column-reverse overflow-auto">
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
            <v-textarea rows="2" class="mx-4" density="compact" variant="outlined" append-icon="mdi-send"
                v-model="textcontent" @click:append="test()"></v-textarea>
        </v-card>
    </LayoutsCardWrapper>
</template>

<script setup>
import { ref } from 'vue'


const items = ref([])
// const list = ref(null)



const textcontent = ref('')
const title = 'John, 11:50'
const avatar = 'https://cdn.vuetifyjs.com/images/john.jpg'

const test = () => {
    items.value.unshift({
        title,
        avatar,
        message: textcontent.value
    })



    // console.log(el.scrollTop, el.clientHeight, el.scrollHeight)
    // const el = list.value.$el


    // el.scrollTop = 2000
    // console.log(el.scrollTop, el.clientHeight, el.scrollHeight)
}

</script>

<style scoped>
.sticky-top {
    position: sticky;
    top: 20px;
}
</style>