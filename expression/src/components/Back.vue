<template>
  <div>
    <div class="themeBg"></div>
  </div>
</template>

<script>
export default {
    name: 'Back',
}
</script>

<style scoped>
.themeBg {
  content: "";
  width: 100%;
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
  --color-filter: hue-rotate(25.4219deg);
  background-size: cover;
  /* background-image: linear-gradient(
      rgba(255, 255, 255, 0.2),
      rgba(255, 255, 255, 0.2)
    ),
    url("../img/homeback.png"); */
  background-image: linear-gradient(transparent, rgb(250, 250, 250) 85%),
    url("../img/homeback.png");

  z-index: -2;
}
</style>