 <template>
  <section id="content">

    <div class="content-header">
      <div class="content-header-block-date">
        <h2>Список задач на сегодня</h2>
      </div>
    </div>

    <div class="content-tasks-block">

      <div class="tasks"
           v-for="task in taskList"
           v-bind:key="task">
        <div class="task-item"><input type="checkbox"> {{task.title}} </div>
      </div>

      <div  class="content-input-tasks">
        <input type="text" size="100" placeholder="Название таска"
               v-bind:value="newPostTitle"
               @input="newPostTitle = $event.target.value">
        <a href="#" v-on:click="addTask">Добавить</a>
      </div>

    </div>
  </section>
</template>

<script>
export default {

  data() {
    return{
      taskList: [
        {id: Date.now(), title: "task 1"},
      ],
      newPostTitle: "",
    }
  },

  methods: {
    addTask() {
      const newTask = {
        id: Date.now(),
        title: this.newPostTitle
      }
      this.taskList.push(newTask)
    }

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