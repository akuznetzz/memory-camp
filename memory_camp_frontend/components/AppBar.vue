<template>
    <v-app-bar color="" dense dark>
        <v-app-bar-nav-icon @click="drawer.changeDrawer()"></v-app-bar-nav-icon>
        <v-app-bar-title>
            <NuxtLink to="/" class="text-decoration-none text-black">Memory.Camp </NuxtLink>
        </v-app-bar-title>
        <v-spacer></v-spacer>
        <v-btn>
            Вход
        </v-btn>
        <v-btn>
            Регистрация
        </v-btn>
    </v-app-bar>
</template>

<script setup lang="ts">

import { useDrawerStore } from '~~/stores/drawer';

const drawer = useDrawerStore()

</script>

<style scoped></style>