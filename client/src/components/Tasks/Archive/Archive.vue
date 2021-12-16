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
  components:{ TasklistDay },
  data(){
    return{
      // responseFinishedTasklist: [],
      dateList: []
    }
  },

  computed:{
    responseFinishedTasklist(){
      return this.$store.getters.getFinishedTasklist
    }
  },

  methods:{
    fetchFinishedTasks() {
      axios.get('http://localhost:8081/api/tasks', { params: {is_finished: true}})
          .then( response => {
            let responseFinishedTasklist = Array.from(response.data.tasks)
            for (let taskObject in responseFinishedTasklist){
              let dateForList = responseFinishedTasklist[taskObject].deadline.split('T')[0]
              if (this.dateList.indexOf(dateForList) === -1){
                this.dateList.push(dateForList)
              }
            }
            this.$store.commit('changeFinishedTasklist', responseFinishedTasklist)
          });
    },

  },

  watch:{
    responseFinishedTasklist(){

    }
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