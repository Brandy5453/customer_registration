import streamlit as st 
# import mysql.connector


id = int(st.number_input("Enter your customer ID", format="%d"))
firstname = st.text_input("Enter your firstname")
lastname = st.text_input("Enter your lastname")
email = st.text_input("Enter your emial")
gender = st.selectbox("Gender", ["Select", "Male", "Female"])


# conn = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     port = "3307",
#     password = "simon@123",
#     database = "customer_registration"
# )

# cursor = conn.cursor()

# # st.button("Register")

# if st.button("Register"):
#     sql = "INSERT INTO customer_table(customer_id, first_name, last_name, email, gender) VALUES (%s, %s, %s, %s, %s)"
#     values = (id, firstname, lastname, email, gender)
#     cursor.execute(sql, values)
#     conn.commit()
#     st.success("Customer has succesfully regsitered")

# else:
#     print("check your entry")

# cursor.close()
# conn.close()


