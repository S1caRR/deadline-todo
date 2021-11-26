 <template>
  <section id="content">

    <div class="content-header">
      <div class="content-header-block-date">
        <h2>Список задач на сегодня</h2>
      </div>
    </div>

    <div v-for="day of cObj.date" :key="day.id" >
      <tasks-day :date="day"/>
    </div>


  </section>
</template>

<script>
 //import TaskList from "../Tasks/TaskList";
 import TasksDay from "../Tasks/TasklistDay";
 import {genCalendarObj} from "calendar-generator";

export default {
  components:{TasksDay},

  data() {
    return{

      cObj: {},
    }
  },

  methods:{
    genCalendarObject(){
      let dateNow = new Date()
      const fromDate = `${dateNow.getFullYear()}-${dateNow.getMonth()}-${dateNow.getDate()}` // format: 'YYYY-MM-DD
      const toDate = `${dateNow.getFullYear()}-${dateNow.getMonth()+2}-${dateNow.getDate()}`
      this.cObj = genCalendarObj(fromDate, toDate)
    }
  },

  beforeMount() {
    this.genCalendarObject()
  },

}
</script>

<style scoped lang="scss">
.content-header {
  width: 90%;
  margin: 0 auto;
  display: block;
  //justify-content: space-between;
  align-items: center;
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
  .task-item{

  }
}
</style>