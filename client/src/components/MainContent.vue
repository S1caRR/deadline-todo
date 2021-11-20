 <template>
  <section id="content">

    <div class="content-header">
      <div class="content-header-block-date">
        <h2>Список задач на сегодня</h2>
      </div>
    </div>

    <div class="content-tasks-block">
        <task-list :taskList="taskList"/>

      <div  class="content-input-tasks">
        <input type="text" size="100" placeholder="Название таска"
               v-model="newTaskTitle">
        <a href="#" v-on:click="addTask">Добавить</a>
      </div>

    </div>

  </section>
</template>

<script>
 import TaskList from "./Tasks/TaskList";

export default {
  components:{ TaskList},

  data() {
    return{
      taskList: [],
      newTaskTitle: "",
    }
  },

  methods: {
    addTask() {
      if (this.newTaskTitle){
        const newTask = {
          id: Date.now(),
          title: this.newTaskTitle
        }
        this.taskList.push(newTask)
        this.newTaskTitle = ""
      }
    },

  }

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