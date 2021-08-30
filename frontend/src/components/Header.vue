<template>
  <div class="header bordered">
    <div class="header-logo">
      <img
        src="../assets/logo.png"
        alt="Fancify logo"
        width="200"
        height="200"
      >
    </div>
    <div class="header-text">
      <h1>
        Fancify
      </h1>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Kaushan+Script&display=swap');

.header {
  display: flex;

  /*
  Inside the flex container, align-items align it vertically and
  justify-content horizontally
  */
  align-items: center;
  justify-content: center;
}

.header-text {
  margin-left: 36px;

  font-family: Kaushan Script, Arial, Helvetica, sans-serif;
  font-size: 48px;
  color: #29B6F6;
  text-align: center;
}
</style>
