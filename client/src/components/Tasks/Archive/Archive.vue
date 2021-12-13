<template>
  <div class="content-header">
    <div class="content-header-block-date">
      <h2>Архив</h2>
    </div>
  </div>

  <div class="task-day" v-for="dayDate in dateList" :key="dayDate" >
    <tasks-day :date="dayDate" :responseTasklist="responseFinishedTasklist" />
  </div>
</template>

<script>
import axios from "axios";
import TasksDay from "../List/TasklistDay";

export default {
  name: "Archive",
  data(){
    return{
      responseFinishedTasklist: [],
      dateList: []
    }
  },
  components:{ TasksDay },
  methods:{
    async fetchFinishedTasks() {
      this.token = localStorage.getItem("token").toString()

      const config = {
        headers: {
          Authorization: this.token
        },
        params: {
          is_finished: true
        }
      }

      try {
        // eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjpudWxsLCJleHAiOjE2NDA3OTIxNDh9.gK_0QsVkXhwlAiFrJusYv_nu8RiCmIFkBJd6GGy7EWY

        let response = await axios.get('http://localhost:8081/api/tasks', config)
        this.responseFinishedTasklist = Array.from(response.data.tasks)

      } catch (e) {
        alert(e.message)
      }

      for (let taskObject in this.responseFinishedTasklist){
        let dateForCalendar = this.responseFinishedTasklist[taskObject].deadline.split('T')[0]
        if (this.dateList.indexOf(dateForCalendar) === -1){
          this.dateList.push(dateForCalendar)
        }

      }

      // axios
      //     .get('https://api.coindesk.com/v1/bpi/currentprice.json')
      //     .then(response => (this.info = response));
    },


  },

  mounted() {
    this.fetchFinishedTasks()
  }
}
</script>

<style scoped>

</style>