 <template>
  <section id="content">

    <div class="content-header">
      <div class="content-header-block-date">
        <h2>Список задач на сегодня</h2>
        <button @click="fetchTasks">GetTasks</button>
      </div>
    </div>

    <div v-for="day of cObj" :key="day.value" >
      <tasks-day v-if="day.inputRange" :date="day" :responseTasklist="responseTasklist" />
    </div>


  </section>
</template>

<script>
 //import TaskList from "../Tasks/TaskList";
 import TasksDay from "../Tasks/TasklistDay";
 import {genCalendarObj} from "calendar-generator";
 import axios from "axios";

export default {
  components:{TasksDay},

  data() {
    return{
      responseTask: { },
      responseTasklist: [],
      cObj: {},
      token: ""
    }
  },

  methods:{
    genCalendarObject(){

      let dateNow = new Date()
      const fromDate = `${ dateNow.getFullYear() }-${ dateNow.getMonth() + 1 }-${ dateNow.getDate() }` // format: 'YYYY-MM-DD
      const toDate = `${ dateNow.getFullYear()+1 }-${ dateNow.getMonth() + 1 }-${ dateNow.getDate() }`

      this.cObj = genCalendarObj(fromDate, toDate).date
    },

    async fetchTasks(){
      this.token = localStorage.getItem('token').toString()
      const headers = {
        Authorization: this.token
      }

      this.isPostLoading = true
      try {
        // eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2NDA3MTEyNjF9.YQiVoz3GBnTw7ZT_bNK8api3_sIwHghLWZT__9ob8qM
        // eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjpudWxsLCJleHAiOjE2NDA3OTIxNDh9.gK_0QsVkXhwlAiFrJusYv_nu8RiCmIFkBJd6GGy7EWY

        const response = await axios.get('http://localhost:8081/api/tasks', {headers})
        this.responseTask = response
        this.responseTasklist = Array.from(this.responseTask.data.data)

      } catch (e) {
        alert(e.message)
      } finally {
        this.isPostLoading = false
      }

    },

  },

  created() {
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