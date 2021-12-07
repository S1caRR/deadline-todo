<template>
  <div class="dialog" v-if="isShow" @mousedown.prevent="hideDialog" >
    <div class="dialog-content" @mousedown.stop>
      <slot></slot>
    </div>
  </div>
  <div v-else>

  </div>
</template>

<script>
export default {
  name: "DialogWindow",
  props:{
    isShow:{
      type: Boolean,
      default: false
    },
  },
  methods:{
    hideDialog() {
      this.$emit('hideDialog')
    }
  }
}
</script>

<style lang="scss">

.dialog{
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, 0.5);
  position: fixed;
  display: flex;
  z-index: 1;
}

.dialog-content{
  margin: auto;
  background: white;
  border-radius: 12px;
  padding: 20px;
}
.dialog-window {
  .dialog-window-button {
    text-align: end;
    margin: .5em .3em;
  }

  a {

    padding: .2em 1em;
    background-color: transparent;
    border: 1px solid lightskyblue;
    border-radius: .4em;
    color: Black;
    //margin-right: .5em;

    text-decoration: none;
    font-size: 22px;

  }

  a:hover {
    background: rgba(173, 216, 230, 0.3);
  }

  .content-input-tasks {
    display: block;

  }

  input {
    margin: 5px;
    height: 40px;
    padding: 1px 10px;
    border-radius: 5px;
  }

  input[type="text"] {
    font-size: 20px;
  }

  h1 {
    margin: auto;
    text-align: center;
  }
}
</style>