import openai

# Replace with your OpenAI API key
openai.api_key = "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"

def get_openai_recommendations(product):
    prompt = f"Suggest eco-friendly alternatives for {product}. List each alternative in the strict format: Product Name (Company)."

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
