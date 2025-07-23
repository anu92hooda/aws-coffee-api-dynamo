# ☕ Coffee Shop Cloud API

This is a real-world cloud-based backend API project where I built everything from scratch — including **manual Lambda deployment**, **custom API Gateway routing**, and **DynamoDB integration**, all in native AWS.

---

### 🔧 Tech Stack
- Python (Flask)
- AWS Lambda
- API Gateway
- DynamoDB
- CloudWatch Logs
- Cerberus (for input validation)

---

### ✅ What This API Can Do

- `GET /get_coffeeshop` → Get details of one or all coffee shops  
- `POST /add_coffeeshop` → Add a new coffee shop  
- `DELETE /delete_coffeeshop` → Delete a shop by name  

---

### 📦 Sample Payload for POST

```json
{
  "shop_name": "Aroma1",
  "coffees_available": ["Espresso", "Latte", "Americano"],
  "location": "Toronto, ON",
  "rating": 3.9
}

### 🚀 Deployment Details (Manual AWS Setup)

This was done without using any frameworks like Serverless, SAM, or Zappa.

**Steps:**
- Created a virtual environment and installed dependencies  
- Bundled app code + dependencies into a zip file  
- Created a Lambda function and uploaded the zip  
- Set up API Gateway manually with Lambda Proxy Integration  
- Created the DynamoDB table and attached IAM role with proper permissions  
- Enabled CloudWatch logs to debug requests




