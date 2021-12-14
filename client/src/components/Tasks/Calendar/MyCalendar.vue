<template>
  <DatePicker v-model="date" title-position="left" :min-date="new Date()" :attributes="attrs" is-expanded>
    <template v-if="this.dateISONoTime " #day-popover="{ day }">
      <tasklist-day v-if="this.dateISONoTime " :date="this.dateISONoTime" :responseTasklist="responseTasklist" />
      <div v-else></div>
    </template>
  </DatePicker>
</template>

<script>
import { Calendar, DatePicker } from 'v-calendar';
import TasklistDay from '../List/TasklistDay'
export default {
  components: {DatePicker, Calendar, TasklistDay},
  data() {
    return {
      localeDate: [],
      date: new Date(),
      deadlineList: [],
      dateISONoTime: '',
      attrs: [
        {
          dot: 'red',
          dates: [],
          popover: true
        },
        {
          dates: 'all',
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
  props: {
    responseTasklist: {},
    dateList: {}
    // date: {},
    // dateISONoTime: {},
    // responseTasklist: []
  },
  computed: {
    responseTasklist() {
      return this.$store.getters.getTasklist
    }
  },
  methods: {
    getDeadlineDates() {
      for (let taskObject in this.responseTasklist) {
        let dateForCalendar = this.responseTasklist[taskObject].deadline.split('T')[0].split('-')
        dateForCalendar = new Date(Number(dateForCalendar[0]), Number(dateForCalendar[1]) - 1, Number(dateForCalendar[2]), 23, 59, 59)
        // dateForCalendar.setTime()
        if (dateForCalendar.getTime() >= (new Date()).getTime()) {
          if ((this.attrs[0].dates.indexOf(dateForCalendar) === -1))
            this.attrs[0].dates.push(dateForCalendar)
        }
      }
    },

    getDeadlineISODatesNoTime() {
      for (let taskObject in this.responseTasklist) {
        let dateForListISOList = this.responseTasklist[taskObject].deadline.split('T')[0].split('-')
        let dateForList = new Date(Number(dateForListISOList[0]),
            Number(dateForListISOList[1]) - 1,
            Number(dateForListISOList[2]),
            23, 59, 59)
        if (this.deadlineList.indexOf(dateForListISOList.join('-')) === -1 && dateForList.getTime() >= (new Date()).getTime()) {
          this.deadlineList.push(dateForListISOList.join('-'))
        }
      }
    },
  },

  mounted() {
    this.attrs[1].dates = this.dateList
    // this.getDeadlineDates()
  },

  watch:{
    date(){
      if (this.date){
        this.localeDate = this.date.toLocaleString().split(',')[0].split('.')
        this.dateISONoTime = `${this.localeDate[2]}-${this.localeDate[1]}-${this.localeDate[0]}`
      }
    },
    responseTasklist(){
      this.getDeadlineDates();
      this.getDeadlineISODatesNoTime();
    }
  },
}
</script>

<style scoped>

</style>