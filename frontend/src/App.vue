<template>
  <div id="app">
    <Header />
    <InputBox />
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import InputBox from "./components/InputBox.vue";

export default {
  components: { Header, InputBox },
  mounted() {
    document.title = "Fancify";
  },
};
</script>

<style>
.bordered {
  border: 1px dotted red;
}
</style>
