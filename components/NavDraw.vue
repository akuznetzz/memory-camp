<template>
    <v-navigation-drawer v-model="drawer">
        <v-list nav>
            <v-list-item to="/about"> О портале</v-list-item>
            <v-list-item to="/people">Люди</v-list-item>
            <v-list-item to="/camps">Выезды</v-list-item>
        </v-list>
    </v-navigation-drawer>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import { useDrawerStore } from '~~/stores/drawer';

const drawerStore = useDrawerStore()

const { drawer } = storeToRefs(drawerStore)

</script>

<style scoped></style>