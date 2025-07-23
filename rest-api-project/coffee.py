from  flask import Flask, jsonify
from mangum import Mangum



data_coffee={"coffee" : [
           "Black" , "Mocha" , " DripCoffee"]

}

app= Flask(__name__)

@app.route('/coffee', methods=['GET'])

def get_coffee_list():
    return jsonify(data_coffee)

handler = Mangum(app)




