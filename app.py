from flask import Flask, request, render_template
import geopy

import os
import csv

import geopy.distance

app = Flask(__name__)

csv_file = 'distances.csv'

@app.route('/')
def home():
    return render_template(r'interface.html')

@app.route('/result', methods=['POST'])
def calcular():
    end1 = request.form['endereco1']
    end2 = request.form['endereco2']
    
    def calculo_enderecos(endereco1, endereco2):
        
        # Calcula a distancia entre os endereços
        loc = geopy.Nominatim(user_agent="distance_calculator")
        
        loc1 = loc.geocode(endereco1, timeout=100)
        loc1_lat = loc1.latitude
        loc1_long = loc1.longitude
        
        loc2 = loc.geocode(endereco2, timeout=100)
        loc2_lat = loc2.latitude
        loc2_long = loc2.longitude
        
        dist = send_lat_long(loc1_lat, loc1_long, loc2_lat, loc2_long)
        
        return dist
            
    def send_lat_long(loc1_lat, loc1_long, loc2_lat, loc2_long):
        
        distancia = geopy.distance.geodesic((loc1_lat, loc1_long), (loc2_lat, loc2_long)).km
        
        distancia = round(distancia, 2)
        
        # Save CSV
        salva_csv(distancia)
        
        return distancia
        #print(f"A distância entre {self.endereco1} e {self.endereco2} é de {distancia:.2f} km.")
    
        
    def salva_csv(dist):
        # Salva as informações no CSV
        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([end1, end2, dist])
        
        return True
    
    try:
        dist = calculo_enderecos(end1, end2)
        #dist = "teste"
        result = f"The distance between {end1} and {end2} is of {dist} km."
        
    except Exception as e:
        print(e)
        result = "Something went wrong - ERROR."
        
    print(result)
    
    return render_template('result.html', result=result)

@app.route('/distances')
def distancias():
    distances = []
    try:
        with open('distances.csv', mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                distances.append(row)
    except FileNotFoundError:
        distances = []
    return render_template('distances.html', distances=distances)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
