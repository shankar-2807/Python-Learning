from flask import render_template,redirect,request,url_for
import mysql.connector 

con = mysql.connector.connect(host="localhost",user="root",password="shankar@2807",database='library_db')

def add_book():
    if request.method == "GET":
        return render_template("add_book.html")
    else:
        bname = request.form.get("bname")
        sql = "insert into Destination (bname) values (%s)"
        val = (bname,)
        cursor =  con.cursor()
        cursor.execute(sql,val)
        con.commit()
        return redirect(url_for("showAllbook")) 

   
















# from flask import Flask, render_template, request, redirect, url_for,session
# #from config import get_db_connection
# import mysql.connector

# def get_db_connection():
#     conn = mysql.connector.connect(host="localhost", user="root", password="shankar@2807", database="library_db")
#     return conn


# # Show all books

# def index():
#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM Book")
#     books = cursor.fetchall()
#     conn.close()
#     return render_template('index.html', books=books)

# # Add book

# def add_book():
#     if request.method == 'POST':
#         bname = request.form['bname']
#         price = request.form['price']
#         author = request.form['author']
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO Book (bname, price, author) VALUES (%s, %s, %s)", 
#                        (bname, price, author))
#         conn.commit()
#         conn.close()
#         return redirect(url_for('index'))
#     return render_template('add_book.html')

# # Edit book by id

# def edit_book(bid):
#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM Book WHERE bid = %s", (bid,))
#     book = cursor.fetchone()
#     if request.method == 'POST':
#         bname = request.form['bname']
#         price = request.form['price']
#         author = request.form['author']
#         cursor.execute("UPDATE Book SET bname=%s, price=%s, author=%s WHERE bid=%s", 
#                        (bname, price, author, bid))
#         conn.commit()
#         conn.close()
#         return redirect(url_for('index'))
#     conn.close()
#     return render_template('edit_book.html', book=book)

# # Delete book by id

# def delete_book(bid):
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM Book WHERE bid = %s", (bid,))
#     conn.commit()
#     conn.close()
#     return redirect(url_for('index'))

# # Search book by id or name

# def search_book():
#     search = request.form['search']
#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)
#     query = "SELECT * FROM Book WHERE bid = %s OR bname LIKE %s"
#     cursor.execute(query, (search, "%" + search + "%"))
#     books = cursor.fetchall()
#     conn.close()
#     return render_template('index.html', books=books)

