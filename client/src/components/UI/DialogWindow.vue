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
      required: true,
      default: false
    },
    isLogin: {},
    isRegistration: {},
  },
  methods:{
    hideDialog() {
      if (this.isLogin){
        this.$emit('showDialog', 'Login')
      }
      else if (this.isRegistration) {
        this.$emit('showDialog', 'Registration')
      }
      else {
        this.$emit('showDialog')
      }

    }
  }
}
</script>

<style scoped>

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


</style>