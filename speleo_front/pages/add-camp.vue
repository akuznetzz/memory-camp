<template>
    <LayoutsPageWrapper>
        <LayoutsCardWrapper>
            <v-card flat>
                <v-card-title primary-title>
                    Добавить выезд
                </v-card-title>
                <v-form class="px-10 pb-10">
                    <v-row>
                        <v-col cols="12" sm="6">
                            <v-card flat class="pt-2">
                                <v-text-field variant="outlined" label="Название выезда"
                                    placeholder="Например, Красная-1989"></v-text-field>
                                <v-text-field variant="outlined" label="Регион" placeholder="Например, Крым"></v-text-field>
                                <div class="d-flex flex-row">
                                    <v-text-field variant="outlined" type="date" label="Дата начала"></v-text-field>
                                    <v-spacer></v-spacer>
                                    <v-text-field variant="outlined" type="date" label="Дата окончания"></v-text-field>
                                </div>

                                <AddCampParticipantCombobox />

                                <v-file-input variant="outlined" multiple clearable chips v-model="files"
                                    label="Фотографии"></v-file-input>

                                <v-textarea rows="2" variant="outlined" label="Описание"></v-textarea>

                            </v-card>
                        </v-col>
                        <v-col cols="12" sm="6">
                            <component v-for="item, index in addCaveComponents" :is="item" :key="index">
                            </component>
                            <!-- <AddCaveForm /> -->
                            <v-btn prepend-icon="mdi-plus" @click.prevent="pushAddCaveForm">Ещё пещера</v-btn>
                        </v-col>
                    </v-row>

                </v-form>
            </v-card>
        </LayoutsCardWrapper>
    </LayoutsPageWrapper>
</template>

<script setup>
import { ref, shallowRef, markRaw } from 'vue'
import addCaveForm from '~~/components/AddCamp/addCaveForm.vue';

const files = ref([])

const acf = markRaw(addCaveForm)
const addCaveComponents = ref([acf])

const pushAddCaveForm = () => {
    addCaveComponents.value.push(acf)
}

// <v-btn @click="test">console</v-btn>
// const test = () => {
//     console.log(files.value)
// }

</script>

<style lang="scss" scoped></style>

