<template>
    <v-container class="pa-0">
        <v-toolbar color="white" density="compact">
            <v-btn icon>
                <v-icon>mdi-menu</v-icon>
                <AppBarMenu />
            </v-btn>
            <v-app-bar-title>
                <NuxtLink to="/" class="text-decoration-none text-black">Speleo </NuxtLink>
            </v-app-bar-title>
            <v-spacer></v-spacer>
            <RegistrationFormsRegAuthModal />

            <!-- <v-btn icon>
                <v-icon>mdi-account-outline</v-icon>
            </v-btn> -->

        </v-toolbar>
    </v-container>
</template>

<script setup lang="ts">

import { useDrawerStore } from '~~/stores/drawer';

const drawer = useDrawerStore()

// drawer.changeDrawer()

</script>

<style scoped></style>