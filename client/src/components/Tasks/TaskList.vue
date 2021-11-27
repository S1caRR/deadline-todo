<template>
  <div class="task-list-container">
    <div class="tasks"
         v-for="task in taskList"
         v-bind:key="task.id">
        <task-item :taskTitle="task.title" />

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

    }
  },

  props: {
    taskList:{
      type: Array,
      required: true
    }
  },

  methods: {
    deleteTask(task){
      // const removeIndex = this.taskList.findIndex( item => item.id === 37 );
      this.taskList.slice(this.taskList.findIndex(task))
    }
  }
}
</script>

<style scoped>

</style>