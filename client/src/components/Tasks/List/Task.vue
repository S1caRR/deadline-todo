<template>
  <div class="task-item">
    <input type="checkbox"> <span @click="toggleDialog" class="task-item-text">{{task.task_name}}</span>
    <div class="delete-button">
      <a href="#" @click="deleteTask(task.id)"><i class="far fa-times-circle"></i></a>
    </div>
  </div>

  <dialog-window class="dialog-window"
                 :isShow="dialogVisible"
                 @hideDialog="toggleDialog">
    <div class="content-input-tasks" >

      <input v-model="taskObj.task_name" type="text" size="40" placeholder="Название таска">
      <br>
      <input v-model="taskObj.task_description" type="text" size="40" placeholder="Описание">
      <br>
      <div class="dialog-window-button">
        <a href="#" @click.prevent="toggleDialog(), updateTask(task.id)">Сохранить</a>
      </div>

    </div>
  </dialog-window>
</template>

<script>
import axios from "axios";
import DialogWindow from "../../UI/DialogWindow";

export default {
  name: "TaskItem",
  components: {DialogWindow},
  data(){
    return{
      currentTask: {},
      dialogVisible: false,
      token: "",
      taskObj: this.task
      //     {
      //   task_name: this.task.task_name,
      //   task_description: this.task.task_description,
      //   deadline: this.task.deadline,
      //   is_finished: this.task.is_finished
      // }
    }
  },
  props: {
    task: { },
  },

  methods:{
    toggleDialog(){
      this.dialogVisible = !this.dialogVisible
    },
    async deleteTask(taskId){

      try {
        this.token = localStorage.getItem("token").toString()

        let config = {
          headers: {
            Authorization: this.token
          },
        }


        const response = await axios.delete(`http://localhost:8081/api/tasks/${taskId}`, config)

        if (response.data.id){
          alert("Таск успешно удалён")
          this.$emit('removeTask', this.task)
        }


      } catch (e) {
        alert('net id')
      }
    },
    async updateTask(taskId){

      try {
        this.token = localStorage.getItem("token").toString()
        let config = {
          headers: {
            Authorization: this.token
          },
          data: this.taskObj
        }

        const response = await axios.patch(`http://localhost:8081/api/tasks/${taskId}`, config.data, config)
        if (response.data.id){
          alert("Таск успешно обновлён")
        }


      } catch (e) {
        alert('ошибочка')
      }
    },
  }

}
</script>

<style scoped lang="scss">
.task-item{
  margin-bottom: 5px;
  margin-left: 10px;
  //display: grid;
  //grid-template-columns:0.1fr 6fr 1fr;
  .task-item-text{
    font-size: 25px;
    margin: 3px;
    font-family: 'Karla', sans-serif;
  }
  .task-item-text:hover{
    cursor: pointer;
  }
  input{
    margin: 3px 2px;
  }

  .delete-button{
    display: inline-block;
    float: right;
    margin: .3em;
    a{
      float: inside;
      font-size: 1em;
      width: 40px;
      padding: .1em .3em;
      //background-color: transparent;
      //border: 1px solid red;
      border-radius: .4em;
      /*margin-right: .5em;*/
      text-decoration: none;
      color: darkred;
      margin-right: 5px;

    }
    a:hover{
      background: rgba(255, 0, 0, 0.3);
    }
  }

}

.task-item:hover{
  background: rgba(121, 118, 253, 0.15);
  border-radius: 5px;
}


</style>