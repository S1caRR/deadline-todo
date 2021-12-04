<template>
  <div class="task-list-container">
<!--    <button @click="refreshTasklist">GetTasksss22</button>-->
    <div class="tasks"
         v-for="task in taskList"
         :key="task.id">

        <task-item :task="task" @removeTask="removeTask"/>

<!--        <a href="#" @click="deleteTask(task)">Удалить</a>-->
    </div>
  </div>
</template>

<script>
import TaskItem from "./Task"
export default {
  components: { TaskItem },

  data(){
    return{
      taskList: null
    }
  },

  props: {
    taskListProp:{ }
  },

  methods: {
    refreshTasklist(){
      this.taskList = this.taskListProp
    },
    removeTask(task){
      this.taskList.splice(this.taskList.indexOf(task), 1)
      this.refreshTasklist()
    }

  },

  created() {
    this.refreshTasklist()
  },
  watch:{
    taskListProp(){
      this.refreshTasklist()
    },
    taskList(){
      return this.taskList
    }
  }

}
</script>

<style scoped>
.tasks{
  margin-bottom: 10px;
}
</style>