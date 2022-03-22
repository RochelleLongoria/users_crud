# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        
    # Now we use class methods to query our database
    @classmethod
    def Get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users').query_db(query)
        # Create an empty list to append our instances of users
        all_users = []
        # Iterate over the db results and create instances of users with cls.
        for dict in results:
            all_users.append( cls(dict) )
        return all_users

    @classmethod
    #don't forget to put cls and data
    def save(cls, data):
        #query adds users into data based off user input
        query = 'INSERT INTO users (first_name, last_name, email) values (%(fname)s,%(lname)s,%(mail)s);'
        mysql = connectToMySQL('users').query_db(query, data)
        return mysql

    @classmethod
    def delete_user(cls,data):
        query = 'Delete from users where id = %(id)s'
        mysql = connectToMySQL('users').query_db(query, data)
        return mysql

    @classmethod
    def edit_user(cls,data):
        query = 'UPDATE users SET (first_name, last_name, email)  values = (%(fname)s,%(lname)s,%(mail)s) WHERE id = %(id)s;'
        mysql = connectToMySQL('users').query_db(query, data)

    @classmethod
    def profile(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users').query_db(query,data)
        # Create an empty list to append our instances of users
        return cls(results[0])