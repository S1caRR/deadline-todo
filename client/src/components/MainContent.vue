 <template>
  <section id="content">

    <div class="content-header">
      <div class="content-header-block-date">
        <h2>Сегодня</h2>
      </div>
    </div>

    <div class="content-tasks-block">
      <div class="content-tasks">
        <div class="tasks-item">
          <label for="checkbox-item"><input id="checkbox-item">123</label>
        </div>


        <input type="checkbox"> task 2
        <input type="checkbox"> task 3
      </div>

      <div  class="content-input-tasks">
        <input type="text" size="40">
        <a href="#">Добавить</a>
      </div>

    </div>
  </section>
</template>

<script>
export default {
  name: "MainContent",
  data() {

  },
  methods: {

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

.content-input-tasks{
  input{

  }
}

.content-tasks-block{
  margin: 3em 3em;
  align-items: center;
  width: 90%;
  .content-tasks{
    input{

    }
  }
}


</style>