<template>
  <header id="header">
    <div class="header">
      <div class="top-nav">
        <div class="logo">
          <a href="#"><img src="../../img/logo.png" alt="logo"></a>
        </div>

        <div class="menu">
          <a href="" @click.prevent="showDialog">Вход</a>
          <a href="">Регистрация</a>
        </div>
      </div>

    </div>

    <dialog-window :isShow="dialogVisible" @showDialog="showDialog">
      <div class="content-input-tasks" >

        <input type="text" size="50" placeholder="Логин">
        <input type="text" size="100" placeholder="Пароль">

        <a href="#" @click="login(), showDialog()">Добавить</a>

      </div>
    </dialog-window>

  </header>
</template>

<script>
import DialogWindow from "../UI/DialogWindow";
import axios from "axios";

export default {
  name: "MainHeader",
  components:{DialogWindow},

  data(){
    return{

      dialogVisible: false,

      loginForCheck: {
        "email":"email",
        "password":"password"
      },

      responseLogin: {
        message: "",
        token: ""
      }

    }
  },


  methods:{

    showDialog(){
      this.dialogVisible = !this.dialogVisible
    },

    async login(){
      const article = {
        "email": "email",
        "password": "password"
        // "Content-Type": "application/json"
      };
      try {
        // eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2NDA3MTEyNjF9.YQiVoz3GBnTw7ZT_bNK8api3_sIwHghLWZT__9ob8qM

        const response = await axios.post('http://localhost:8081/api/login', article)
        this.responseLogin.message  = response.data.message
        this.responseLogin.token = response.data.token
        alert(this.responseLogin.token)
        localStorage.setItem('token', this.responseLogin.token)
      } catch (e) {
        alert('error')
      }


    },

  },

  created() {

  }
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