<template>
  <div id="app">
    <main-container></main-container>
  </div>
</template>

<script>
import MainContainer from "./components/Main";

export default {
  components: {MainContainer},
  name: "App",
}
</script>

<style>

*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}


/*#app {*/
/*  font-family: Avenir, Helvetica, Arial, sans-serif;*/
/*  -webkit-font-smoothing: antialiased;*/
/*  -moz-osx-font-smoothing: grayscale;*/
/*  text-align: center;*/
/*  color: #2c3e50;*/
/*}*/

</style>