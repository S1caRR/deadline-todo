<template>
  <div class="content-header">
    <div class="content-header-block-date">
      <h2>Список задач на месяц</h2>
      <!--        <button @click="fetchTasks">GetTasks</button>-->
    </div>
    <DatePicker v-model="this.date" title-position="left" :min-date="new Date()" :attributes="attrs" is-expanded>
      <template v-if="this.dateISONoTime && this.date" #day-popover="{ day }" >
<!--        <div v-if="this.dateISONoTime && this.date" class="text-xs text-gray-300 font-semibold text-center">-->
          <tasklist-day-info v-if="this.dateISONoTime && this.date" :date="this.dateISONoTime" :responseTasklist="responseTasklist" />
          <div v-else></div>
<!--        </div>-->
      </template>

    </DatePicker>

<!--    <DatePicker v-model="date" />-->
  </div>

  <div class="task-day" v-for="dayDate in dateList" :key="dayDate" >
    <tasks-day :date="dayDate" :responseTasklist="responseTasklist" />
  </div>
</template>

<script>
import { Calendar, DatePicker } from 'v-calendar';
import TasksDay from "./TasklistDay";
import TasklistDayInfo from "./TasklistDayInfo";

export default {
  name: "TasklistMain",
  components: {TasksDay, Calendar, DatePicker, TasklistDayInfo},
  data(){
    return{
      localeDate: [],
      date: new Date(),
      dateISONoTime: '',
      dateObjList: [],
      taskList: [],
      attrs: [
        {
          // highlight: {
          //   color: 'red',
          //   fillMode: 'outline'
          // },
          dot: 'red',
          dates: [],
          popover: true
          //     {
          //   visibility: 'focus',
          //   hideIndicator: true,
          // }
        },
      ],
    }
  },
  props:{
    dateList: {},
    responseTasklist: { }
  },
  methods:{


  },
  mounted() {
    this.$emit('onFetchTasks')
    this.getDeadlines
    this.attrs.dates = this.dateObjList
  },
  computed:{
    getDeadlines(){
      for (let taskObject in this.responseTasklist){
        let dateForCalendar = this.responseTasklist[taskObject].deadline.split('T')[0].split('-')
        dateForCalendar = new Date(dateForCalendar[0],Number(dateForCalendar[1])-1,dateForCalendar[2])
        if (dateForCalendar.getTime()>=(new Date()).getTime() ){
          this.attrs[0].dates.push(dateForCalendar)
        }

      }
    },
  },
  watch:{
    responseTasklist(){
      this.getDeadlines
    },
    date(){
      if (this.date){
        this.localeDate = this.date.toLocaleString().split(',')[0].split('.')
        this.dateISONoTime = `${this.localeDate[2]}-${this.localeDate[1]}-${this.localeDate[0]}`
      }
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