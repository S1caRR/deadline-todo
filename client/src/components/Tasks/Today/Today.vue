<template>
  <div class="content-header">
    <div class="content-header-block-date">
      <h2>Today</h2>
    </div>
  </div>

  <div class="task-day" >
    <tasklist-day :date="dateList[0]" :responseTasklist="responseTasklist" />
  </div>
</template>

<script>
import TasklistDay from "../List/TasklistDay";
import axios from "axios";
export default {
  name: "Today",
  components:{ TasklistDay},
  data(){
    return{

    }
  },
  props:{
    dateList: {},
  },
  computed:{
    responseTasklist(){
      return this.$store.getters.getTasklist
    }
  },
  methods:{
    refreshResponse(){
      axios
          .get('http://localhost:8081/api/tasks', {params:{is_finished: false}})
          .then( response => {
            this.$store.commit('changeTasklist', Array.from(response.data.tasks));
          });

    }
  },
  mounted() {
    this.refreshResponse()
  }
}
</script>

<style scoped lang="scss">
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