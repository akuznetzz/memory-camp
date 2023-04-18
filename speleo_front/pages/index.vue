<template>
    <v-container class="px-6">
        <v-row>
            <v-col cols="12">
                <AboutCard />
            </v-col>
            <v-col cols="12" sm="6">
                <PeopleCard />
            </v-col>
            <v-col cols="12" sm="6">
                <CampsCard />
            </v-col>

        </v-row>
    </v-container>
</template>

<script setup lang="ts">
import AboutCard from '~~/components/MainPage/AboutCard.vue';
import PeopleCard from '~~/components/MainPage/PeopleCard.vue';
import CampsCard from '~~/components/MainPage/CampsCard.vue';



</script>

<style scoped></style>