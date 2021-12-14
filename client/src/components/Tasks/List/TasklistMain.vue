<template>
  <div class="content-header">
    <div class="content-header-block-date">
      <h2>Предстоящее</h2>
      <!--        <button @click="fetchTasks">GetTasks</button>-->
    </div>
<!--    <DatePicker v-model=date title-position="left" :min-date="new Date()" :attributes="attrs" is-expanded updateLayot>-->
<!--      <template #day-popover="{ }">-->
<!--          <tasks-day v-if="this.dateISONoTime" :date="this.dateISONoTime"-->
<!--                     :responseTasklist="responseTasklist "-->
<!--                             style="" />-->
<!--&lt;!&ndash;          <div v-else></div>&ndash;&gt;-->
<!--      </template>-->
<!--    </DatePicker>-->

  <my-calendar :dateList="dateList" :responseTasklist="responseTasklist" />
  </div>

    <div class="task-day" v-for="dayDate in deadlineList" :key="dayDate.id" >
      <tasklist-day :date="dayDate" :responseTasklist="responseTasklist" />
    </div>
</template>

<script>
import { Calendar, DatePicker } from 'v-calendar';
import TasklistDay from "./TasklistDay";
import axios from "axios";
import MyCalendar from "../Calendar/MyCalendar";

export default {
  name: "TasklistMain",
  components: {TasklistDay, Calendar, DatePicker, MyCalendar},
  data(){
    return{
      localeDate: [],
      date: new Date(),
      deadlineList: [],
      dateISONoTime: '',
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
        {
          dates: [],
          popover: true
        },
        {
          dates: new Date(),
          highlight: {
            color: 'red',
            fillMode: 'outline'
          },
        }
      ],
    }
  },
  computed:{
    responseTasklist(){
      return this.$store.getters.getTasklist
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
              // this.$store.dispatch('refreshTasklist')
              // this.responseTasklist = this.$store.getters.getTasklist;this.responseTasklist = this.$store.getters.getTasklist;

           });
    },
    // getDeadlineDates(){
    //   for (let taskObject in this.responseTasklist){
    //     let dateForCalendar = this.responseTasklist[taskObject].deadline.split('T')[0].split('-')
    //     dateForCalendar = new Date(Number(dateForCalendar[0]),Number(dateForCalendar[1])-1,Number(dateForCalendar[2]),23,59,59)
    //     // dateForCalendar.setTime()
    //     if (dateForCalendar.getTime()>=(new Date()).getTime()){
    //       if ((this.attrs[0].dates.indexOf(dateForCalendar)===-1))
    //         this.attrs[0].dates.push(dateForCalendar)
    //     }
    //   }
    // },

    getDeadlineISODatesNoTime(){
      for (let taskObject in this.responseTasklist) {
        let dateForListISOList = this.responseTasklist[taskObject].deadline.split('T')[0].split('-')
        let dateForList = new Date(Number(dateForListISOList[0]),
            Number(dateForListISOList[1])-1,
            Number(dateForListISOList[2]),
            23,59,59)
        if (this.deadlineList.indexOf(dateForListISOList.join('-'))===-1 && dateForList.getTime()>=(new Date()).getTime()){
          this.deadlineList.push(dateForListISOList.join('-'))
        }
      }
    },

    // toISODate(date){
    //   date = date.toLocaleDateString().split('.')
    //   return `${date[2]}-${date[1]}-${date[0]}`
    // }

  },

  mounted() {
    this.getUnfinishedTasklist()
    // this.attrs[1].dates = this.dateList
    // this.getDeadlineDates()
  },

  watch:{
    // date(){
    //   if (this.date){
    //     this.localeDate = this.date.toLocaleString().split(',')[0].split('.')
    //     this.dateISONoTime = `${this.localeDate[2]}-${this.localeDate[1]}-${this.localeDate[0]}`
    //   }
    // },
    responseTasklist(){
      // this.getDeadlineDates();
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