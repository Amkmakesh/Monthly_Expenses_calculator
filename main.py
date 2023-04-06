import streamlit as st
from Back_End import table_crete
import sqlite3


st.title("Monthly Expense Calculator")

table_crete()

Option_2 = ['Add new data', 'update the data', 'Total expense spend','Show all data', 'delete the data']

option = st.selectbox("Select the option", (Option_2))


if option == "Add new data":
    date = st.date_input("Enter the date")
    category = st.selectbox("select your category of expenses",
                            ('Vegetables','Outside Food','Grocery','Movie', 'Shopping', 'others'))
    amount = st.number_input("Enter the Amount")
    remarks = st.text_input("Remarks")
    submit = st.button('submit')
    if submit:
        con = sqlite3.Connection("Exp_web.dp")
        cursor = con.cursor()
        sql = "INSERT into Exp (Date, Category, Amount, Remarks) values (?, ?, ?, ?)"
        data = (date, category, amount, remarks)
        cursor.execute(sql, data)
        con.commit()
        con.close()
        st.success("New data added successfully")

elif option == "update the data":
    id = st.number_input("Enter the id to update")
    date = st.date_input("Enter the date")
    category = st.selectbox("select your category of expenses",
                            ('Vegetables', 'Outside Food', 'Grocery', 'Movie', 'Shopping', 'others'))

    amount = st.number_input("Enter the Amount")
    remarks = st.text_input("Remarks")
    submit = st.button('submit')
    if submit:
        con = sqlite3.Connection("Exp_web.dp")
        cursor = con.cursor()
        sql = "Update Exp set Date=?, Category=?, Amount=?, Remarks=? Where id=?"
        data_update = (date, category, amount, remarks, id)
        cursor.execute(sql, data_update)
        con.commit()
        con.close()
        st.success("Data updated successfully")


elif option == "Total expense spend":
    con = sqlite3.Connection("Exp_web.dp")
    cursor = con.cursor()
    sql = "select total(Amount) from Exp"
    cursor.execute(sql)
    con.commit()
    st.write("The total amount spend:")
    st.write(cursor.fetchone()[0])
    con.close()

elif option == "Show all data":
    con = sqlite3.Connection("Exp_web.dp")
    cursor = con.cursor()
    sql = "select ID, Date, Category, Amount, Remarks from Exp"
    cursor.execute(sql)
    data_select = cursor.fetchall()
    st.dataframe(data_select)
    con.close()

elif option == "delete the data":
    to_delete = st.number_input("Enter the id to delete.")
    submit = st.button('submit')
    if submit:
        con = sqlite3.Connection("Exp_web.dp")
        cursor = con.cursor()
        sql = "delete from Exp where id=?"
        data = (to_delete, )
        cursor.execute(sql, data)
        con.commit()
        con.close()
        st.success("Data deleted successfully")


