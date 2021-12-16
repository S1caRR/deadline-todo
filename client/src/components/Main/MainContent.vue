<template>
  <section id="content">
    <router-view :dateList="getDateList"></router-view>
  </section>
</template>

<script>
 import {genCalendarObj} from "calendar-generator";
 import Today from "../Tasks/Today/Today";
 import TasklistMain from "../Tasks/List/TasklistMain";
 import Expired from "../Tasks/Expired/Expired";

export default {
  components:{TasklistMain, Today, Expired},
  computed:{
    // Генератор дат, возвращает список дат в формате yyyy-mm-dd
    getDateList(){
      let dateNow = new Date()
      let dateNowISO = this.toISODate(dateNow)

      let dateAfter = new Date(
          dateNow.getFullYear()+1,
          (dateNow.getMonth()-1),
          dateNow.getDate())
      dateAfter = this.toISODate(dateAfter)

      let cObj = genCalendarObj(dateNowISO, dateAfter).date
      let datelist = []
      for (let dateObj in cObj){
        if (cObj[dateObj].inputRange){
          datelist.push(dateObj)
        }
      }
      return datelist
    },
  },

  methods:{
    // Преобразует получаемый параметр типа Date в формат yyyy-mm-dd,
    // не toISOString потому что Date в таком случае преобразуется без учёта таймзоны
    toISODate(date){
      date = date.toLocaleDateString().split('.')
      return `${date[2]}-${date[1]}-${date[0]}`
    },
  },
}
</script>

<style lang="scss">
#content{
  //background: linear-gradient(to right top, #404297, #404297, #4a0771);
  //background: #16E0B0;
  margin: 1px 20% 0 2px;
  border-radius: 7px;
  border: 1.5px #90A5E6 solid;
  width: 70%;
  //margin-right: 20%;
}

</style>