<template>
  <div class="content-header">
    <div class="content-header-block">
      <h2>Профиль</h2>
    </div>
  </div>
  <div class="profile-container">
    <span>{{username}}</span>
      <div class="">
        <span class="tg-description">Вы можете указать свой telegram ID и наш бот будет высылать вам список тасков на день каждое утро.</span>
        <p>
          Your Telegram ID is: <input v-model="tgID" type="text">
          <button @click="changeTgID">Change TG ID</button> </p>
        <span class="change-password">Сменить пароль:</span>
        <p>
          <input v-model="oldPassword" type="text" placeholder="Старый пароль">
          <input v-model="newPassword" type="text" placeholder="Новый пароль">
          <button @click="changePassword">Сменить пароль</button>
        </p>
      </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Profile",
  components: {  },
  data(){
    return{
      tgID: '',
      oldPassword: '',
      newPassword: ''
    }
  },
  computed:{
    getTgID(){
      return this.$store.getters.getTgID
    },
  },
  methods:{
    changeTgID(){
      axios.patch(`http://localhost:8081/api/profile`, {tg_id: this.tgID})
          .then(() => {
            this.$store.commit('setTgID', this.tgID)
          });
    },
    changePassword(){
      axios.patch(`http://localhost:8081/api/profile/reset_password`,
          {old_password: this.oldPassword,
                new_password: this.newPassword})
          .then(() => {
            alert('Пароль успешно изменён')
          })
          .catch(()=>alert('Неверный старый пароль'));
    }
  },
  mounted() {
    this.$store.dispatch('refreshToken')
    this.tgID = this.getTgID
  },
  watch:{
    getTgID(){
      this.tgID = this.getTgID
    }
  }

}
</script>

<style scoped lang="scss">
.content-header {
  width: 95%;
  margin: 0 auto;
  display: block;
  align-items: center;
  border-bottom: 2px solid cadetblue;

}
.content-header-block {
  display: block;
  width: 100%;
  margin-top: 10px;
  margin-bottom: 20px;
  text-align: center;
}
.profile-container{
  font-size: 1.5em;
  margin: 1em;
}
.tg-description{
  font-size: .7em;
}
p{
  border-bottom: 1px solid black;
  margin-bottom: 10px;
  padding-bottom: 10px;
  backdrop-filter: revert;
}
</style>