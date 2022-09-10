from flask import Flask,request,jsonify
import utill
app = Flask(__name__)

@app.route("/get_vehical_names")
def get_vehical_name():
    response1 = jsonify({
           'vehical': utill.get_vehical_names()
    })
    response1.headers.add('Access-control-Allow-Origin', '*')
    return response1

@app.route("/get_fuel_type")
def get_fuel_type():
    response2 = jsonify({
           'fuel': utill.get_fuel_type()
    })
    response2.headers.add('Access-control-Allow-Origin', '*')
    return response2

@app.route("/get_seller_type")
def get_seller_type():
    response3 = jsonify({
           'seller': utill.get_seller_type()
    })
    response3.headers.add('Access-control-Allow-Origin', '*')
    return response3

@app.route("/get_transmission_type")
def get_transmission_type():
    response4 = jsonify({
           'transmission': utill.get_transmission_type()
    })
    response4.headers.add('Access-control-Allow-Origin', '*')
    return response4

@app.route("/get_owner_type")
def get_owner_type():
    response5 = jsonify({
           'owner': utill.get_owner_type()
    })
    response5.headers.add('Access-control-Allow-Origin', '*')
    return response5

@app.route('/used_car_price',methods=['GET','POST'])
def used_car_price():
    name = request.form['name']
    year = request.form['year']
    km_driven = float(request.form["km_driven"])
    fuel = request.form['fuel']
    seller_type = request.form['seller_type']
    transmission = request.form['transmission']
    owner = request.form['owner']
    mileage = float(request.form['mileage'])
    engine = request.form['engine']
    seats = request.form['seats']

    response6 = jsonify({
           'estimated_price':utill.get_estimated_price(name,year,km_driven,fuel,seller_type,transmission,owner,mileage,engine,seats)
    })

    return response6



if __name__ == "__main__":
    print("Starting python flask server for car price predictions..")
    app.run()
