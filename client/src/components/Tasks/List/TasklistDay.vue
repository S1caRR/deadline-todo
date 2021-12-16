<template>
  <div class="tasklist-day">
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

      <transition name="dropdown">
        <div class="task-input-form" v-if="isCreatingTask">
          <input class="task-name-input"
                 v-model="newTaskTitle"
                 type="text"
                 placeholder="Название таска">
          <textarea class="task-desc-textarea"
                    v-model="newTaskBody"
                    placeholder="Описание таска">
          </textarea>
          <input class="time-input"
                 v-model="newTaskTime"
                 type="time"
                 placeholder="чч:мм">

          <a class="accept-task-changes"
             @click="addTask()">
            <i class="far fa-check-square"></i>
          </a>
        </div>
      </transition>
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
    responseTasklist: { }
  },

  methods: {
    addTask() {
      if (this.newTaskTitle) {

        // Формируем таск для передачи
        const article = {
          task_name: this.newTaskTitle,
          task_description: this.newTaskBody,
          deadline: this.newTaskTime? // Если время указано
              `${this.date}T${this.newTaskTime}:${new Date().toLocaleTimeString().split(':')[2]}` // Отправляем таск с указанным временем
              :`${this.date}T00:00:00` // Иначе во времени указываем 00:00:00,
                                       // чтобы он отображался в начале списка тасков, таски с указанной датой будут отображаться под ними
        };
        axios
            .post('http://localhost:8081/api/tasks', article)
            .then(() => {
              this.$store.dispatch('refreshTasklist')
              this.newTaskTitle = ""
              this.newTaskBody = ""
              this.isCreatingTask=!this.isCreatingTask
            });
      }
    },

    // Забираем из списка всех тасков только таски на текущее число
    getMyTasks() {
      this.tasklist = this.responseTasklist

      this.tasklist = this.tasklist.filter( (obj) => {
        let isoString = obj.deadline.split('T')[0]
        if (isoString === this.date){
          return obj
        }
      });

    },

    // Преобразуем полученную дату формата yyyy-mm-dd в массив для отображения в темплэйте
    // Можно поменять на split('-').join('.')
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

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

.slide-enter, .slide-leave-to{
  transform: scaleY(0);
}

.dropdown-enter-active,
.dropdown-leave-active {
  transition: all 0.5s;
}
.dropdown-enter{
  transform: translateY(30px);
}
.dropdown-leave-to {
  opacity: 0;
  transform: translateY(-30px);
}

.task-input-form{
  display: block;
  //border-top: 1px solid gray;
  //border-bottom: 1px solid gray;
  border-radius: 3px;
  padding: 10px 0 10px 0;
  width: 100%;
  .task-name-input{
    width: 90%;
    padding: 5px;
    margin-left: 1.4em;
    margin-bottom: 0;
    border: 0.5px solid gray;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;

    border-bottom: #6E7091;
    font-size: 18px;
  }
  .task-desc-textarea{
    resize: none;
    padding: 5px;
    margin-left: 1.4em;
    width: 90%;
    font-size: 18px;
    border: 0.5px solid gray;
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
  }
  .time-input{
    float: right;
    color: orangered;
    margin-left: 0;
    margin-right: 3em;
    margin-bottom: 0;
    font-size: 18px;
  }
  .accept-task-changes{
    cursor: pointer;
    display: block;
    margin-left: 1em;
    margin-bottom: .1em;
    font-size: 25px;
    height: 30px;
    width: 30px;
    color: #ABADDD;
  }
  .accept-task-changes:hover{
    border-radius: 5px;
    background: rgba(81, 120, 72, 0.1);
  }
}
</style>