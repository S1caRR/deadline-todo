<template>
  <section id="sidebar">
    <div class="core-block">
      <router-link to="/today">
        <i class="fas fa-tasks"></i>Сегодня<span>{{ todayCount }}</span>
      </router-link>

      <router-link to="/upcoming">
        <i class="fa fa-calendar"></i>Предстоящее<span>{{ upcomingCount }}</span>
      </router-link>

      <router-link to="/archive">
          <i class="fa fa-calendar-times"></i>Архив<span>0</span>
      </router-link>

      <router-link to="/expired">
          <i class="fa fa-calendar-times"></i>Просроченное<span>0</span>
      </router-link>
    </div>
  </section>
</template>

<script>
export default {
  name: "MainSidebar",
  data(){
    return{
      // todayCount: 0,
      // upcomingCount: 0,
      // archiveCount: 0
    }
  }
}
</script>

<style scoped lang="scss">
#sidebar {
  position: sticky;
  top: 20px;
  margin: 0 40px 0 35%;
  border: 2px solid #90A5E6;
  border-radius: 12px;
  max-height: 175px
}
.core-block {
  display: flex;
  z-index: 0;
  background: linear-gradient(to right top,  #90A5E6, #ABADDD);
  //height: 90%;
  width: auto;
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
  color: black;
    a{
      margin-top: .3em;
      color: white;
      text-decoration: none;
      letter-spacing: 1px;
      font-size: 1em;
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