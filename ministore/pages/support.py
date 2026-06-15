import streamlit as st
from openai import OpenAI

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="MiniStore Support",
    page_icon="💬",
    layout="wide"
)

# --------------------------------------------------
# OpenAI Client
# --------------------------------------------------
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# --------------------------------------------------
# Product Catalog
# --------------------------------------------------
PRODUCT_CATALOG = """
MiniStore Product Catalog:

1. Wireless Bluetooth Headphones
- Price: $79.99
- Category: Electronics
- Features:
  Active noise cancellation,
  30-hour battery life,
  premium sound quality.

2. Smart Fitness Watch
- Price: $129.99
- Category: Electronics
- Features:
  Heart rate tracking,
  sleep tracking,
  workout monitoring,
  smartphone notifications.

3. Ergonomic Office Chair
- Price: $249.99
- Category: Furniture
- Features:
  Mesh back,
  lumbar support,
  ergonomic comfort.

4. Organic Coffee Beans
- Price: $18.99
- Category: Groceries
- Features:
  Premium Arabica beans,
  sustainably sourced.

5. Running Shoes
- Price: $89.99
- Category: Fashion
- Features:
  Lightweight,
  comfortable,
  performance-focused.

6. Portable Laptop Stand
- Price: $34.99
- Category: Accessories
- Features:
  Adjustable aluminum stand,
  portable design.
"""

# --------------------------------------------------
# System Prompt
# --------------------------------------------------
SYSTEM_PROMPT = f"""
You are MiniStore Support Assistant,
a professional and friendly customer support representative.

Your job is to ONLY answer questions related to:
- products
- orders
- shipping
- delivery
- returns
- refunds
- payments
- customer support

You MUST politely refuse unrelated questions
and redirect the user back to MiniStore support topics.

Store Policies:
- Standard delivery: 3-5 business days
- Express delivery: 1-2 business days
- Returns accepted within 30 days
- Refunds processed within 5-7 business days
- Payment methods:
  Credit/Debit Cards,
  UPI,
  Net Banking,
  PayPal,
  Cash on Delivery

Here is the product catalog:

{PRODUCT_CATALOG}

Always be concise, professional,
and customer-friendly.
"""

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
    '<div class="chat-subtitle">Ask questions about products, delivery, refunds, returns, payments, and orders.</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# Initialize Chat History
# --------------------------------------------------
if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

# --------------------------------------------------
# Display Previous Messages
# --------------------------------------------------
for message in st.session_state.messages:

    # Skip system prompt display
    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# User Input
# --------------------------------------------------
user_input = st.chat_input(
    "Ask something about MiniStore..."
)

# --------------------------------------------------
# Handle User Message
# --------------------------------------------------
if user_input:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate assistant response
    with st.chat_message("assistant"):

        with st.spinner("Typing..."):

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=st.session_state.messages,
                temperature=0.5
            )

            assistant_reply = response.choices[0].message.content

            st.markdown(assistant_reply)

    # Store assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )