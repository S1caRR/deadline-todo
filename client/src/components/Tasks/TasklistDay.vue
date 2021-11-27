<template>
  <div class="date-now-container">

<!--    DayHeader-->
    <div class="date-now-header">
      {{ date.day }} - {{ date.month }} - {{ date.year }}
    </div>

<!--    TaskList-->

    <div class="content-tasks-block">
      <task-list :taskList="taskList"/>

      <dialog-window :isShow="dialogVisible" @showDialog="showDialog">
        <div class="content-input-tasks" >

          <input type="text" size="50" placeholder="Название таска"
                 v-model="newTaskTitle">
          <input type="text" size="100" placeholder="Описание таска"
                 v-model="newTaskData">
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

export default {
  name: "TasksDay",
  components:{TaskList, DialogWindow},
  data() {
    return{
      taskList: [],
      newTaskTitle: "",
      newTaskData:"",
      dialogVisible: false
    }
  },

  methods: {
    addTask() {
      if (this.newTaskTitle) {
        const newTask = {
          id: Date.now(),
          title: this.newTaskTitle,
          data: this.newTaskData
        }
        this.taskList.push(newTask)
        this.newTaskTitle = ""
        this.newTaskData = ""
        this.dialogVisible = false
      }
    },

    showDialog(){
      this.dialogVisible = !this.dialogVisible
    }
  },

  props:{
    date: { }
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