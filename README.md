![123shots_so](https://github.com/user-attachments/assets/9ac30d62-0b34-4a3f-b2f5-cf2d07c5f941)

# Eco-Friendly Product Recommendations App

## Overview

This web application provides users with eco-friendly alternatives for common products. Users can edit product names, retrieve recommendations in real-time, and interact with an intuitive interface. The application uses OpenAI's GPT-3.5 Turbo model to generate suggestions.

## Features

- **Real-time Recommendations**: Users can edit product names and receive updated eco-friendly alternatives immediately.
- **Interactive Checkboxes**: Each product has an associated checkbox that, when clicked, activates the update function and temporarily changes its state to indicate processing.
- **User-Friendly Interface**: The application is built using Flask and renders a clean HTML interface for easy navigation.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript, Chart.js
- **Backend**: Python, Flask
- **API**: OpenAI GPT-3.5 Turbo for generating recommendations

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- OpenAI API key

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Boweii22/Fintech-Hackathon.git
   cd eco-friendly-recommendations
   ```

2. **Install Dependencies**:

   ```bash
   pip install flask openai
   ```

3. **Set Up Your OpenAI API Key**:

   Open `app.py` and replace the placeholder with your actual OpenAI API key:

   ```python
   openai.api_key = "YOUR_API_KEY_HERE"
   ```

4. **Run the Application**:

   ```bash
   python app.py
   ```

5. **Access the App**:

   Open your browser and go to `http://127.0.0.1:5000/`.

## Usage

- Edit the product names in the table to get eco-friendly alternatives.
- Click the checkbox next to each product to fetch updated recommendations.
- Click the "Get Recommendations for All Products" button to retrieve suggestions for all products at once.
