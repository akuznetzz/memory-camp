<template>
    <LayoutsPageWrapper>
        <v-row>
            <v-col cols="12" sm="8" md="9" order="1" order-sm="0">
                <LayoutsCardWrapper>
                    <!-- <v-card>
                        <v-card-title>
                            О выезде
                        </v-card-title>
                        <v-card-text>
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis molestiae, eos mollitia, totam
                            tenetur quis dolores dignissimos aperiam officiis eligendi quidem dolorum excepturi. Repudiandae
                            ut,
                            omnis quas officiis enim ullam!
                        </v-card-text>
                    </v-card> -->
                    <v-card>
                        <v-expansion-panels>
                            <v-expansion-panel>
                                <v-expansion-panel-title class="d-flex flex-row justify-start">
                                    <span class="text-h6">Красная 1989-1</span>
                                    <v-divider vertical class="mx-6"></v-divider>
                                    <span>Крым</span>
                                    <v-divider vertical class="mx-6"></v-divider>
                                    <span>Май'89</span>
                                </v-expansion-panel-title>

                                <v-expansion-panel-text>
                                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quam illo similique,
                                    architecto non libero cum perspiciatis temporibus recusandae vel a voluptate quos
                                    maiores consequuntur. Dolor molestias quos consectetur adipisci consequuntur!
                                </v-expansion-panel-text>
                            </v-expansion-panel>
                        </v-expansion-panels>
                    </v-card>

                </LayoutsCardWrapper>
            </v-col>
            <v-col cols="12" sm="4" md="3" order="2" order-sm="0">
                <LayoutsCardWrapper>
                    <v-card>
                        <v-expansion-panels>
                            <v-expansion-panel title="Участники выезда">
                                <v-expansion-panel-text>
                                    <v-list>
                                        <v-list-item>Александр Пушкин</v-list-item>
                                        <v-list-item>Александр Пушкин</v-list-item>
                                        <v-list-item>Александр Пушкин</v-list-item>
                                    </v-list>
                                </v-expansion-panel-text>
                            </v-expansion-panel>
                        </v-expansion-panels>
                    </v-card>
                </LayoutsCardWrapper>
            </v-col>

            <v-col cols="12" sm="6" :md=photoMdSize order="4" order-sm="0">
                <v-card variant="text" class="pb-2">
                    <v-row>
                        <CampImagePreview />

                        <v-textarea variant="outlined" rows="2" label="Описание"></v-textarea>


                        <CampImagePreview />
                        <CampImagePreview />
                        <CampImagePreview />
                        <CampImagePreview />
                        <CampImagePreview />
                        <CampImagePreview />
                        <CampImagePreview />
                    </v-row>
                </v-card>

            </v-col>
            <v-col cols="12" sm="6" :md=chatMdSize order="3" order-sm="0" height="600">
                <CampCardsChatCard />
            </v-col>

        </v-row>

    </LayoutsPageWrapper>
</template>

<script setup lang="ts">

const chatMdSize = 6
const photoMdSize = 6

</script>

<style scoped></style>