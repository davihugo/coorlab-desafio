 <template>
  <div class="container">
    <Navbar />
    <div class="rectangle">
      <div class="bar">
        <h4><b-icon-truck class="me-2" />Calculadora de Viagem</h4>
      </div>

      <b-card class="mt-4 p-4 custom-card" style="background-color: #f0f0f0">
        <h5><b-icon-cart-plus-fill /> Calcule o Valor da Viagem</h5>
        <form @submit.prevent="onSubmit" class="form">
          <div class="form-group">
            <label for="destination">Destino</label>
            <input
              type="text"
              id="destination"
              v-model="destination"
              placeholder="Insira o destino"
            />
          </div>

          <div class="form-group">
            <label for="date">Data</label>
            <input
              type="date"
              id="date"
              v-model="date"
              placeholder="Selecione uma data"
            />
          </div>

          <div class="form-group button">
            <button type="submit">Buscar</button>
          </div>
        </form>
      </b-card>
    </div>
    <div v-if="results.length > 0">
      <h2>Resultados</h2>
      <ul>
        <li v-for="result in results" :key="result.id">
          <p>{{ result.city }}</p>
          <p>{{ result.duration }}</p>
          <p>{{ result.price_confort }}</p>
          <p>{{ result.price_econ }}</p>
        </li>
      </ul>
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
      results: [],
    };
  },
  methods: {
    onSubmit() {
      axios
        .post("http://localhost:5000/viagens/buscar", {
          params: {
            destination: this.destination,
            date: this.date,
          },
        })
        .then((response) => {
          console.log(response.data);
          this.results = response.data.transport;
        })
        .catch((error) => {
          console.error("Erro ao buscar viagens:", error);
        });
    },
  },
};
</script>

<style>
.container {
  max-width: 800px;
  margin: 0 auto;
}

.rectangle {
  width: 1500px;
  height: 700px;
  margin: 20px auto;
  background-color: #fff;
  border: 1px solid #ccc;
  padding: 20px;
  margin-left: 50px;
  border-radius: 20px;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.bar {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 50px;
  background-color: #183348;
  border-radius: 15px 15px 0px 0px;
  display: flex;
  align-items: center;
}

.bar h4 {
  margin: 30px;
  padding: 0 20px;
  font-size: 1.5em;
  color: #fff;
}

.custom-card {
  width: 500px;
  margin-right: auto;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  min-height: 500px;
}

h1 {
  text-align: center;
}

form {
  margin-top: 40px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.form-group {
  margin-bottom: 10px;
  margin-left: 0;
}

label {
  margin-left: 0;
  margin-bottom: 10px;
  font-weight: bold;
  /* padding: 5px 10px; */
}

input {
  padding: 5px;
  border: 1px solid #ccc;
  display: flex;
  flex-direction: column;
  border-left: 8px solid #ccc;
}

button {
  width: 300px;
  padding: 5px 10px;
  border: 1px solid #ccc;
  background-color: #000;
  color: #fff;
  margin: 20px 50px;
}
.button {
  display: flex;
  justify-content: center;
  align-self: center;
  margin: 20px 55px;
}

.button-container {
  margin-bottom: 10000px;
}

.rectangle h5 {
  margin-top: 50px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 10px;
}
</style>