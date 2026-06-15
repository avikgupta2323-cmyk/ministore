import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="MiniStore Support",
    page_icon="💬",
    layout="wide"
)

# --------------------------------------------------
# Product Knowledge Base
# --------------------------------------------------
products = {
    "headphones": {
        "name": "Wireless Bluetooth Headphones",
        "price": "$79.99",
        "description": "Noise cancellation and 30-hour battery life."
    },

    "watch": {
        "name": "Smart Fitness Watch",
        "price": "$129.99",
        "description": "Tracks heart rate, sleep, and workouts."
    },

    "chair": {
        "name": "Ergonomic Office Chair",
        "price": "$249.99",
        "description": "Comfortable chair with lumbar support."
    },

    "coffee": {
        "name": "Organic Coffee Beans",
        "price": "$18.99",
        "description": "Premium Arabica beans."
    },

    "shoes": {
        "name": "Running Shoes",
        "price": "$89.99",
        "description": "Lightweight athletic shoes."
    },

    "stand": {
        "name": "Portable Laptop Stand",
        "price": "$34.99",
        "description": "Adjustable aluminum laptop stand."
    }
}

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------
st.markdown("""
<style>

.chat-title {
    text-align: center;
    font-size: 2.5rem;
    font-weight: bold;
    margin-bottom: 10px;
}

.chat-subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown(
    '<div class="chat-title">💬 MiniStore Support Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="chat-subtitle">Ask questions about products, orders, refunds, delivery, and payments.</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# Session State for Chat History
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# Display Chat History
# --------------------------------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# Rule-Based Chatbot Logic
# --------------------------------------------------
def chatbot_response(user_input):

    text = user_input.lower()

    # ----------------------------------------------
    # Product Questions
    # ----------------------------------------------
    for key, product in products.items():

        if key in text:

            return f"""
### {product['name']}

💰 Price: {product['price']}

📝 Description:
{product['description']}
"""

    # ----------------------------------------------
    # Delivery Questions
    # ----------------------------------------------
    if "delivery" in text or "shipping" in text:
        return """
🚚 Standard delivery takes 3-5 business days.

⚡ Express delivery takes 1-2 business days.
"""

    # ----------------------------------------------
    # Refund Questions
    # ----------------------------------------------
    if "refund" in text:
        return """
💵 Refunds are processed within 5-7 business days
after approval.
"""

    # ----------------------------------------------
    # Return Questions
    # ----------------------------------------------
    if "return" in text:
        return """
📦 Products can be returned within 30 days
if unused and in original packaging.
"""

    # ----------------------------------------------
    # Payment Methods
    # ----------------------------------------------
    if "payment" in text or "pay" in text:
        return """
💳 We accept:

- Credit/Debit Cards
- UPI
- Net Banking
- PayPal
- Cash on Delivery
"""

    # ----------------------------------------------
    # Order Status
    # ----------------------------------------------
    if "order" in text or "status" in text:
        return """
📋 To check your order status:

1. Go to your profile
2. Open "My Orders"
3. Select your order
"""

    # ----------------------------------------------
    # Default Response
    # ----------------------------------------------
    return """
🤖 I'm here to help!

You can ask me about:

- Products
- Delivery
- Refunds
- Returns
- Payments
- Order Status
"""

# --------------------------------------------------
# Chat Input
# --------------------------------------------------
user_prompt = st.chat_input(
    "Ask something about MiniStore..."
)

if user_prompt:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_prompt
    })

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Generate bot response
    response = chatbot_response(user_prompt)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)