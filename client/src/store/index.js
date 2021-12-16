import { createStore } from 'vuex'
import createPersistedState from "vuex-persistedstate";
import axios from "axios";

export default createStore({
    state: {
        isAuthorized: false,
        token: '',
        tasklist: [],
        finishedTasklist: [],
        username: '',
        tgID: ''
    },
    getters:{
        getToken: state => {
            return state.token
        },
        getAuthStatus: state => {
            return state.isAuthorized
        },

        getTasklist: state => {
            return state.tasklist
        },
        getFinishedTasklist: state => {
            return state.finishedTasklist
        },
        getUsername: state => {
            return state.username
        },
        getTgID: state => {
            return state.tgID
        }
    },
    actions:{
        refreshTasklist(context) {
            axios.defaults.headers.common['Authorization'] = this.state.token
            axios.get('http://localhost:8081/api/tasks', {params:{is_finished: false}})
                .then( response => {
                    context.commit('changeTasklist', Array.from(response.data.tasks));
                });
        },
        refreshFinishedTasklist(context) {
            axios.defaults.headers.common['Authorization'] = this.state.token

            axios.get('http://localhost:8081/api/tasks', {params:{is_finished: true}})
                .then( response => {
                    context.commit('changeFinishedTasklist', Array.from(response.data.tasks));
                });
        },
        // На всякий случай
        refreshToken(context) {
            axios.defaults.headers.common['Authorization'] = context.state.token
        }

    },
    mutations: {
        changeToken: (state, newToken) => {
            state.token = newToken
            // axios.defaults.headers.common['Authorization'] = newToken
        },
        changeAuthStatus: state =>{
            state.isAuthorized = !state.isAuthorized
        },
        changeTasklist: (state, newTasklist) =>{
            state.tasklist = newTasklist
        },
        changeFinishedTasklist: (state, newFinishedTasklist) =>{
            state.finishedTasklist = newFinishedTasklist
        },
        setUsername: (state, newUsername) =>{
            state.username = newUsername
        },
        setTgID: (state, newTgID) =>{
            state.tgID = newTgID
        },
    },
    plugins: [createPersistedState()]
})
