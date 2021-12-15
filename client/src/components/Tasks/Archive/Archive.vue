<template>
  <div class="content-header">
    <div class="content-header-block-date">
      <h2>Архив</h2>
    </div>
  </div>

  <div class="task-day" v-for="dayDate in dateList" :key="dayDate" >
    <tasklist-day :date="dayDate" :responseTasklist="responseFinishedTasklist" />
  </div>
</template>

<script>
import axios from "axios";
import TasklistDay from "../List/TasklistDay";

export default {
  name: "Archive",
  data(){
    return{
      responseFinishedTasklist: [],
      dateList: []
    }
  },
  components:{ TasklistDay },
  methods:{
    fetchFinishedTasks() {
      axios.get('http://localhost:8081/api/tasks', { params: {is_finished: true}})
          .then( response => {
            this.responseFinishedTasklist = Array.from(response.data.tasks)
            for (let taskObject in this.responseFinishedTasklist){
              let dateForList = this.responseFinishedTasklist[taskObject].deadline.split('T')[0]
              if (this.dateList.indexOf(dateForList) === -1){
                this.dateList.push(dateForList)
              }
            }
          });
    },

  },

  mounted() {
    this.fetchFinishedTasks()
  }
}
</script>

<style scoped>
.content-header-block-date {
  display: block;
  width: 100%;
  margin-top: 10px;
  margin-bottom: 20px;
  text-align: center;
}
.content-header {
   width: 95%;
   margin: 0 auto;
   display: block;
 //justify-content: space-between;
   align-items: center;
   border-bottom: 2px solid cadetblue;

 }
</style>