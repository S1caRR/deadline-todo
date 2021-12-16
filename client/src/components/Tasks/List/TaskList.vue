<template>
    <div class="tasklist"
         v-for="task in tasklist"
         :key="task.id">
          <task :task="task"/>
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
.tasklist{
  margin-bottom: 10px;
}
</style>