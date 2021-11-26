<template>
  <div class="date-now-container">

<!--    DayHeader-->
    <div class="date-now-header">
      {{ date.day }} - {{ date.month }} - {{ date.year }}
    </div>

<!--    TaskList-->

    <div class="content-tasks-block">
        <task-list :taskList="taskList"/>

      <div  class="content-input-tasks">
        <input type="text" size="100" placeholder="Название таска"
               v-model="newTaskTitle">
        <a href="#" v-on:click="addTask">Добавить</a>
      </div>

    </div>

  </div>
</template>

<script>
import TaskList from "./TaskList";

export default {
  name: "TasksDay",
  components:{TaskList},
  data() {
    return{
      taskList: [],
      newTaskTitle: "",
    }
  },

  methods: {
    addTask() {
      if (this.newTaskTitle) {
        const newTask = {
          id: Date.now(),
          title: this.newTaskTitle
        }
        this.taskList.push(newTask)
        this.newTaskTitle = ""
      }
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