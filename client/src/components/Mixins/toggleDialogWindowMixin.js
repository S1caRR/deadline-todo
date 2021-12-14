export default {
    props:{
      isShow:{
          type: Boolean,
          default: false
      }
    },
    methods:{
        hideDialog(){
            this.$emit('hideDialog')
        }
    },
}