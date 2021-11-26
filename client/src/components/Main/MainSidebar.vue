<template>
  <section id="sidebar">

    <div class="core-block">
      <a href=""> <i class="fas fa-tasks"></i>Сегодня<span>0</span></a>
      <a href=""> <i class="fa fa-calendar"></i>Предстоящее<span>0</span></a>
      <a href=""> <i class="fa fa-calendar-times"></i>Архив<span>0</span></a>
    </div>
  </section>
</template>

<script>
export default {
  name: "MainSidebar"
}
</script>

<style scoped lang="scss">
#sidebar{
  border-right: 1px solid darkgray;
  height: 100%;
  background-color: rgb(191 191 191);
  border-right: 1px solid black;
  font-size: 20px;
  font-family: sans-serif;
}
.core-block {
  text-align: left;
  justify-content: space-between;
  padding: 0 1em;
  display: flex;
  flex-direction: column;
  border-bottom: 1px solid gray;
  margin: .2em 0px;

  a{
    margin-top: .3em;
    color: black;
    text-decoration: none;
  }
  a:last-child {
    margin-bottom: .5em;
  }
  i{
    float: left;
    padding-right: .7em;
    margin-right: .4em;
    font-size: .8em;
  }
  span{
    font-size: .8em;
    color: lightslategray;
    margin-left: .3em;
  }
}

</style>