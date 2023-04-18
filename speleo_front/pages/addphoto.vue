<template>
    <v-container class="pa-0">
        <v-sheet class="ma-4 pa-8">

            <v-form>
                <v-file-input accept="image/*" label="" v-model="d.image"></v-file-input>
                <v-text-field type="" error-count="" placeholder="Название" label="" append-icon="" v-model="d.name"
                    outlined></v-text-field>
                <v-text-field type="" error-count="" placeholder="Комментарий" label="" append-icon="" v-model="d.comment"
                    outlined></v-text-field>
                <v-btn type="submit" @click.prevent="submitForm">Отправить</v-btn>
            </v-form>
        </v-sheet>
    </v-container>
</template>

<script setup>
import { ref } from 'vue';


const d = ref({
    name: '',
    comment: '',
    image: null
})

const submitForm = () => {
    // console.log(d.value.image[0])


    let fd = new FormData()
    fd.append('name', d.value.name)
    fd.append('comment', d.value.comment)
    fd.append('file', d.value.image[0])
    // console.log(fd)

    // useFetch('http://127.0.0.1:8000/api/test/').then(r => console.log(r.data.value))

    // let fd = new FormData()

    // console.log(fd)


    useFetch('http://127.0.0.1:8000/api/test/', {
        method: 'POST',
        headers: { 'Content-Type': 'multipart/form-data; boundary=----' },
        body: fd
    }).then(resp => console.log(resp.data.value)).catch(err => console.log(err.data))
}

</script>

<style scoped></style>