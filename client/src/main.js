import { createApp } from 'vue'
import App from './App.vue'
import store from './store'
import router from "./router/router";
import axios from "axios";

axios.defaults.headers.common['Authorization'] = store.getters.getToken
createApp(App)
    .use(store).use(router)
    .mount('#app')

