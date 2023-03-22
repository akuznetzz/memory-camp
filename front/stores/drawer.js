import { defineStore } from 'pinia';

export const useDrawerStore = defineStore('drawer', {
    state: () => ({
        drawer: false
    }),
    actions: {
        changeDrawer() {
            this.drawer = !this.drawer
        }
    }
})