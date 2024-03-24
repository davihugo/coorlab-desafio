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
  data() {
    return {
      isSidebarOpen: false
    };
  },
  methods: {
    toggleSidebar() {
      this.isSidebarOpen = !this.isSidebarOpen;
    }
  }
};
</script>
<style>

/* responsividade */

.sidebar-open {
  width: 200px; 
  transition: width 0.3s ease; 
}

.sidebar-closed {
  width: 50px;
  transition: width 0.3s ease; 
}

/* FIM responsividade */


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

/* responsividade */


@media (max-width: 1400px) {
  .sidebar {
    width: 100%; 
    position: fixed; 
    left: 0;
    top: 0; 
    transform: translateX(-100%); 
    transition: transform 0.3s ease-in-out; 
  }

  .sidebar.open { 
    transform: translateX(0); 
  }
}
</style>