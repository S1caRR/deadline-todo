<template>
  <div class="task-list-container">
    <button @click="refreshTasklist">GetTasksss22</button>
    <div class="tasks"
         v-for="task in taskList"
         :key="task.id">
        <task-item :taskTitle="task.task_name" />

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
    deleteTask(task){
      // const removeIndex = this.taskList.findIndex( item => item.id === 37 );
      this.taskList.slice(this.taskList.findIndex(task))
    },

    refreshTasklist(){
      this.taskList = this.taskListProp
    }

  },

  created() {
    this.refreshTasklist()
  }

}
</script>

<style scoped>

</style>