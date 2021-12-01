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
// import axios from 'axios';

export default {

  name: "TasksDay",
  components:{TaskList, DialogWindow},

  data() {
    return{
      taskList: [],
      newTaskTitle: "",
      newTaskBody:"",
      dialogVisible: false
    }
  },

  methods: {

    addTask() {
      if (this.newTaskTitle) {
        const newTask = {
          id: Date.now(),
          title: this.newTaskTitle,
          data: this.newTaskBody
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
      // for (let i = 0; i < this.responseTasklist; i++) {
      //   let splittedISO = this.responseTasklist[i].deadline.split('T')
      //   if ( splittedISO [0] === `${this.date.year}-${this.date.month}-${this.date.day}`) {
      //     this.taskList.push(this.responseTasklist[i])
      //   }
      //   alert(splittedISO)
      // }

      this.taskList = this.responseTasklist

      this.taskList = this.taskList.filter( (obj) => {
        let isoString = obj["deadline"].split('T')

        if (isoString[0] === `${this.date.year}-${this.date.month}-0${this.date.day}`){
          return obj
        }
      });

    },

    refreshTasklist(){
      this.taskList = this.responseTasklist
      this.taskList = this.taskList.filter( (obj) => {
        let isoString = obj["deadline"].split('T')

        if (isoString[0] === `${this.date.year}-${this.date.month}-0${this.date.day}`){
          return obj
        }
      });
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