import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# --------------------------------------------------
# Product Database
# --------------------------------------------------
products = [
    {
        "name": "Wireless Bluetooth Headphones",
        "price": 79.99,
        "category": "Electronics",
        "description": "Premium sound quality with active noise cancellation and 30-hour battery life."
    },
    {
        "name": "Smart Fitness Watch",
        "price": 129.99,
        "category": "Electronics",
        "description": "Track heart rate, sleep, workouts, and receive smartphone notifications."
    },
    {
        "name": "Ergonomic Office Chair",
        "price": 249.99,
        "category": "Furniture",
        "description": "Comfortable mesh chair with lumbar support for long work sessions."
    },
    {
        "name": "Organic Coffee Beans",
        "price": 18.99,
        "category": "Groceries",
        "description": "Freshly roasted premium Arabica beans sourced from sustainable farms."
    },
    {
        "name": "Running Shoes",
        "price": 89.99,
        "category": "Fashion",
        "description": "Lightweight athletic shoes designed for comfort and performance."
    },
    {
        "name": "Portable Laptop Stand",
        "price": 34.99,
        "category": "Accessories",
        "description": "Adjustable aluminum stand compatible with most laptops and tablets."
    }
]

# --------------------------------------------------
# Custom CSS Styling
# --------------------------------------------------
st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.hero {
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    padding: 40px;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 3rem;
}

.section-title {
    font-size: 1.8rem;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 15px;
}

.product-card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.08);
    border: 1px solid #e2e8f0;
    height: 320px;
    margin-bottom: 20px;
}

.product-title {
    font-size: 1.2rem;
    font-weight: bold;
}

.product-category {
    color: gray;
    font-size: 0.9rem;
}

.product-price {
    color: green;
    font-size: 1.3rem;
    font-weight: bold;
    margin-top: 10px;
}

/* Floating Support Button */
.support-button {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background-color: #2563eb;
    color: white;
    padding: 15px 22px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
    z-index: 999;
}

.support-button:hover {
    background-color: #1d4ed8;
}

.footer {
    text-align: center;
    margin-top: 40px;
    color: gray;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.title("🛍️ MiniStore")

categories = ["All"] + sorted(list(set([p["category"] for p in products])))

selected_category = st.sidebar.selectbox(
    "Browse Categories",
    categories
)

st.sidebar.markdown("---")

st.sidebar.subheader("🛒 Shopping Cart")

st.sidebar.metric("Items in Cart", 3)
st.sidebar.metric("Cart Total", "$228.97")

# --------------------------------------------------
# Hero Section
# --------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🛍️ MiniStore</h1>
    <p>Your One-Stop Destination for Quality Products</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Welcome Section
# --------------------------------------------------
st.markdown(
    '<div class="section-title">Welcome to MiniStore</div>',
    unsafe_allow_html=True
)

st.write("""
Discover premium products across electronics, fashion,
furniture, groceries, and accessories.
""")

# --------------------------------------------------
# Filter Products
# --------------------------------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

# --------------------------------------------------
# Featured Products
# --------------------------------------------------
st.markdown(
    '<div class="section-title">Featured Products</div>',
    unsafe_allow_html=True
)

for i in range(0, len(filtered_products), 3):

    cols = st.columns(3)

    for col, product in zip(cols, filtered_products[i:i+3]):

        with col:

            st.markdown(
                f"""
                <div class="product-card">
                    <div class="product-title">{product['name']}</div>
                    <div class="product-category">{product['category']}</div>

                    <p>{product['description']}</p>

                    <div class="product-price">
                        ${product['price']:.2f}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.button(
                "Add to Cart",
                key=product["name"]
            )

# --------------------------------------------------
# Floating Support Button
# --------------------------------------------------
st.markdown("""
<a href="/Support_Chatbot" target="_self" class="support-button">
💬 Support
</a>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("""
<div class="footer">
© 2026 MiniStore • Built with Streamlit
</div>
""", unsafe_allow_html=True)