<template>
  <header id="header">
    <div class="header">
      <div class="top-nav">
        <div class="logo">
          <a href="#"><img src="../../img/logo.png" alt="logo"></a>
        </div>

        <div class="menu" v-if="!getAuthStatus">
          <a href="" @click.prevent="showDialog('Login')">Вход</a>
          <a href="" @click.prevent="showDialog('Registration')">Регистрация</a>
        </div>

<!--        Убрать инлайны-->
        <div v-else class="menu" style="
              color: white;
              font-size: 20px" >
          <span class="headerLogin">{{getUsername}}</span>
          <header-profile :username="getUsername" :tgID="getTgID"/>
          <a href="" @click.prevent="logout">Выход</a>
        </div>
      </div>

    </div>

<!--    <dialog-window v-if="$store.getters.getIsShowDialogHeader" class="dialog-window"-->
<!--                   :isLogin="isLogin"-->
<!--                   :isRegistration="isRegistration"-->
<!--                   @hideDialog="hideDialog">-->
      <dialog-window :isShow="isShow" class="dialog-window"
                     :isLogin="isLogin"
                     :isRegistration="isRegistration"
                     @hideDialog="hideDialog">
      <div class="content-input-tasks" >
        <h1 v-if="isLogin">Вход</h1>
        <h1 v-else>Регистрация</h1>

        <input v-model="loginForCheck.inputLogin" type="text" size="30" placeholder="Логин">
        <br>
        <input v-model="loginForCheck.inputPassword" type="text" size="30" placeholder="Пароль">
        <br>
        <div class="dialog-window-button">
          <a href="#" v-if="isLogin" @click="login(), hideDialog()">Войти</a>
<!--          , hideDialog()-->
          <a href="#" v-else-if="isRegistration" @click="register(), hideDialog()">Зарегистрироваться</a>
        </div>

      </div>
    </dialog-window>

  </header>
</template>

<script>
import DialogWindow from "../UI/DialogWindow";
import axios from "axios";
import store from "../../store";
import HeaderProfile from "../Profile/HeaderProfile";

export default {
  name: "MainHeader",
  components:{HeaderProfile, DialogWindow},

  data(){
    return{
      isShow: false,
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
  computed:{
    getToken(){
      return this.$store.getters.getToken
    },
    getAuthStatus(){
      return this.$store.getters.getAuthStatus
    },
    getTgID(){
      return this.$store.getters.getTgID
    },
    getUsername(){
      return this.$store.getters.getUsername
    }
  },

  methods:{
    showDialog(operation){
      this.isShow = !this.isShow

      if (operation === 'Login'){
          this.isLogin = !this.isLogin
        }
      else if (operation === 'Registration'){
        this.isRegistration = !this.isRegistration
      }
    },

    hideDialog(){
      this.isShow = !this.isShow
      this.isLogin = false
      this.isRegistration = false
    },

    login(){
      const article = {
        "login": this.loginForCheck.inputLogin,
        "password": this.loginForCheck.inputPassword
      };

      axios.post('http://localhost:8081/api/login', article)
          .then(response => {
            this.$store.commit('changeToken', response.data.token)
            this.$store.commit('changeAuthStatus')
            axios.defaults.headers.common['Authorization'] = this.getToken
            this.getProfileData()
          }).catch(()=>alert('Неверный логин или пароль'))

    },

    register(){
      const article = {
        "login": this.loginForCheck.inputLogin,
        "password": this.loginForCheck.inputPassword
      };
         axios.post('http://localhost:8081/api/register', article).then().catch(()=>alert('Логин уже зарегистрирован'))
    },
    getProfileData(){
      axios
          .get('http://localhost:8081/api/profile')
          .then( response => {
            this.$store.commit('setUsername', response.data.login)
            this.$store.commit('setTgID', response.data.tg_id)
            // this.$store.commit('changeTasklist', Array.from(response.data.tasks));
            // this.$store.dispatch('refreshTasklist')
            // this.responseTasklist = this.$store.getters.getTasklist;this.responseTasklist = this.$store.getters.getTasklist;

          });
    },
    logout(){
      this.$store.commit('changeAuthStatus')
      this.$store.commit('changeToken', '')
      // this.$store.commit('changeTasklist', '')
      localStorage.clear()
    }
  },
  watch:{
    // isShow(){
    //   this.isShow = this.$store.state.isShow
    // }
  },
  mounted() {

  }
}

</script>

<style lang="scss">
.header{
  display: flex;
  align-items: center;
  margin: 0 0px 2px 0px;
  width: 100%;
  height: 50px;
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
    padding: .2em 1em;
    background-color: transparent;
    border: 1px solid lightskyblue;
    border-radius: .4em;
    color: white;
    margin-right: .5em;
    text-decoration: none;
    font-size: 18px;
    letter-spacing: 1px;
    font-weight: 700;
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
  letter-spacing: 1.5px;
}



</style>