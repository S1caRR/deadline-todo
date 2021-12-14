<template>
  <div class="menu" style="display: inline">
    <span class="header-username-title">{{getUsername}}</span>
<!--    <ul>-->
<!--      <li>Пирожное</li>-->
<!--      <li>Пончик</li>-->
<!--      <li>Мёд</li>-->
<!--    </ul>-->
  </div>
</template>

<script>
export default {
  name: "HeaderProfile",
  props: {
    username: {},
    tgID: {}
  }
}
</script>

<style scoped>

</style>