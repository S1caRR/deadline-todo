import Main from "../components/Main/Main";
import App from "../App";
import {createRouter, createWebHistory} from "vue-router";
import MainContent from "../components/Main/MainContent";
import Today from "../components/Tasks/Today/Today";
import TasklistMain from "../components/Tasks/List/TasklistMain";
import Archive from "../components/Tasks/Archive/Archive";
import Profile from "../components/Profile/Profile";

const routes = [
    {
        path: '/',
        replace: '/today',
        component: Today
    },
    {
        path: '/upcoming',
        component: TasklistMain,
    },
    {
        path: '/today',
        component: Today
    },
    {
        path: '/archive',
        component: Archive
    },
    {
        path: '/profile',
        component: Profile
    },
    {
        path: '/expired'
    }
]

const router = createRouter({
    routes,
    history: createWebHistory()
})

export default router;