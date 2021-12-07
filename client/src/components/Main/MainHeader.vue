<template>
  <header id="header">
    <div class="header">
      <div class="top-nav">
        <div class="logo">
          <a href="#"><img src="../../img/logo.png" alt="logo"></a>
        </div>

        <div class="menu" v-if="!authorized">
          <a href="" @click.prevent="showDialog('Login')">Вход</a>
          <a href="" @click.prevent="showDialog('Registration')">Регистрация</a>
        </div>

<!--        Убрать инлайны-->
        <div class="menu" v-else style="
              color: white;
              font-size: 20px" >
          <span class="headerLogin">{{loginForCheck.inputLogin}}</span>
          <a href="" @click.prevent="logout">Выход</a>
        </div>
      </div>

    </div>

    <dialog-window class="dialog-window"
                   :isShow="dialogVisible"
                   :isLogin="isLogin"
                   :isRegistration="isRegistration"
                   @hideDialog="hideDialog">
      <div class="content-input-tasks" >
        <h1 v-if="isLogin">Вход</h1>
        <h1 v-else>Регистрация</h1>

        <input v-model="loginForCheck.inputLogin" type="text" size="40" placeholder="Логин">
        <br>
        <input v-model="loginForCheck.inputPassword" type="text" size="40" placeholder="Пароль">
        <br>
        <div class="dialog-window-button">
          <a href="#" v-if="isLogin" @click="login(), hideDialog()">Войти</a>
          <a href="#" v-else-if="isRegistration" @click="register(), hideDialog()">Зарегистрироваться</a>
        </div>

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

      isLogin: false,
      isRegistration: false,

      loginForCheck: {
        inputLogin: 'login',
        inputPassword: 'password'
      },

      responseLogin: {
        message: "",
        token: ""
      },

      responseRegistration:{
        message: ""
      },

    }
  },

  props:{
    authorized: { type: Boolean }
  },

  methods:{
    showDialog(operation){
      this.dialogVisible = !this.dialogVisible
      if (operation === 'Login'){
        this.isLogin = !this.isLogin
      }
      else if (operation === 'Registration'){
        this.isRegistration = !this.isRegistration
      }
    },

    hideDialog(){
      this.dialogVisible = false
      this.isLogin = false
      this.isRegistration = false
    },

    async login(){
      const article = {
        "login": this.loginForCheck.inputLogin,
        "password": this.loginForCheck.inputPassword
      };
      try {
        // eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2NDA3MTEyNjF9.YQiVoz3GBnTw7ZT_bNK8api3_sIwHghLWZT__9ob8qM

        const response = await axios.post('http://localhost:8081/api/login', article)

        this.responseLogin.message  = response.data.message
        this.responseLogin.token = response.data.token

        localStorage.setItem("token", this.responseLogin.token)

        // Меняем статус авторизации
        this.$emit("changeAuthStatus", true)

      } catch (e) {
        alert('error')
      }
    },

    async register(){
      const article = {
        "login": this.loginForCheck.inputLogin,
        "password": this.loginForCheck.inputPassword
      };
      let response
      try {
        // eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2NDA3MTEyNjF9.YQiVoz3GBnTw7ZT_bNK8api3_sIwHghLWZT__9ob8qM

         response = await axios.post('http://localhost:8081/api/register', article)

        this.responseRegistration.message = response.data.message
        alert(this.responseRegistration.message)
      } catch (e) {
        alert('Логин уже зарегистрирован')
      }
    },
    logout(){
      this.$emit("changeAuthStatus", false)
    }
  },
}

</script>

<style lang="scss">
.header{
  display: flex;
  align-items: center;
  margin: 2px 0;
  width: 100%;
  height: 75px;
  //background: linear-gradient(to right top, #ABADDD, #6E7091);
  //background-image: url("../../img/bg1.png"); #FF0101
  background: linear-gradient(to right top, #ABADDD, #5D84E6);
  border: 1px solid #90A5E6;
  border-radius: 7px;
}

.top-nav{
  display: flex;
  align-items: center;
  width: 70%;
  margin: 0 auto;
  justify-content: space-between;
}

.menu{
  a{
    width: 200px;
    padding: .4em 1.5em;
    background-color: transparent;
    border: 1px solid lightskyblue;
    border-radius: .4em;
    color: white;
    margin-right: .5em;
    text-decoration: none;
    font-size: 18px;
    letter-spacing: 2px;
  }
  a:hover{
    background: rgba(173,216,230,0.3);
  }
}

.logo img{
  width: 150px;
}

.headerLogin{
  margin-right: 20px;
}



</style>