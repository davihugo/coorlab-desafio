<template>
  <div class="sidebar">
    <img src="@/assets/logo.png" alt="Logo" />
    <div class="calculator">
      
      <p>CALCULADORA DE VIAGENS</p>
      <b-icon icon="calculator-fill"></b-icon>
    </div>
  </div>
</template>

<script>
import { BIcon } from "bootstrap-vue"; 
export default {
  name: "SidebarComponent",
  components: {
    BIcon,
  },
  props: {},
  data() {
    return {
      // ...
    };
  },
  computed: {
    // ...
  },
  watch: {
    // ...
  },
  methods: {
    // ...
  },
  mounted() {
    // ...
  },
};
</script>
<style>
.sidebar {
  width: 300px;
  height: 100%;
  background-color: #183348;
  position: fixed;
  left: 0;
  top: 0;
  z-index: 100;
  color: white;
  display: flex;
  flex-direction: column;
  padding-top: 20px;
}

.sidebar img {
  width: 250px;
  height: 40px;
  margin: 10px auto;
}

.calculator {
  display: flex;
  align-items: center;
  justify-content: flex-start; 
  margin-left: 20px; 
}

.calculator p {
  margin-right: 10px; 
  margin-top: 19px;
}

.calculator .b-icon {
  font-size:17px;
}
</style>