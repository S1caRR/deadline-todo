<template>
  <div class="date-now-container">

<!--    DayHeader-->
    <div class="date-now-header">
      {{ISODateArray[2]}}.{{ISODateArray[1]}}.{{ISODateArray[0]}}
    </div>

<!--    TaskList-->
    <div class="content-tasks-block" >

      <task-list :tasklist="tasklist" />

      <a v-if=" $route.path!=='/archive'"
          href="#"
         @click.prevent="isCreatingTask=!isCreatingTask">
        <i class="far fa-plus-square"></i>
      </a>
      <div v-if="isCreatingTask"
           style="display:block;
           margin-top: 1em;
           padding-top: 1em;
           border-top: 1px solid gray;
           border-radius: 10px;
           width: auto;
           ">
        <input
            v-model="newTaskTitle"
            type="text"
            placeholder="Название таска"
            style="
              width: 85%;
              margin-left: 1.4em;
              margin-bottom: 0;
              font-size: 20px">
        <textarea
            v-model="newTaskBody"
            placeholder="Описание таска"
            style="resize: none;
              margin-left: 1.4em;
              margin-bottom: 0;
              width: 85%;
              height: 50px;
              font-size: 20px;
              margin-top: 0;">
        </textarea>
        <input
            v-model="newTaskTime"
            type="time"
            placeholder="чч:мм"
            style="
            color: rebeccapurple;
            color-adjust: exact;
              float: right;
              margin-left: 0;
              margin-right: 10%;
              margin-bottom: 0;
              font-size: 20px;
              ">
        <a style="display: block;
                margin-left: 1em;
                margin-bottom: .1em;
                font-size: 25px;
                height: 30px;
                width: 30px;"
                @click="addTask()">
          <i class="far fa-check-square"></i>
        </a>
      </div>

    </div>
  </div>
</template>

<script>
import TaskList from "./TaskList";
import DialogWindow from "../../UI/DialogWindow";
import axios from "axios";

export default {
  name: "TasklistDay",
  components:{TaskList, DialogWindow},
  data() {
    return{
      tasklist: [],
      newTaskTitle: "",
      newTaskBody: "",
      newTaskTime: "",
      isCreatingTask: false,
      ISODateArray: []
    }
  },

  props: {
    date: { },
    responseTasklist: {}
  },

  methods: {
    addTask() {
      if (this.newTaskTitle) {
        const article = {
          task_name: this.newTaskTitle,
          task_description: this.newTaskBody,
          deadline: this.newTaskTime?
              `${this.date}T${this.newTaskTime}:${this.getISOTimeNow(new Date()).split(':')[2]}`
              :`${this.date}T00:00:00`
              // :`${this.date}T${this.getISOTimeNow(new Date())}`
        };
        axios
            .post('http://localhost:8081/api/tasks', article)
            .then(() => {
              this.$store.dispatch('refreshTasklist')
              this.newTaskTitle = ""
              this.newTaskBody = ""
              this.isCreatingTask=!this.isCreatingTask
            });
          // const response = await axios.post('http://localhost:8081/api/tasks', article)


      }
    },
    getMyTasks() {
      this.tasklist = this.responseTasklist

      this.tasklist = this.tasklist.filter( (obj) => {
        let isoString = obj.deadline.split('T')[0]

        if (isoString === this.date){
          return obj
        }
      });

    },
    getISOTimeNow(){
      console.log(new Date().toLocaleTimeString());
      // return new Date().toISOString().split('.')[0].split('T')[1]
      return new Date().toLocaleTimeString()
    },

    dateISOtoArray(){
      this.ISODateArray = this.date.split('-')
    },

    refreshTasklist(){
      this.dateISOtoArray()
      this.getMyTasks()
    }
  },

  computed:{

  },

  created() {
    // this.tasklist = this.responseTasklist
    this.getMyTasks()
    this.dateISOtoArray()
  },

  watch:{
    responseTasklist(){
      this.refreshTasklist()
    },
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
  //font-family: 'Karla', sans-serif;
  font-family: 'Exo 2', sans-serif;
  font-weight: 400;
  font-size: 19px;
  color: gray;
  margin: .3em .7em;
  //border-bottom: 1px solid teal;
  text-align: end;
}
a{
  width: 100px;
  padding: 0em .1em;
  background-color: transparent;
  //border: 1px solid lightskyblue;
  border-radius: .4em;
  color: indianred;
  margin-right: .5em;
  text-decoration: none;
  margin-top: 5px;
  margin-left: .5em;
  font-size: 25px;
  letter-spacing: 1px;

  //margin-right: .5em;
}

a:hover{
  background: rgba(173,216,230,0.6);
}

//input {
//  margin: 5px;
//  height: 40px;
//  padding: 1px 10px;
//  border-radius: 5px;
//  font-family: 'Exo 2', sans-serif;
//  font-weight: 400;
//}
//
//input[type="text"] {
//  font-size: 20px;
//}


</style>