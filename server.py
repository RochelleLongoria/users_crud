from flask import Flask, redirect, render_template, request
from user import User
app = Flask(__name__)   
# -------Display---------------
# -----first page route needs display the users and create user hyperlink----

@app.route('/')
@app.route('/users')
def display_users():
    return render_template('users.html')

# --------Display Create User form page --------

@app.route('/users/new')
def show_create_user_form():
    return render_template('create_user.html')

# ------Process Create User form -----

@app.route('/users/new/process', methods = ['POST'])  
def create_users():
    User.save(request.form)
    return redirect('/read_all')

# -------Display Single User Page -----

@app.route('/user/<int:id>')
def profile(id):
    data = {"id": id}
    return render_template('read_one.html', user = User.profile(data))

# ---------Edit User Page ------

@app.route('/user/<int:id>/edit')
def edit(id):
    return render_template('edit.html')

# -------- Process Editing on User ------

@app.route('/user/fixed')
def process_edit():
    User.save(request.form)
    return redirect ('/read_all')

# -------Delete Process on Deleting User--------

@app.route('/user/<int:id>/destroy')
def delete_user(id):
    data = {'id' : id}
    User.delete_user(data)
    return redirect ('/read_all')

# ------Call the get all classmethod to get all users

@app.route('/read_all')
def index():
    user = User.Get_all()
    return render_template('read_all.html', all_users = user)

if __name__=="__main__":  
    app.run(debug=True)    

