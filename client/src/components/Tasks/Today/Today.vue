<template>
  <div class="content-header">
    <div class="content-header-block-date">
      <h2>Today</h2>
    </div>
  </div>

  <div class="task-day" >
    <tasks-day :date="dateList[0]" :responseTasklist="responseTasklist" />
  </div>
</template>

<script>
import TasksDay from "../List/TasklistDay";
export default {
  name: "Today",
  components:{ TasksDay},
  data(){
    return{

    }
  },
  props:{
    dateList: {},
    responseTasklist: {}
  },
  methods:{

  },
  mounted() {
    this.$emit('fetchTasks')
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