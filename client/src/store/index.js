import { createStore } from 'vuex'
import createPersistedState from "vuex-persistedstate";

export default createStore({
    state: {
        isShowDialogHeader: false,
        isShowDialogCreateTask: false,
        isAuthorized: false,
        token: '',
        tasklist: []
    },
    getters:{
        getIsShowDialogHeader(state){
            return state.isShowDialogHeader
        },
        getIsShowDialogCreateTask(state){
            return state.isShowDialogCreateTask
        },
        getToken(state){
            return state.token
        },
        getAuthStatus(state){
            return state.isAuthorized
        },
        getTasklist(state){
            return state.tasklist
        },
    },
    actions:{
      // toggleDialog(context){
      //     context.commit('toggleIsShow');
      // }
    },
    mutations: {
        toggleIsShowDialogHeader(state){
            state.isShowDialogHeader = !state.isShowDialogHeader
        },
        toggleIsShowDialogCreateTask(state){
            state.isShowDialogCreateTask = !state.isShowDialogCreateTask
        },
        changeToken(state, newToken){
            state.token = newToken
        },
        changeAuthStatus(state){
            state.isAuthorized = !state.isAuthorized
        },
        changeTasklist(state, newTasklist){
            state.tasklist = newTasklist
        },
    },


    plugins: [createPersistedState()]
})
