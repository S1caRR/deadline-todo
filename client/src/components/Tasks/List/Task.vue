<template>
  <div class="task-item">
    <div class="checked" v-if="taskObj.is_finished">
      <input type="checkbox" checked @click.prevent="taskObj.is_finished = !taskObj.is_finished, updateTask()">
        <span class="task-item-text">{{taskObj.task_name}}</span>
    </div>

    <div class="unchecked" v-else>
      <div v-if="!isUpdating">
        <input type="checkbox" @click.prevent="taskObj.is_finished = !taskObj.is_finished, updateTask()">
        <span
            @click="toggleIsUpdating"
            class="task-item-text">
          {{taskObj.task_name}}
        </span>
        <span v-if="deadlineTimeHHMM!=='00:00'"
            @click="toggleIsUpdating"
            class="task-item-time">
          {{deadlineTimeHHMM}}
        </span>
        <div class="delete-button">
          <a href="#" @click.prevent="deleteTask()"><i class="far fa-times-circle"></i></a>
        </div>
      </div>

      <div v-else style="display: block;
        border-top: 1px solid gray;
        border-bottom: 1px solid gray;
        border-radius: 3px;
        padding: 10px 0 10px 0;
        width: 100%">
        <input
               v-model="taskObj.task_name"
               type="text"
               placeholder="Название таска"
               style="width: 85%; margin-left: 1.4em; margin-bottom: 0; font-size: 20px">
        <textarea
            v-model="taskObj.task_description"
            placeholder="Описание таска"
            style="resize: none; margin-left: 1.4em; width: 85%;font-size: 20px">
        </textarea>
        <input
            v-model="newDeadlineTime"
            type="time"
            placeholder="чч:мм"
            style="
              float: right;
              margin-left: 0;
              margin-right: 10%;
              margin-bottom: 0;
              font-size: 20px;
              ">
        <a style="display: block;
                margin-left: 1em;
                margin-bottom: .1em;
                font-size: 25px;
                height: 30px;
                width: 30px;"
           @click="updateTask()">
          <i class="far fa-check-square"></i>
        </a>
      </div>

    </div>

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Task",
  data(){
    return{
      currentTask: {},
      isUpdating: false,
      // не (taskObj: this.task) потому что в task есть поле id, а в запрос это поле не передаётся
      taskObj: {
        task_name: this.task.task_name,
        task_description: this.task.task_description,
        deadline: this.task.deadline,
        is_finished: this.task.is_finished
      },
      newDeadlineTime: `${this.task.deadline.split('T')[1].split(':')[0]}:${this.task.deadline.split('T')[1].split(':')[1]}`
    }
  },
  props: {
    task: { },
  },
  computed:{
    // Возвращает время в формате hh-mm для редактирования таска
    deadlineTimeHHMM(){
      let arr = this.task.deadline.split('T')[1].split(':')
      return `${arr[0]}:${arr[1]}`
    }
  },

  methods:{
    // Удаление таска
    deleteTask(){
      axios.delete(`http://localhost:8081/api/tasks/${this.task.id}`)
          .then(() => this.$store.dispatch('refreshTasklist'))
    },

    // Изменение таска
    updateTask(){
      if (this.taskObj.task_name){
          let config = {
            data: this.taskObj
          }
          axios.patch(`http://localhost:8081/api/tasks/${this.task.id}`, config.data)
              .then(() => {
                this.$store.dispatch('refreshTasklist')
                this.toggleIsUpdating()
              }).catch(()=>alert('Введите корректную дату в формате чч:мм'));

      }
    },

    // Переключатель для темплэйта
    toggleIsUpdating(){
      this.isUpdating=!this.isUpdating
    }
  },
  watch:{
    task(){
      this.taskObj = this.task
    },

    // При изменении дедлайна нужно обновить данные для отправки в запросе
    newDeadlineTime(){
      let deadlineArray = this.taskObj.deadline.split('T')[0]
      this.taskObj.deadline = `${deadlineArray}T${this.newDeadlineTime}:00`
    },

    deadlineTimeHHMM(){
      this.newDeadlineTime = this.deadlineTimeHHMM
    }
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
    font-size: 22px;
    margin: 3px;
    //font-family: 'Karla', sans-serif;
    font-family: 'Exo 2', sans-serif;
    font-weight: 400;
  }
  .task-item-text:hover{
    cursor: pointer;
  }
  .task-item-time{
    font-size: 22px;
    margin: 0px;
    color: orangered;
    border: 1px solid gray;
    border-radius: 5px;
    padding: 0px 1px;
    //font-family: 'Karla', sans-serif;
    font-weight: 1000;
  }

  .checked{
    display: inline;

    .task-item-text{
      color: lightgrey;
    }

  }
  .unchecked{
    display: inline;

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