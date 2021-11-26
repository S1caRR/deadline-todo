<template>
  <header id="header">
    <div class="header">
      <div class="top-nav">
        <div class="logo">
          <a href="#"><img src="../../img/logo.png" alt="logo"></a>
        </div>

        <div class="menu">
          <a href="">Вход</a>
          <a href="">Регистрация</a>
        </div>
      </div>

    </div>
  </header>
</template>

<script>
export default {
  name: "MainHeader"
}
</script>

<style  scoped lang="scss">
.header{
  display: flex;
  align-items: center;
  width: 100%;
  height: 75px;
  background-color: black;
  border-bottom: 1px solid black;
}

.top-nav{
  display: flex;
  align-items: center;
  width: 1180px;
  margin: 0 auto;
  justify-content: space-between;
}

.menu{
  a{
    width: 200px;
    padding: .5em 2em;
    background-color: transparent;
    border: 1px solid lightskyblue;
    border-radius: .4em;
    color: white;
    margin-right: .5em;
    text-decoration: none;
  }

}

.logo img{
  width: 150px;
}


</style>