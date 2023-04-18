<template>
    <LayoutsPageWrapper>
        <LayoutsCardWrapper>
            <v-card>
                <v-card-title primary-title>Профиль</v-card-title>
                <v-card-text>
                    <v-row>
                        <v-col cols="12" sm="6" order="2" order-sm="1">
                            <v-text-field label="Фамилия" variant="outlined" density="compact"></v-text-field>
                            <v-text-field label="Имя" variant="outlined" density="compact"></v-text-field>
                            <v-text-field label="Отчество" variant="outlined" density="compact"></v-text-field>
                            <v-text-field label="Прозвище" variant="outlined" density="compact"></v-text-field>
                            <v-text-field type="date" label="День рождения" variant="outlined"
                                density="compact"></v-text-field>
                            <v-text-field label="Телефон" variant="outlined" density="compact"></v-text-field>
                            <v-text-field label="Год начала обучения" variant="outlined" density="compact"></v-text-field>
                            <v-text-field label="Год окончания обучения" variant="outlined"
                                density="compact"></v-text-field>
                            <v-text-field label="Группа МГРИ" variant="outlined" density="compact"></v-text-field>
                            <v-checkbox label="Посещал ли спелеошколу"></v-checkbox>
                            <v-checkbox label="Посещал ли спелесекцию"></v-checkbox>
                            <v-text-field label="Роль в группе" variant="outlined" density="compact"></v-text-field>
                            <v-textarea rows="2" label="О себе" variant="outlined" density="compact"></v-textarea>

                        </v-col>
                        <v-col cols="12" sm="6" order="1" order-sm="2">
                            <v-sheet>
                                <v-img src="/570238.png" @click="avatarUpload">

                                </v-img>
                            </v-sheet>
                        </v-col>
                    </v-row>
                </v-card-text>
            </v-card>
        </LayoutsCardWrapper>
    </LayoutsPageWrapper>
</template>

<script setup>

const avatarUpload = () => {
    const el = document.createElement('input')
    el.type = 'file'
    el.click()
}

</script>

<style lang="scss" scoped></style>