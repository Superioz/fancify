<template>
  <div id="app">
    <Header />
  </div>
</template>

<script>
import Header from "./components/Header.vue";

export default {
  components: { Header },
  mounted() {
    document.title = "Fancify";
  },
};
</script>
