<template>
  <div class="date-now-container">

<!--    DayHeader-->
    <div class="date-now-header" >
      {{ date.day }} - {{ date.month }} - {{ date.year }}
<!--      <button @click="getMyTasks">GetTasksss</button>-->
    </div>

<!--    TaskList-->

    <div class="content-tasks-block" >
      <task-list :taskListProp="taskList"/>
<!--      <div v-else>Loading......</div>-->

      <dialog-window :isShow="dialogVisible" @showDialog="showDialog">
        <div class="content-input-tasks" >

          <input type="text" size="50" placeholder="Название таска"
                 v-model="newTaskTitle">
          <input type="text" size="75" placeholder="Описание таска"
                 v-model="newTaskBody">
          <a href="#" v-on:click="addTask">Добавить</a>

        </div>
      </dialog-window>
      <a href="#" @click="showDialog">Создать</a>

    </div>

  </div>
</template>

<script>
import TaskList from "./TaskList";
import DialogWindow from "../UI/DialogWindow";
import axios from "axios";


export default {

  name: "TasksDay",
  components:{TaskList, DialogWindow},

  data() {
    return{
      taskList: [],
      newTaskTitle: "",
      newTaskBody: "",
      dialogVisible: false,
      response: {
        message: ""
      }
    }
  },

  methods: {
    async addTask() {
      if (this.newTaskTitle) {

        let isoDate = new Date()

        isoDate.setFullYear(this.date.year)
        isoDate.setMonth(this.date.month-1)
        isoDate.setDate(this.date.day)

        isoDate = isoDate.toISOString().split('.')[0]

        const newTask = {
          task_name: this.newTaskTitle,
          task_description: this.newTaskBody,
          deadline: isoDate
        }

        const article = {
          task_name: this.newTaskTitle,
          task_description: this.newTaskBody,
          deadline: isoDate
        };


        this.token = localStorage.getItem('token').toString()
        const headers = {
          Authorization: this.token
        }

        try {
          // eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2NDA3MTEyNjF9.YQiVoz3GBnTw7ZT_bNK8api3_sIwHghLWZT__9ob8qM
          const response = await axios.post('http://localhost:8081/api/tasks', article, {headers})
          this.response.message = response.data.message
          alert(this.response.message)
        } catch (e) {
          alert('error')
        }

        this.taskList.push(newTask)
        this.newTaskTitle = ""
        this.newTaskBody = ""
        this.dialogVisible = false

      }
    },

    showDialog() {
      this.dialogVisible = !this.dialogVisible
    },

    getMyTasks() {
      this.taskList = this.responseTasklist
      let isoDate = new Date()

      isoDate.setFullYear(this.date.year)
      isoDate.setMonth(this.date.month-1)
      isoDate.setDate(this.date.day)

      isoDate = isoDate.toISOString().split('T')[0]
      this.taskList = this.taskList.filter( (obj) => {
        let isoString = obj.deadline.split('T')[0]

        //`${this.date.year}-${this.date.month}-0${this.date.day}`

        if (isoString === isoDate){
          return obj
        }
      });

    },

    refreshTasklist(){
      this.getMyTasks()
    }

  },

  props: {
    date: { },
    responseTasklist: { }
  },

  created() {
    this.getMyTasks()
  },

  watch:{
    responseTasklist(){
      this.refreshTasklist()
    }
  }

}
</script>

<style scoped>
.date-now-container{
  margin: 20px;
}

.date-now-header{
  border-bottom: 2px solid teal;
  margin-bottom: 10px;
}

</style>