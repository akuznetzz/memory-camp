<template>
    <v-card class="ma-2">
        <v-row no-gutters>
            <v-col cols="9">
                <v-row class="pa-4">
                    <CampImagePreview />
                    <CampImagePreview />
                    <CampImagePreview />
                    <CampImagePreview />
                    <CampImagePreview />
                    <CampImagePreview />
                </v-row>
            </v-col>
            <v-col cols="3" class="mt-4">
                <v-card>
                    <v-card-title>
                        Список участников
                    </v-card-title>

                    <v-card-text>
                        <v-list>
                            <v-list-item>
                                <v-list-item>Александр Пушкин</v-list-item>
                                <v-list-item>Виктор Васнецов</v-list-item>
                                <v-list-item>Лев Толстой</v-list-item>
                                <v-list-item>Юрий Гагарин</v-list-item>
                            </v-list-item>
                        </v-list>
                    </v-card-text>
                </v-card>
            </v-col>

        </v-row>
    </v-card>
</template>

<script setup lang="ts">

</script>

<style scoped></style>