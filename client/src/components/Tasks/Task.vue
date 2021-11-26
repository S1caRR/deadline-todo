<template>
  <div class="task-item">
    <input type="checkbox"> {{taskTitle}}

  </div>
</template>

<script>
export default {
  name: "TaskItem",

  props: {
    taskTitle: {
      type: String,
    }
  },


}
</script>

<style scoped>

</style>