<template>
  <div class="task-list-container">
    <div class="task-item"
         v-for="task in taskList"
         v-bind:key="task">
      <input type="checkbox"> {{task.title}}
    </div>

  </div>
</template>

<script>
export default {

  data(){

  },
  props: {
    taskList:{
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>

</style>