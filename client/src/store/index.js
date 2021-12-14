import { createStore } from 'vuex'
import createPersistedState from "vuex-persistedstate";
import axios from "axios";

export default createStore({
    state: {
        isAuthorized: false,
        token: '',
        tasklist: [],
        haveResponse: false,
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
        getUsername: state => {
            return state.username
        },
        getTgID: state => {
            return state.tgID
        }
    },
    actions:{
        refreshTasklist(context){
            axios.defaults.headers.common['Authorization'] = this.state.token
            axios.get('http://localhost:8081/api/tasks', {params:{is_finished: false}})
                .then( response => {
                    context.commit('changeTasklist', Array.from(response.data.tasks));
                });
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
        setUsername: (state, newUsername) =>{
            state.username = newUsername
        },
        setTgID: (state, newTgID) =>{
            state.tgID = newTgID
        },
    },


    plugins: [createPersistedState()]
})
