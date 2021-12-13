import Main from "../components/Main/Main";
import App from "../App";
import {createRouter, createWebHistory} from "vue-router";
import MainContent from "../components/Main/MainContent";
import Today from "../components/Tasks/Today/Today";
import TasklistDay from "../components/Tasks/List/TasklistDay";
import CalendarMonth from "../components/Tasks/Calendar/CalendarMonth";
import TasklistMain from "../components/Tasks/List/TasklistMain";
import Archive from "../components/Tasks/Archive/Archive";

const routes = [
    {
        path: '/',
        component: MainContent
    },
    {
        path: '/upcoming',
        component: TasklistMain,
        replace: true
    },
    {
        path: '/calendar',
        component: CalendarMonth
    },
    {
        path: '/today',
        component: Today
    },
    {
        path: '/archive',
        component: Archive
    },
]

const router = createRouter({
    routes,
    history: createWebHistory()
})

export default router;