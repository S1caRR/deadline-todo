<template>
  <div class="date-now-container">

<!--    DayHeader-->
    <div class="date-now-header">
<!--      {{ date.day }} - {{ date.month }} - {{ date.year }}-->
      {{dateISO[2]}}.{{dateISO[1]}}.{{dateISO[0]}}
<!--      <button @click="getMyTasks">GetTasksss</button>-->
    </div>

<!--    TaskList-->

    <div class="content-tasks-block" >
      <task-list :taskListProp="taskList"/>
<!--      <div v-else>Loading......</div>-->

      <dialog-window :isShow="dialogVisible" @hideDialog="toggleDialog">
        <div class="content-input-tasks" >

          <input type="text" size="50" placeholder="Название таска"
                 v-model="newTaskTitle">
          <input type="text" size="75" placeholder="Описание таска"
                 v-model="newTaskBody">
          <a href="#" v-on:click.prevent="addTask">Добавить</a>

        </div>
      </dialog-window>

      <a href="#" @click.prevent="toggleDialog">Создать</a>

    </div>

  </div>
</template>

<script>
import TaskList from "./TaskList";
import DialogWindow from "../../UI/DialogWindow";
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
      },
      dateISO: ""
    }
  },

  props: {
    date: { },
    responseTasklist: { }
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

        // this.refreshTasklist()
      }
    },

    toggleDialog() {
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
    dateToISOString(){
      let newDate = new Date()
      newDate.setFullYear(this.date.year)
      newDate.setMonth(this.date.month-1)
      newDate.setDate(this.date.day)
      this.dateISO = newDate.toISOString().split('T')[0].split('-')
    },

    refreshTasklist(){
      this.getMyTasks()
    }

  },



  created() {
    this.getMyTasks()
    this.dateToISOString()
  },

  watch:{
    responseTasklist(){
      this.refreshTasklist()
    },
    date(){
      this.dateToISOString()
    }
  }

}
</script>

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300&family=Karla:wght@300&family=Readex+Pro:wght@300&family=Tinos&display=swap');
.date-now-container{
  //border-bottom: 2px solid teal;
  //border: 1px solid teal;
  //border-top: 0.2px solid teal;
  border-bottom: 0.2px solid teal;
  border-radius: 5px;
  margin-bottom: -1px;
  padding-bottom: 15px;

}
.date-now-header{

  /*font-family: 'Readex Pro', sans-serif;*/
  font-family: 'Karla', sans-serif;
  font-weight: 1000;
  font-size: 19px;
  color: gray;
  margin-left: .4em;
  margin-bottom: .3em;
  margin-top: .3em;
  margin-right: .4em;
  //border-bottom: 1px solid teal;
  text-align: end;
}
a{
  width: 100px;
  padding: .2em 1em;
  background-color: transparent;
  border: 1px solid lightskyblue;
  border-radius: .4em;
  color: Black;
  margin-right: .5em;
  text-decoration: none;
  margin-top: 5px;
  margin-left: 10px;
  font-size: 17px;
  letter-spacing: 1px;
}

a:hover{
  background: rgba(173,216,230,0.3);
}

</style>