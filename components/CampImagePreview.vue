<template>
    <v-col cols="12" sm="6">
        <v-card class="mx-auto">
            <v-img
                src="https://oir.mobi/uploads/posts/2021-05/1622262892_61-oir_mobi-p-krasivie-vidi-prirodi-priroda-krasivo-foto-65.jpg"
                height="200px" cover></v-img>

            <v-card-subtitle>
                Замечательная фотография замечательного выезда
            </v-card-subtitle>

            <v-card-text>
                <v-textarea outlined placeholder="Комментарий"></v-textarea>
            </v-card-text>

        </v-card>
    </v-col>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const show = ref(false)

</script>

<style scoped></style>