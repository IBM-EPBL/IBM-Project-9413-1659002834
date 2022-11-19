from flask import Flask, render_template , request , redirect
app = Flask(_name_)

users = [
   {"name":"prime","email":"praveen1412822@gmail.com","password":"secret"}
]

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/about")
def about():
   return render_template("about.html")

@app.route("/signin" ,methods = ['POST', 'GET'])
def signin():
   if request.method == 'POST':
      user_email = request.form['email']
      user_password = request.form['password']
      for user in users:
         if user["email"] == user_email:
            if user["password"] == user_password:
               return redirect("/home")
               
   
   return render_template("signin.html")

@app.route("/signup" ,methods = ['POST', 'GET'])
def signup():
   if request.method == 'POST':
      user_name = request.form['name']
      user_email = request.form['email']
      user_password = request.form['password']
      users.append({"name":user_name , "email":user_email , "password":user_password})
      return redirect("/home")

   return render_template("signup.html")

@app.route("/home")
def home():
   return render_template("home.html")

@app.route("/users")
def user():
   return users

if _name_ == '_main_':
   app.run(debug = True)