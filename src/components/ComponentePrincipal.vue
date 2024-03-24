<template>
  <div class="container">
    <Navbar />
    <div class="rectangle">
      <div class="bar">
        <h4><b-icon-truck class="me-2" />Calculadora de Viagem</h4>
      </div>

      <b-card class="mt-4 p-4 custom-card" style="background-color: #f0f0f0">
        <h5><b-icon-cart-plus-fill /> Calcule o Valor da Viagem</h5>
        <form @submit.prevent="buscarViagens" class="form flex-item">
          <div class="form-group">
            <label for="destination">Destino</label>
            <select v-model="destination" id="destination" class="form-control">
              <option v-for="city in cities" :key="city" :value="city">{{ city }}</option>
            </select>

          </div>

          <div class="form-group">
            <label for="date">Data</label>
            <input type="date" id="date" v-model="date" placeholder="Selecione uma data" />
          </div>

          <div class="form-group button">
            <button type="submit">Buscar</button>
          </div>
        </form>
      </b-card>

      <!-- Flashcard de Resultados -->
      <b-card v-if="results" class="mt-4 p-4 custom-card result-card  flex-container" style="background-color: #f0f0f0">
        <h4>Estas são as melhores alternativas de </h4>
        <h4> viagem para a data selecionada : </h4>
        <div class="flashcard">
        <div class="result-card">
          <div class="details">
            <p>{{ results.viagem_rapida.name }}</p>
            <p>Assento: {{ results.viagem_rapida.bed }}</p>
            <p>Tempo estimado: {{ results.viagem_rapida.duration }}</p>
          </div>
          <div class="value">
            <h5>VALOR</h5>
            <p>{{ results.viagem_rapida.price_confort }}</p>
          </div>
        </div>
        <div class="result-card">
          <div class="details">
            <p>{{ results.viagem_economica.name }}</p>
            <p>Assento: {{ results.viagem_economica.seat }}</p>
            <p>Tempo estimado: {{ results.viagem_economica.duration }}</p>
          </div>
          <div class="value">
            <h5>VALOR</h5>
            <p>{{ results.viagem_economica.price_econ }}</p>
          </div>
        </div>
      </div>
      </b-card>
    </div>
  </div>
</template>

<script>
import { BIconTruck, BCard, BIconCartPlusFill } from "bootstrap-vue";
import axios from "axios";

export default {
  components: {
    BIconTruck,
    BCard,
    BIconCartPlusFill,
  },
  data() {
    return {
      destination: "",
      date: "",
      results: null,
      cities: [],
      transportadoras: [],
    };
  },
  mounted() {
    this.fetchCities(); 
  },
  methods: {
    async fetchCities() {
      try {
        const response = await axios.get("http://localhost:3000/fetch");
        this.cities = response.data;
      } catch (error) {
        console.error("Erro ao buscar cidades:", error);
      }
    },
    async buscarViagens() {
      if (!this.destination || !this.date) {
        alert("Por favor, preencha todos os campos.");
        return;
      }

      try {
        const response = await axios.get(`http://localhost:3000/viagens/${this.destination}`);
        this.results = response.data;
      } catch (error) {
        console.error("Erro ao buscar viagens:", error);
      }
    },
  },
};
</script>


<style scoped>
.valor-container {
  display: flex;
  justify-content: center;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.rectangle {
  width: 90%;
  max-width: 800px;
  height: auto;
  margin: 20px auto;
  background-color: #fff;
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 20px;
  position: relative;
}

.bar {
  width: 100%;
  height: 50px;
  background-color: #183348;
  border-radius: 15px 15px 0 0;
  display: flex;
  align-items: center;
}

.bar h4 {
  margin: 0;
  padding: 0 20px;
  font-size: 1.5em;
  color: #fff;
}

.flashcard {
  display: flex;
}

.result-card {
  display: flex;
  /*flex-direction: column;*/
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px; 

  padding: 10px;
  border: 1px solid #183348;
  border-radius: 10px;
  background-color: #fff;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1);
  margin-right: 10px;
}
.details,
.value {
  text-align: center;
  margin-right: 30px;

}
.value {
  background-color: #183348;
  border-radius: 12px;

}

.value h5 {
  margin-bottom: 5px; 
  color: #ccc;
  padding: 2em 1em 0 1em;
}

.value p {
  color: #ccc;
  padding : 0 0 2em 0 ;

}

.result-card:last-child {
  margin-right: 0;
}
.result-card h5 {
  margin-top: auto;
  margin-bottom: auto;
}

.result-card h6 {
  margin: 0;
}

.result-card.price {
  background-color: #af9b9b;
}

.custom-card {
  width: 100%;
}

h5 {
  margin-top: 20px;
}

form {
  margin-top: 20px;
}

.form-group {
  margin-bottom: 10px;
}

label {
  margin-bottom: 5px;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
}

button {
  width: 100%;
  padding: 8px 0;
  border: 1px solid #ccc;
  background-color: #000;
  color: #fff;
  margin-top: 20px;
}
</style>