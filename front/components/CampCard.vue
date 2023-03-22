<template>
    <v-card class="d-flex bg-blue-lighten-5 my-2 py-2 align-center justify-start" to="/camp">
        <div class="ml-2">
            <v-img src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg" width="150"></v-img>
        </div>
        <v-card-title>Хибины</v-card-title>
        <v-card-subtitle>Апрель'80</v-card-subtitle>
        <p class="text-grey-lighten-1">Это был классный выезд в компании классных людей, где все классно провели
            время</p>
    </v-card>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const show = ref(false)



</script>

<style scoped></style>

