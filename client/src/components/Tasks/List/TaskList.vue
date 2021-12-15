<template>
  <div class="task-list-container">
    <div class="tasks"
         v-for="task in tasklist"
         :key="task.id">
          <task :task="task"/>
    </div>
  </div>
</template>

<script>
import Task from "./Task"
export default {
  components: { Task },

  props: {
    tasklist:{ }
  },

}
</script>

<style scoped>
.tasks{
  margin-bottom: 10px;
}
</style>