<template>
  <div>
    <main-header :authorized="authorized" @changeAuthStatus="changeAuthStatus" />
    <div>
      <div class="main">
        <main-sidebar/>
        <main-content v-if="authorized" />
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

  data(){
    return{
      authorized: false
    }
  },

  methods:{
    abortLocalStorage(){
      localStorage.clear()
    },

    changeAuthStatus(status=false){
      this.authorized = status
    }
  },

  mounted() {
    this.abortLocalStorage()
  },

  watch:{
    authorized(){
      return this.authorized
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