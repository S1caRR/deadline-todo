<template>
  <div>
    <main-header/>
    <div>
      <div class="main">
        <main-sidebar/>
        <main-content/>
      </div>
    </div>
  </div>
</template>

<script>
import MainHeader from "./MainHeader";
import MainSidebar from "./MainSidebar";
import MainContent from "./MainContent";

export default {
  components: {MainHeader, MainContent, MainSidebar},
  name: "MainContainer",
}
</script>

<style scoped lang="scss">

.main{
  display: grid;
  grid-template-columns: 1fr 5fr;
  height: 1080px;
}

/*#nav {*/
/*  padding: 30px;*/
/*}*/

/*#nav a {*/
/*  font-weight: bold;*/
/*  color: #2c3e50;*/
/*}*/

/*#nav a.router-link-exact-active {*/
/*  color: #42b983;*/
/*}*/
</style>