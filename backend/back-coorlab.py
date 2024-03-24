from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/fetch')
def fetch():
    print("Abrindo arquivo data.json...")
    with open('../data.json') as file:
        data = json.load(file)
    print("Arquivo data.json aberto com sucesso.")

    transports = data['transport']
    cities = set()

    for transport in transports:
        city = transport['city']
        if city not in cities:
            cities.add(city)

    return jsonify(sorted((list(cities))))





@app.route('/viagens/<string:destino>')
def search_trip(destino):
    print("Abrindo arquivo data.json...")
    with open('../data.json') as file:
        data = json.load(file)
    transports = data['transport']

    filtered_transports = []
    
    for transport in transports:
        if transport['city'] == destino:
            filtered_transports.append(transport)

    comfort = max(filtered_transports, key=lambda x: float(x["price_confort"].replace("R$ ", "").replace(",", ".")))
    econ = min(filtered_transports, key=lambda x: float(x["price_econ"].replace("R$ ", "").replace(",", ".")))

    results = {
        "viagem_rapida": comfort, 
        "viagem_economica": econ
    }

    return jsonify(results)

if __name__ == '__main__':
    app.run(port=3000)
    