<template>
  <div>
    <main-header />
    <div>
      <div class="main">
        <main-sidebar/>
        <main-content v-if="getAuthStatus && getToken" />
        <div v-else class="need-to-auth-text">Для продолжения необходимо авторизоваться</div>
      </div>
    </div>
  </div>
</template>

<script>
import MainHeader from "./MainHeader";
import MainSidebar from "./MainSidebar";
import MainContent from "./MainContent";
import axios from "axios";


export default {
  components: {MainHeader, MainContent, MainSidebar},
  name: "MainContainer",

  computed:{
    getAuthStatus(){
      return this.$store.getters.getAuthStatus
    },
    getToken(){
      return this.$store.getters.getToken
    }
  },

  watch:{
    getToken(){
      axios.defaults.headers.common['Authorization'] = this.getToken
    }
  }
}
</script>

<style lang="scss">

.main{
  display: grid;
  grid-template-columns:2fr 5fr;
  //height: 1080px;
}
.need-to-auth-text{
  width: 80%;
  color: orange;
  font-size: 30px;
  border: 2px solid #ABADDD;
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