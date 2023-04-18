<template>
    <v-col cols="12" md="12">
        <v-card class="mx-auto" rounded="0">
            <v-img
                src="https://oir.mobi/uploads/posts/2021-05/1622262892_61-oir_mobi-p-krasivie-vidi-prirodi-priroda-krasivo-foto-65.jpg"
                height="250" cover></v-img>

            <v-card-actions>
                <v-btn icon @click="show2 = !show2">
                    <v-icon>mdi-account-group-outline</v-icon>
                </v-btn>

                <v-spacer></v-spacer>

                <v-btn icon="mdi-forum-outline" @click="show = !show"></v-btn>
            </v-card-actions>

            <v-expand-transition>
                <div v-show="show">
                    <v-divider></v-divider>

                    <camp-cards-image-comments />
                </div>
            </v-expand-transition>
            <v-expand-transition>
                <div v-show="show2">
                    <v-divider></v-divider>

                    <v-card-text>
                        <v-list>
                            <v-list-item>Александр Пушкин</v-list-item>
                            <v-list-item>Александр Пушкин</v-list-item>
                            <v-list-item>Александр Пушкин</v-list-item>
                        </v-list>
                    </v-card-text>
                </div>
            </v-expand-transition>
        </v-card>
    </v-col>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const show = ref(false)
const show2 = ref(false)

</script>

<style scoped></style>