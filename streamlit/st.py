#--------In this project first  connecct mysql and python--------
import mysql.connector
import mysql.connector
#---To import images to mysql-----------
from PIL import Image
#--------- connecting mysql to python-------------
dbconnection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dinesh@9963",
    database="zepto_clone"
)
print(dbconnection)
print("dbconnection sucessfully")
curobj=dbconnection.cursor()

#------------- users table quarey in python --------------
curobj.execute("""
CREATE TABLE if not exists users(
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    lastname varchar(100),
    phone VARCHAR(15),
    password VARCHAR(100)
);
""")

#-------------- products table quarey in python ---------------
curobj.execute("""
CREATE TABLE if not exists products(
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price FLOAT,
    image VARCHAR(255)
);
""")
#--------------- cart table quarey in python --------------
curobj.execute("""
CREATE TABLE if not exists cart(
    cart_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    product_id INT,
    quantity INT
);
""")
#--------------- orders table quarey in python --------------
curobj.execute("""
CREATE TABLE if not exists orders(
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    total_amount FLOAT
);
""")
#--------------------instering products to the products table------------------------
cursor = dbconnection.cursor()
def products_exists(name):
    cur = dbconnection.cursor()
    cur.execute("SELECT * FROM products WHERE name=%s", (name,))
    result = cur.fetchone()
    cur.close()
    return result
cursor.execute("SELECT name FROM products")
existing_products = [row[0] for row in cursor.fetchall()]

if "Rice" not in existing_products:
 name = "Rice"
 price = 50
 image = "images/rice.jpg"
 query = "INSERT INTO products (name, price, image) VALUES(%s, %s, %s)"
 values = (name, price, image)
 cursor.execute(query, values)
 dbconnection.commit()
 cursor = dbconnection.cursor()

if "Apple" not in existing_products:
 name = "Apple"
 price = 100
 image = "images/apple.jpg"
 query = "INSERT INTO products (name, price, image) VALUES(%s, %s, %s)"
 values = (name, price, image)
 cursor.execute(query, values)
 dbconnection.commit()
 cursor = dbconnection.cursor()

if "Milk" not in existing_products:
 name = "Milk"
 price = 80
 image = "images/milk.jpg"
 query = "INSERT INTO products(name, price, image) VALUES(%s, %s, %s)"
 values = (name, price, image)
 cursor.execute(query, values)
 dbconnection.commit()
 cursor = dbconnection.cursor()

if "Black Grapes" not in existing_products:
 name = "Black Grapes"
 price = 70
 image = "images/Black Grapes.jpg"
 query = "INSERT INTO products(name, price, image) VALUES(%s, %s, %s)"
 values = (name, price, image)
 cursor.execute(query, values)
 dbconnection.commit()
 cursor = dbconnection.cursor()

if "Bread" not in existing_products:
 name = "Bread"
 price = 30
 image = "images/Bread.jpg"
 query = "INSERT INTO products(name, price, image) VALUES(%s, %s, %s)"
 values = (name, price, image)
 cursor.execute(query, values)
 dbconnection.commit()
 cursor = dbconnection.cursor()

if "custard apple" not in existing_products:
 name = "custard apple"
 price = 120
 image = "images/custard apple.jpg"
 query = "INSERT INTO products(name, price, image) VALUES(%s, %s, %s)"
 values = (name, price, image)
 cursor.execute(query, values)
 dbconnection.commit()
 cursor = dbconnection.cursor()

if "Green grapes" not in existing_products:
 name = "Green grapes"
 price = 120
 image = "images/Green grapes.jpg"
 query = "INSERT INTO products(name, price, image) VALUES(%s, %s, %s)"
 values = (name, price, image)
 cursor.execute(query, values)
 dbconnection.commit()

print("Product inserted successfully")

#cursor.execute("TRUNCATE TABLE Product ")
#dbconnection.commit()
#print("Table cleared and reset")

#=============  importing streamlit to python =================
import streamlit as st

# =================session state======================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_id" not in st.session_state:
    st.session_state.user_id = None

#------------------- Mini Zepto App interface--------------------------------------------------
st.title("Welcome to Mini Zepto App 🛒")
st.markdown("#### 🥗 Fresh Food, Good Health💚")
st.sidebar.markdown(" ## Hi 👋 please Login/Register  ↓ ")
choice = st.sidebar.selectbox("choose",("Login", "Register"))
#menu = ["Login", "Register"]
page = st.sidebar.radio("Menu", ["Products", "Cart"])


#--------------------------login creation code----------------------------------------
if choice == "Login":
   st.subheader ("Enter login details")
   phone = st.text_input("Phone")
   password = st.text_input("Password", type="password")
   login_button= st.button("Login")
   if login_button: 
        if phone == "" or password == "":
          st.error("⚠️ All fields are required!")
        else:
          cursor.execute(
               "SELECT * FROM users WHERE phone=%s AND password=%s",
          (phone, password)
          )
          users= cursor.fetchone()
          if users:
               st.session_state.logged_in = True   # ✅ LOGIN SUCCESS
               st.session_state.user_id = users[0]
               st.success("Login Successful")
               st.rerun()   # 🔥 GO TO NEXT PAGE
          else:
                st.error("Invalid Credentials")


#---------------------------- Register creation code -------------------------
elif  choice == "Register":
    st.subheader ("Enter Register details")
    name = st.text_input("Name")
    phone = st.text_input("Phone")
    password = st.text_input("Password", type="password")
    c_password = st.text_input("confirm password",type="password")
    register_button= st.button("Register")
    if register_button:
        if name == "" or phone == "" or password == "" or c_password == "":
            st.error("⚠️ All fields are required!")

        elif password != c_password:
            st.error("⚠️ Passwords do not match!")

        elif len(phone) != 10 or not phone.isdigit():
            st.error("⚠️ Enter valid 10-digit phone number!")
        else :  
            q=("INSERT INTO users(name,phone, password) VALUES (%s,%s,%s)")
            values = (name, phone, password)
            cursor.execute(q,values)
            dbconnection.commit()
            st.success("Registered Successfully")

# ---------------------------AFTER LOGIN IT SHOWS PRODUCTS PAGE CODE ----------------------
if st.session_state.logged_in:

    st.sidebar.success("You are logged in ✅")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_id = None
        st.rerun()

    st.title("🛒 Product Page - Mini Zepto")

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    for product in products:
        product_id = product[0]
        name = product[1]
        price = product[2]
        image = product[3]

        st.image(image, width=150)
        st.write(f"**{name}**")
        st.write(f"Price: ₹{price}")

        qty = st.number_input(f"Quantity for {name}", min_value=1, key=product_id)

        if st.button(f"Add to Cart - {name}", key=f"cart_{product_id}"):
            cursor.execute(
                "INSERT INTO cart(user_id, product_id, quantity) VALUES (%s, %s, %s)",
                (st.session_state.user_id, product_id, qty)
            )
            dbconnection.commit()
            st.success(f"{name} added to cart 🛒")
#--------------------------------PRODUCTS SELECT ONE ADD TO CART CODE -----------------------------
elif page == "Cart":
        st.title("🛒 Your Cart")

        cursor.execute("""
            SELECT c.cart_id, p.name, p.price, p.image, c.quantity
            FROM cart c
            JOIN products p ON c.product_id = p.product_id
            WHERE c.user_id = %s
        """, (st.session_state.user_id,))

        cart_items = cursor.fetchall()

        total = 0

        if not cart_items:
            st.warning("Your cart is empty 🛒")
        else:
            for item in cart_items:
                cart_id = item[0]
                name = item[1]
                price = item[2]
                image = item[3]
                qty = item[4]

                subtotal = price * qty
                total += subtotal

                st.image(image, width=120)
                st.write(f"**{name}**")
                st.write(f"Price: ₹{price}")
                st.write(f"Quantity: {qty}")
                st.write(f"Subtotal: ₹{subtotal}")

                if st.button(f"Remove {name}", key=f"del_{cart_id}"):
                    cursor.execute("DELETE FROM cart WHERE cart_id=%s", (cart_id,))
                    dbconnection.commit()
                    st.rerun()

                st.markdown("---")

            st.success(f"🧾 Total Amount: ₹{total}")
