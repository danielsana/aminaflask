from flask import Flask, render_template, request
import pymysql

#create the main app
app=Flask(__name__)


@app.route("/")

@app.route("/register", methods=['post,get'])

def register():
    if request.method == 'post':
        connection = pymysql.connect(host='localhost', user='root', password='', database='aminacosmetics')

        #receving information from the form
        username = request.form['username']
        password = request.form['password']
        phonenumber = request.form['phonenumber']

        # define the sql query

        sql = "insert into user(username,password,phonenumber) values (%s,%s,%s)"

        #create the cursor

        cursor = connection.cursor()

        # execute the sql

        cursor.execute(sql,(username,password,phonenumber))

        # commit the changes in the database

        connection.commit()

        print("saved successfully")
    else:
        return render_template("signup.html")
    
app.run(debug=True)
# username="janekamau"
# password="bfirjw788982"
# phonenumber='07678956154'
# cursor=connection.cursor()
# sql = "insert into user(username,password,phonenumber) values (%s,%s, %s)"
# data=(username,password,phonenumber) 


# cursor.execute(sql,data)
# connection.commit()





# print("Record Saved Successfully")




# SELECT IN PYTHON:Login,Ecommerce....
# UPDATE 
# DELETE
# FLASK-python framework to run web applications