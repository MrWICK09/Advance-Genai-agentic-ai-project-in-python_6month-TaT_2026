import streamlit as st

st.set_page_config(page_title="Amazon Clone", layout="wide")

# 🔥 Custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;
    }
    .navbar {
        background-color: #131921;
        padding: 15px;
        color: white;
        font-size: 22px;
        font-weight: bold;
        border-radius: 5px;
    }
    .product-card {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 12px;
        text-align: center;
        background-color: white;
        transition: 0.3s;
    }
    .product-card:hover {
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
        transform: scale(1.02);
    }
    .price {
        color: green;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 🔹 Navbar
st.markdown('<div class="navbar">🛒 Amazon Clone</div>', unsafe_allow_html=True)

# 🔹 Search bar
search = st.text_input("🔍 Search for products...")

# 🔥 Product Data (working images)
products = [
    {
        "name": "iPhone 15",
        "price": "$999",
        "img": "https://picsum.photos/id/101/300/200",
    },
    {
        "name": "Gaming Laptop",
        "price": "$1200",
        "img": "https://picsum.photos/id/180/300/200",
    },
    {
        "name": "Headphones",
        "price": "$199",
        "img": "https://picsum.photos/id/29/300/200",
    },
    {
        "name": "Running Shoes",
        "price": "$89",
        "img": "https://picsum.photos/id/21/300/200",
    },
    {
        "name": "Smart Watch",
        "price": "$250",
        "img": "https://picsum.photos/id/1062/300/200",
    },
    {"name": "Camera", "price": "$799", "img": "https://picsum.photos/id/250/300/200"},
]

# 🔹 Search filter
if search:
    products = [p for p in products if search.lower() in p["name"].lower()]

# 🔹 Cart (simple)
if "cart" not in st.session_state:
    st.session_state.cart = []

# 🔹 Layout
cols = st.columns(3)

for i, product in enumerate(products):
    with cols[i % 3]:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)

        st.image(product["img"], use_container_width=True)
        st.subheader(product["name"])
        st.markdown(
            f'<div class="price">{product["price"]}</div>', unsafe_allow_html=True
        )

        if st.button("Add to Cart", key=i):
            st.session_state.cart.append(product["name"])

        st.markdown("</div>", unsafe_allow_html=True)

# 🔥 Cart display
st.sidebar.title("🛒 Cart")

if st.session_state.cart:
    for item in st.session_state.cart:
        st.sidebar.write(f"✔️ {item}")
else:
    st.sidebar.write("Cart is empty")
