<template>
  <section id="content">

    <div class="content-header">
      <div class="content-header-block-date">
        <h2>Список задач на месяц</h2>
<!--        <button @click="fetchTasks">GetTasks</button>-->
      </div>
    </div>

    <calendar-month/>

    <div class="task-day" v-for="dayDate of cObj" :key="dayDate.value" >
      <tasks-day v-if="dayDate.inputRange" :date="dayDate" :responseTasklist="responseTasklist" />
    </div>

  </section>
</template>

<script>
 //import TaskList from "../Tasks/TaskList";
 import TasksDay from "../Tasks/List/TasklistDay";
 import CalendarMonth from "../Tasks/Calendar/CalendarMonth";
 import {genCalendarObj} from "calendar-generator";
 import axios from "axios";

export default {
  components:{TasksDay, CalendarMonth},

  data() {
    return{
      response: null,
      responseTask: { },
      responseTasklist: [],
      cObj: {},
      token: "",
    }
  },

  methods:{
    genCalendarObject(){
      let dateNow = new Date()
      let dateNowISO = dateNow.toISOString().split('T')[0].split('-')

      let dateAfter = new Date()
      // Прибавляем месяц к новой дате, но в данном случае ещё меняется и год, это нужно учесть
      dateAfter.setMonth((Number(dateNowISO[1])+1)%13)
      dateAfter.setFullYear(Number(dateNowISO[0])+1)
      let dateAfterISO = dateAfter.toISOString().split('T')[0].split('-')

      // Вроде можно без сбора по кусочкам и деления ( убрать split('-') ) ???
      const fromDate = `${dateNowISO[0]}-${dateNowISO[1]}-${dateNowISO[2]}`
      const toDate = `${dateAfterISO[0]}-${dateAfterISO[1]}-${dateAfterISO[2]}`

      this.cObj = genCalendarObj(fromDate, toDate).date
    },


    async fetchTasks(){
      this.token = localStorage.getItem("token").toString()

      const config = {
        headers: {
          Authorization: this.token
        }
      }

      try {
        // eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjpudWxsLCJleHAiOjE2NDA3OTIxNDh9.gK_0QsVkXhwlAiFrJusYv_nu8RiCmIFkBJd6GGy7EWY

        this.response = await axios.get('http://localhost:8081/api/tasks', config)
        this.responseTask = this.response
        this.responseTasklist = Array.from(this.responseTask.data.data.tasks)

      } catch (e) {
        alert(e.message)
      }
    },
    refreshResponse(){
      this.responseTask = this.response
      this.responseTasklist = Array.from(this.responseTask.data.data.tasks)
    }

  },

  mounted() {
    this.genCalendarObject()
    this.fetchTasks()
  },

  watch:{
    response(){
      this.refreshResponse()
      this.token = localStorage.getItem('token').toString()
    },

  }
}
</script>

<style scoped lang="scss">
#content{
  //background: linear-gradient(to right top, #404297, #404297, #4a0771);
  //background: #16E0B0;
  margin: 1px 20% 0px 2px;
  border-radius: 10px;
  border: 2px #90A5E6 solid;
  width: 70%;
  //margin-right: 20%;
}
.content-header {
  width: 95%;
  margin: 0 auto;
  display: block;
  //justify-content: space-between;
  align-items: center;
  border-bottom: 2px solid cadetblue;

}
.content-header-block-date {
  display: block;
  width: 100%;
  margin-top: 10px;
  margin-bottom: 20px;
  text-align: center;
}

.content-tasks-block{
  margin: 0em 3em;
  align-items: center;
  width: 90%;

  .content-tasks{
    margin-bottom: 10px;
    border: 2px solid teal;
  }
  .task-item:first-child{
    border-top: 5px solid teal;
  }

  .task-day:first-child{
    border-top: 5px solid teal;
  }
}
</style>