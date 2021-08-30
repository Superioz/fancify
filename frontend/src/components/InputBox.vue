<template>
  <div class="input-box">
    <input
      v-model="content"
      class="input-field"
      placeholder="Insert content here"
    >
    <button type="submit">
      <i class="fa fa-user icon" />
    </button>
  </div>
</template>

<script>
/*
- Text should be cut at the end, no overflow or wrap
- should be bigger
- when in focus: small blue highlight underneath
- "enter logo" at the end of the line of the box
- preview text is "insert content"
*/

export default {
  name: "InputField",
  data: function() {
    return {
      content: ""
    };
  }
};
</script>

<style scoped>
.input-field-box {
  display: flex;
  justify-content: center;
}
</style>
