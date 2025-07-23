from cerberus import Validator

coffee_shop_schema={
    "shop_name": {"type": "string", "required": True, "empty": False},
    "location": {"type": "string", "required": False},
    "coffees_available": {
        "type": "list",
        "schema": {"type": "string"},
        "required": False
    },
    "rating": {
        "type": "float",
        "min": 1,
        "max": 5,
        "required": False
    }
}

coffee_Shop_validator= Validator(coffee_shop_schema)

