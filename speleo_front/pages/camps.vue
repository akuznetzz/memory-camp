<template>
    <LayoutsPageWrapper>
        <LayoutsCardWrapper>
            <v-card flat>
                <v-card-title primary-title>
                    Список выездов
                </v-card-title>
                <v-sheet class="d-flex align-center">
                    <v-chip size="small" class="ml-6 mr-4">
                        Даты
                    </v-chip>
                    <v-chip size="small">
                        Место
                    </v-chip>
                    <v-chip size="small" class="mx-4">
                        Участники
                    </v-chip>
                    <v-spacer></v-spacer>
                    <v-btn prepend-icon="mdi-plus" class="mr-6" to="/add-camp">Добавить выезд</v-btn>
                </v-sheet>
                <v-sheet class="ma-4">

                    <v-table>
                        <thead>
                            <tr>
                                <th>Camp name</th>
                                <th>Image</th>
                                <th>Region</th>
                                <th>Date</th>
                                <th>Comment</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="item, index in items" :key="index" class="table-row" @click.prevent="toTheCamp">
                                <td>{{ item.name }}</td>
                                <td><v-img :src=item.image width="150" class="ma-2"></v-img></td>
                                <td>{{ item.region }}</td>
                                <td>{{ item.date }}</td>
                                <td>{{ item.comment }}</td>
                            </tr>
                        </tbody>
                    </v-table>

                </v-sheet>
            </v-card>
        </LayoutsCardWrapper>
    </LayoutsPageWrapper>
</template>

<script setup lang="ts">

const toTheCamp = () => {
    navigateTo('/camp')
}


const items = [
    {
        name: 'Красная 1-1989',
        image: 'https://cdn.vuetifyjs.com/images/cards/sunshine.jpg',
        region: 'Крым',
        date: 'Май',
        comment: 'Отлично провели время!'
    },
    {
        name: 'Красная 1-1989',
        image: 'https://cdn.vuetifyjs.com/images/cards/sunshine.jpg',
        region: 'Крым',
        date: 'Май',
        comment: 'Отлично провели время!'
    },
    {
        name: 'Красная 1-1989',
        image: 'https://cdn.vuetifyjs.com/images/cards/sunshine.jpg',
        region: 'Крым',
        date: 'Май',
        comment: 'Отлично провели время!'
    },
]

</script>

<style scoped>
.table-row:hover {
    background-color: #F5F5F5;
}
</style>