<template>
  <section id="sidebar">

    <div class="core-block">
<!--      <a href="today"> <i class="fas fa-tasks"></i>Сегодня<span>0</span></a>-->
<!--      <a href="/upcoming"> <i class="fa fa-calendar"></i>Предстоящее<span>0</span></a>-->
<!--      <a href="archive"> <i class="fa fa-calendar-times"></i>Архив<span>0</span></a>-->
<!--      <a href="calendar"> <i class="fa fa-calendar-times"></i>Календарь<span>0</span></a>-->
      <router-link to="/today">
        <i class="fas fa-tasks"></i>Сегодня<span>{{ todayCount }}</span>
      </router-link>
      <router-link to="/upcoming">
        <i class="fa fa-calendar"></i>Предстоящее<span>{{ upcomingCount }}</span>
      </router-link>
      <router-link to="/archive">
          <i class="fa fa-calendar-times"></i>Архив<span>0</span>
      </router-link>
      <router-link to="/calendar">
          <i class="fa fa-calendar-times"></i>Календарь<span>0</span>
      </router-link>
    </div>
  </section>
</template>

<script>
export default {
  name: "MainSidebar",
  data(){
    return{
      todayCount: 0,
      upcomingCount: 0,
      archiveCount: 0
    }
  }
}
</script>

<style scoped lang="scss">
#sidebar{
  margin-left: 50%;
}
.core-block {
  height: 130px;
  //background-color: rgb(191 191 191);
  border: 2px solid #90A5E6;
  min-font-size: 5px;
  //font-size: 40px;
  border-radius: 7px;
  position: sticky;
  top: 10px;
  z-index: 0;
  background: linear-gradient(to right top,  #90A5E6, #ABADDD);
  //height: 90%;
  //width: 15%;
  //background: black;
  //position: fixed;
  text-align: left;
  justify-content: space-between;
  padding: 0 1em;
  display: flex;
  flex-direction: column;
  //border-bottom: 1px solid gray;
  //margin: .2em 0px;

  //margin-left: 40px;
  margin-right: 5px;

    a{
      margin-top: .3em;
      color: white;
      text-decoration: none;
      letter-spacing: 1px;
    }
    a:last-child {
      margin-bottom: .5em;
    }
    a:hover{
      background: rgba(173,216,230,0.3);
    }
    i{
      float: left;
      padding-right: .5em;
      padding-top: .25em;
      margin-right: .4em;
      font-size: .8em;
      color: black;
    }
    span{
      font-size: .8em;
      color: lightslategray;
      padding-left: .3em;
    }
}

</style>