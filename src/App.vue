<template>
  <div>
    
    <NavBar /><ComponentePrincipal />
    <Sidebar />
    
  </div>
</template>

<script>
import ComponentePrincipal from "./components/ComponentePrincipal.vue";
import Sidebar from "./components/Sidebar.vue";
import NavBar from "./components/NavBar.vue"
export default {
  name: "App",
  components: {
    ComponentePrincipal,
    Sidebar,
    NavBar
  },
};
</script>