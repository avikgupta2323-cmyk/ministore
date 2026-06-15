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
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 1.2rem;
        opacity: 0.9;
    }

    .section-title {
        font-size: 1.8rem;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 15px;
        color: #1e293b;
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
        font-weight: 700;
        color: #111827;
    }

    .product-category {
        color: #64748b;
        font-size: 0.85rem;
        margin-bottom: 10px;
    }

    .product-price {
        color: #16a34a;
        font-size: 1.3rem;
        font-weight: bold;
        margin-top: 10px;
    }

    .footer {
        text-align: center;
        color: gray;
        margin-top: 40px;
        padding: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Sample Product Data
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
# Sidebar - Categories & Cart Summary
# --------------------------------------------------
st.sidebar.title("🛍️ MiniStore")

categories = ["All"] + sorted(list(set([p["category"] for p in products])))

selected_category = st.sidebar.selectbox(
    "Browse Categories",
    categories
)

st.sidebar.markdown("---")
st.sidebar.subheader("🛒 Shopping Cart")

# Demo cart summary
cart_items = 3
cart_total = 228.97

st.sidebar.metric("Items in Cart", cart_items)
st.sidebar.metric("Cart Total", f"${cart_total:.2f}")

st.sidebar.markdown("---")
st.sidebar.info("Demo Store Interface\n\nNo checkout functionality included.")

# --------------------------------------------------
# Homepage Hero Section
# --------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🛍️ MiniStore</h1>
    <p>Your One-Stop Destination for Quality Products at Great Prices</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Welcome Section
# --------------------------------------------------
st.markdown('<div class="section-title">Welcome to MiniStore</div>', unsafe_allow_html=True)

st.write(
    """
    Discover premium products across electronics, fashion, furniture,
    groceries, and accessories. Browse our featured collection and
    find products that fit your lifestyle.
    """
)

# --------------------------------------------------
# Filter Products by Category
# --------------------------------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

# --------------------------------------------------
# Featured Products Section
# --------------------------------------------------
st.markdown(
    '<div class="section-title">Featured Products</div>',
    unsafe_allow_html=True
)

# Responsive product grid using Streamlit columns
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
                    <div class="product-price">${product['price']:.2f}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Demo button
            st.button(
                f"Add to Cart",
                key=product["name"]
            )

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("""
<div class="footer">
    © 2026 MiniStore • Modern E-Commerce Demo Built with Streamlit
</div>
""", unsafe_allow_html=True)