<template>
    <v-card flat class="pt-2">
        <v-text-field :density=density variant="outlined" label="Название пещеры"></v-text-field>
        <v-text-field :density=density variant="outlined" label="Координаты"></v-text-field>
        <v-text-field :density=density variant="outlined" label="Адрес"></v-text-field>
        <v-text-field :density=density variant="outlined" label="Сайт"></v-text-field>

    </v-card>
</template>

<script setup>

const density = 'compact'

</script>

<style lang="scss" scoped></style>