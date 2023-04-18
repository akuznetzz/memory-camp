<template>
    <LayoutsPageWrapper>
        <LayoutsCardWrapper>
            <v-card>
                <v-card-title primary-title>
                    Персоны
                </v-card-title>
                <v-sheet class="d-flex ">
                    <v-chip size="small" class="mx-4">
                        Годы обучения
                    </v-chip>
                    <v-chip size="small">
                        Группа
                    </v-chip>
                    <v-chip size="small" class="mx-4">
                        Выезды
                    </v-chip>
                </v-sheet>
                <v-sheet class="ma-4">

                    <v-table>
                        <thead>
                            <tr>
                                <th></th>
                                <th>Имя</th>
                                <th>Годы обучения</th>
                                <th>Группа</th>
                                <th>Выезды</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="item, index in items" :key="index">
                                <td><v-avatar :image="item.avatar"></v-avatar></td>
                                <td>{{ item.name }}</td>
                                <td>{{ item.years }}</td>
                                <td>{{ item.group }}</td>
                                <td>{{ item.camps }}</td>
                            </tr>
                        </tbody>
                    </v-table>

                </v-sheet>
            </v-card>
        </LayoutsCardWrapper>
    </LayoutsPageWrapper>
</template>

<script setup lang="ts">

const items = [
    {
        avatar: 'https://i.pravatar.cc/150?img=54',
        name: 'Иван Иванов',
        years: '1988-1994',
        group: 'RF22',
        camps: 'Кунгурская, Капова, Воронцовская'
    },
    {
        avatar: 'https://i.pravatar.cc/150?img=54',
        name: 'Иван Иванов',
        years: '1988-1994',
        group: 'RF22',
        camps: 'Кунгурская, Капова, Воронцовская'
    },
    {
        avatar: 'https://i.pravatar.cc/150?img=54',
        name: 'Иван Иванов',
        years: '1988-1994',
        group: 'RF22',
        camps: 'Кунгурская, Капова, Воронцовская'
    },
]

</script>

<style scoped></style>