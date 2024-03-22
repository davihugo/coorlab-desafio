import App from './App.vue'
import Vue from 'vue'
import axios from 'axios';


import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)

Vue.use(IconsPlugin)

Vue.prototype.$http = axios;

// Adicionar interceptor para configurar CORS
axios.interceptors.request.use(config => {
    config.headers['Access-Control-Allow-Origin'] = '*'; // Ou você pode especificar a origem permitida
    return config;
});

new Vue ({
  el: '#app' ,
  render : h => h(App)
});