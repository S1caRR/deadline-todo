<template>
  <div class="task-item">
    <input type="checkbox"> {{task.task_name}}
    <a href="#" @click="deleteTask(task.id)">Удалить</a>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "TaskItem",

  props: {
    task: { },

  },

  methods:{
    async deleteTask(taskId){

      try {
        this.token = localStorage.getItem("token").toString()
        const headers = {
          Authorization: this.token
        }

        const response = await axios.delete(`http://localhost:8081/api/tasks/${taskId}`, {headers})

        if (response.data.id){
          alert("Таск успешно удалён")
          this.$emit('removeTask', this.task)
        }


      } catch (e) {
        alert('net id')
      }
    },
  }

}
</script>

<style scoped>

</style>