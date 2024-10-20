# from flask import Flask, render_template, request
# from data import get_openai_recommendations

# app = Flask(__name__)

# # Static list of products (add more if you like)
# static_products = [
#     "Plastic Bottle",
#     "Plastic Bag",
#     "Shampoo Bottle",
#     "Styrofoam Cup",
#     "Disposable Cutlery"
# ]

# @app.route("/", methods=["GET", "POST"])
# def index():
#     product_recommendations = {}

#     if request.method == "POST":
#         for product in static_products:
#             # Get recommendations for each product
#             recommendations = get_openai_recommendations(product)
#             product_recommendations[product] = recommendations
        
#         # Render the table with recommendations
#         return render_template("index.html", product_recommendations=product_recommendations)
    
#     return render_template("index.html", product_recommendations=None)

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import openai

# Replace with your OpenAI API key
openai.api_key = "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"

app = Flask(__name__)

# Static list of products
static_products = [
    "Plastic Straws",
    "Plastic Bags",
    "Plastic Bottles",
    "Shampoo Bottles",
    "Styrofoam Cups"
]

def get_openai_recommendations(product):
    prompt = f"Suggest eco-friendly alternatives for {product}. List just 3 each alternative in the strict format: Product Name (Company)."

    try:
        # Make a request to the OpenAI GPT-3.5 Turbo model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant who provides eco-friendly product alternatives."},
                {"role": "user", "content": prompt}
            ]
        )
        
        # Extract the alternatives from the response
        alternatives = response['choices'][0]['message']['content'].strip().split('\n')
        
        # Clean up the alternatives and ensure they follow the desired format
        formatted_alternatives = [alt.strip() for alt in alternatives if " (" in alt and ")" in alt]
        
        return formatted_alternatives
    except Exception as e:
        print(f"Error: {e}")
        return []

@app.route("/", methods=["GET", "POST"])
def index():
    product_recommendations = {}
    
    if request.method == "POST":
        for product in static_products:
            # Get recommendations for each product using the OpenAI API
            recommendations = get_openai_recommendations(product)
            product_recommendations[product] = recommendations
        
        return render_template("index.html", product_recommendations=product_recommendations)
    
    return render_template("index.html", product_recommendations=None)

@app.route("/update_recommendation", methods=["POST"])
def update_recommendation():
    # Get the edited product from the request
    product = request.json.get("product")
    # Fetch updated recommendations based on the new product name
    recommendations = get_openai_recommendations(product)
    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True)
