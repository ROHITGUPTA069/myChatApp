# First, you need to install the necessary libraries.
# Open your terminal or command prompt and run:
# pip install Flask google-generativeai

import os
from flask import Flask, request, jsonify
import google.generativeai as genai
from datetime import datetime

# Create a Flask web server application
app = Flask(__name__)

# --- API CONFIGURATION (INSECURE METHOD) ---
# WARNING: Storing your API key directly in the code is insecure and not recommended
# for production. Anyone with access to this code will have your key.
# It is strongly recommended to use environment variables instead.
try:
    # --- PUT YOUR API KEY HERE ---
    api_key = "api here"

    if api_key == "YOUR_API_KEY_HERE":
        raise ValueError("Please replace 'YOUR_API_KEY_HERE' with your actual Gemini API key.")

    genai.configure(api_key=api_key)
    # Initialize the Gemini model
    model = genai.GenerativeModel('gemini-1.5-flash')
    print("Gemini API configured successfully.")

except Exception as e:
    # If the API key isn't set, the app will still run but this endpoint will fail.
    print(f"CRITICAL ERROR: Failed to configure Gemini API: {e}")
    model = None


# --- API ENDPOINT FOR YOUR ANDROID APP ---
# This route now accepts POST requests at the '/ask' endpoint.
@app.route('/ask', methods=['POST'])
def ask_gemini():
    """
    Takes a prompt from the app's JSON request body, gets a response from Gemini,
    and returns the data as a new JSON object.
    """
    # Check if the Gemini model was initialized correctly
    if model is None:
        return jsonify({"error": "Gemini API not configured on the server."}), 500

    # --- 1. GET PROMPT FROM THE APP'S REQUEST BODY ---
    # Get the JSON data sent by your app
    data = request.get_json()

    # Check if the data is valid and contains a 'prompt' key
    if not data or 'prompt' not in data:
        return jsonify({"error": "Invalid request. JSON body must contain a 'prompt' key."}), 400

    user_prompt = data['prompt']
    print(f"Received prompt from app: '{user_prompt}'")

    try:
        # --- 2. CALL THE GEMINI API ---
        # Send the prompt to the Gemini model
        response = model.generate_content(user_prompt)

        # --- 3. RETURN GEMINI'S RESPONSE TO THE APP ---
        # Create a dictionary to hold the results
        result_data = {
            "status": "success",
            "prompt_sent": user_prompt,
            "location": "Balajan, Assam",
            "timestamp": datetime.now().isoformat(),
            "response_text": response.text
        }
        # Send the response back to your app in JSON format
        return jsonify(result_data)

    except Exception as e:
        # Handle potential errors from the Gemini API call
        print(f"An error occurred while calling Gemini API: {e}")
        return jsonify({"error": f"Failed to get response from Gemini. Details: {e}"}), 500


# --- RUN THE SERVER ---
if __name__ == '__main__':
    # The server will be accessible on your local network.
    # '0.0.0.0' makes it accessible from other devices on the same network.
    app.run(host='0.0.0.0', port=5000, debug=True)
