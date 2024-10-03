import pickle
import streamlit as st

# Load the model
model1 = pickle.load(open("area.pkl", "rb"))

# Function to format the price in Indian Rupees
def format_inr(value):
    return f"₹{value:,.2f}"

def myf1():
    # Set the title and add a header with custom styling
    st.markdown("""
        <style>
        body {
            background-color: rgba(0, 0, 0, 0.5); /* Faded black background */
        }
        .main-title {
            font-size: 3em;
            color: #4CAF50;
            text-align: center;
            font-family: 'Arial', sans-serif;
        }
        .sub-title {
            font-size: 2em;
            color: #FFA500;
            text-align: center;
            font-family: 'Arial', sans-serif;
        }
        .instructions {
            font-size: 1.2em;
            color: #333;
            font-family: 'Arial', sans-serif;
        }
        .price {
            font-size: 1.5em;
            color: #007BFF;
            font-family: 'Arial', sans-serif;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<div class="main-title">AreaWise Housing Price Prediction</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Predict the price of houses based on the sqrft area</div>', unsafe_allow_html=True)
    st.markdown('<div class="instructions">Enter the area value to get the predicted price.</div>', unsafe_allow_html=True)
    
    # Add a slider for input
    area = st.slider("Enter the area value (in square feet):", 0, 100000, 5000)
    
    # Predict button
    pred = st.button("Predict")
    
    # Show the prediction when the button is clicked
    if pred:
        op = model1.predict([[area]])
        st.markdown(f'<div class="price">The predicted price of the area is: {format_inr(op[0])}</div>', unsafe_allow_html=True)

# Run the function
if __name__ == "__main__":
    myf1()
