<template>
    <v-col cols="12" sm="6">
        <v-card rounded="0" class="" to="/human">
            <v-row no-gutters>
                <v-col cols="4" class="pl-6 py-6">
                    <v-avatar color="grey" size="150" rounded="0">
                        <v-img cover src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"></v-img>
                    </v-avatar>
                    <v-list-item title="Marcus Obrien" subtitle="Network Engineer"></v-list-item>
                </v-col>
                <v-col cols="8" class="pt-6">
                    <v-card-subtitle>
                        Краткое описание
                    </v-card-subtitle>
                    <v-card-text>
                        Какой-то дополнительный текст
                    </v-card-text>
                    <v-card-subtitle>
                        Годы участия
                    </v-card-subtitle>
                    <v-card-text>
                        1970-1980
                    </v-card-text>

                </v-col>
            </v-row>
        </v-card>
    </v-col>
</template>

<script setup lang="ts">

</script>

<style scoped></style>