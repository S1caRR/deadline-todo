<template>
  <div class="content-header">
    <div class="content-header-block-date">
      <h2>Просроченное</h2>
    </div>
    <input type="text" v-model="myFilter">

<!--    <my-calendar :dateList="dateList" :responseTasklist="responseTasklist" />-->
  </div>

  <div class="task-day" v-for="dayDate in deadlineList" :key="dayDate.id" >
    <tasklist-day :date="dayDate" :responseTasklist="responseTasklist" />
  </div>
</template>


<script>
import { Calendar, DatePicker } from 'v-calendar';
import TasklistDay from "../List/TasklistDay";
import axios from "axios";
import MyCalendar from "../Calendar/MyCalendar";

// Копипаста за недостатком времени
export default {
  components: {TasklistDay},
  data(){
    return{
      deadlineList: [],
      dateISONoTime: '',
      myFilter: ''
    }
  },
  computed:{
    responseTasklist(){
      return this.$store.getters.getTasklist.filter((item)=>{
        if(item.task_name.includes(this.myFilter)){
          return item
        }
      })
    }
  },
  props:{
    dateList: {},
  },
  methods:{
    getUnfinishedTasklist(){
      axios
          .get('http://localhost:8081/api/tasks', {params:{is_finished: false}})
          .then( response => {
            this.$store.commit('changeTasklist', Array.from(response.data.tasks));
          });
    },

    // Поскольку в TasklistDay принимается дата в формате
    getDeadlineISODatesNoTime(){
      for (let taskObject in this.responseTasklist) {
        let dateForListISOList = this.responseTasklist[taskObject].deadline.split('T')[0].split('-')
        let dateForList = new Date(Number(dateForListISOList[0]),
            Number(dateForListISOList[1])-1,
            Number(dateForListISOList[2]),
            23,59,59)
        if (this.deadlineList.indexOf(dateForListISOList.join('-'))===-1 && dateForList.getTime()<=(new Date()).getTime()){
          this.deadlineList.push(dateForListISOList.join('-'))
        }
      }
    },

  },

  mounted() {
    this.getUnfinishedTasklist()

  },

  watch:{
    responseTasklist(){
      this.getDeadlineISODatesNoTime();
    }
  },
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