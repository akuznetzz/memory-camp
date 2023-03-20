<template>
    <v-card class="ma-2">
        <v-card-title primary-title>
            Список выездов
        </v-card-title>
        <v-sheet class="d-flex ">
            <v-chip size="small" class="mx-4">
                Даты
            </v-chip>
            <v-chip size="small">
                Место
            </v-chip>
            <v-chip size="small" class="mx-4">
                Участники
            </v-chip>
        </v-sheet>
        <v-sheet class="ma-4">
            <v-card class="d-flex flex-column">
                <CampCard />
                <CampCard />
                <CampCard />
                <CampCard />
                <CampCard />
                <CampCard />
            </v-card>


        </v-sheet>

    </v-card>
</template>

<script setup lang="ts">


</script>

<style scoped></style>