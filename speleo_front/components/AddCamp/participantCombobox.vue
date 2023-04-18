<template>
    <v-combobox variant="outlined" v-model="model" v-model:search="search" :hide-no-data="false" :items="items"
        hide-selected label="Выберите участников" multiple closable-chips chips>
        <template v-slot:no-data>
            <v-list-item>
                <v-list-item-title>
                    No results matching "<strong>{{ search }}</strong>". Press
                    <kbd>enter</kbd> to create a new one
                </v-list-item-title>
            </v-list-item>
        </template>
    </v-combobox>
</template>

<script setup>
import { ref } from 'vue'

const items = ref(['Александр Пушкин', 'Лев Толстой', 'Михаил Лермонтов'])
const model = ref([])
const search = ref(null)


</script>

<style lang="scss" scoped></style>