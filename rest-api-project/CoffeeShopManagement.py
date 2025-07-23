import json
import awsgi
from flask import Flask, jsonify, request
from DynamoDBConnector import DBConnection
import CoffeeSchemas
import logging

tableName= "CoffeeShops"

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger()

# Creating flask app
app= Flask(__name__)

# This function will return list if coffeeshop details from DynamoDB
@app.route('/get_coffeeshop', methods=['GET'])
def get_coffeeshop_list():

    try:
        table= DBConnection.db_Connector(tableName)

    except Exception as e:

        logger.error("Issue while connecting with DB", e)
        return jsonify({"error": "Issue while connecting with DB"}), 500

    shop_name= request.args.get('shop_name')

    if shop_name:
        try:
            logger.info(f"Searching {tableName} with {shop_name}")
            response= table.get_item(Key={"shop_name": shop_name})
            item= response.get('Item')

            if item:
                logger.debug(item)
                return jsonify(item)

            else:
                logger.error("Shop not found")
                return jsonify({"error": "Shop not found"}) ,404

        except Exception as e:
            logger.error("Error fetching shop", e)
            return jsonify({"error": "Error fetching shop", "details": str(e)}), 500

    try:
        response= table.scan()
        return jsonify(response.get("Items", []))

    except Exception as e:
        logger.error("Error scanning shops" , e)
        return jsonify({"error": "Error scanning shops", "details": str(e)}), 500


#This function will Add coffeeshop details in DynamoDB
@app.route('/add_coffeeshop', methods=['POST'])
def add_coffeeshop():

    data= request.get_json()
    logger.debug(data)

    if not CoffeeSchemas.coffee_Shop_validator.validate(data):
        logger.error(json.dumps({"error": CoffeeSchemas.coffee_Shop_validator.errors}))
        return jsonify({"error": CoffeeSchemas.coffee_Shop_validator.errors}), 400

    try:
        table= DBConnection.db_Connector(tableName)

    except Exception as e:
        logger.error("Issue while connecting with DB", e)
        return jsonify({"error": "Issue while connecting with DB"}), 500

    table.put_item(Item=data)

    logger.info("Coffee shop added successfully!")
    return jsonify({"message": "Coffee shop added successfully!", "data": data}), 201


#This function will Delete coffeeshop details in DynamoDB
@app.route('/delete_coffeeshop', methods=['DELETE'])
def delete_coffeeshop():
    shop_name= request.args.get("shop_name")

    if not shop_name:
        logger.error("Missing required parameter: shop_name")
        return jsonify({"error": "Missing required parameter: shop_name"}), 400

    try:
        table= DBConnection.db_Connector(tableName)
        response= table.delete_item(Key={"shop_name": shop_name})

        logger.info(f"Coffee shop '{shop_name}' deleted successfully")
        return jsonify({"message": f"'{shop_name}' deleted successfully from {tableName} "}), 200

    except Exception as e:
        logger.error("Error deleting item", e)
        return jsonify({"error": "Error deleting item", "details": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)

def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})



