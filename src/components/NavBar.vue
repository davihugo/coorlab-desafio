<template>
  <div class="navbar"></div>
</template>

<script>
export default {
  data() {
    return {
      destination: "",
      date: "",
      results: [],
    };
  },
};
</script>


<style >
.navbar {
  width: 84%;
  height: 100px;
  margin-left: 300px;
  background-color: #FFFFFF;
  position: fixed;
  left: 0;
  top: 0;
  z-index: 100;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 20px;
  /* SOMBREADO */
  box-shadow: 0px 0px 10px rgba(12, 12, 12, 0.5);
}
</style>
