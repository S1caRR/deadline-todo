<template>
  <div class="task-item">
    <input type="checkbox"> <span>{{task.task_name}}</span>
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

<style scoped lang="scss">
.task-item{


  span{
    font-size: 20px;
    margin: 6px;
    font-family: 'Karla', sans-serif;
  }
}
a{
  font-size: 18px;
  width: 50px;
  padding: .2em 1em;
  background-color: transparent;
  border: 1px solid red;
  border-radius: .4em;
  color: Black;
  /*margin-right: .5em;*/
  text-decoration: none;
}
a:hover{
  background: rgba(255, 0, 0, 0.3);
}

input{
  margin: 3px 2px;
}

</style>