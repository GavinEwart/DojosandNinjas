
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import ninja
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class Dojo:
    db = "dojos_and_ninjas_schema" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # What changes need to be made above for this project?
        #What needs to be added here for class association?

    @classmethod
    def get_all_dojos(cls):
        query = """
                SELECT * FROM dojos
                """
        dojos = []
        results = connectToMySQL(cls.db).query_db(query)
        for dojo in results:
            dojos.append(cls(dojo))
        print(results)
        print(dojos)
        return dojos

    @classmethod
    def get_dojo_by_id(cls, dojo_id):
        query = """
                SELECT * FROM dojos
                WHERE id = %(id)s
                """
        data = {
            'id': dojo_id
        }

        db = connectToMySQL(cls.db)
        result = db.query_db(query, data)

        if result:
            dojo_data = result[0]
            dojo = cls(dojo_data)
            return dojo
        else:
            return None
        
    @classmethod
    def create_new_dojo(cls, data):
        query = """
                INSERT INTO dojos (name)
                VALUES (%(name)s)
                """
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        if result:
            return result
        else:
            return "Failed to add user"

    # Create Users Models



    # Read Users Models



    # Update Users Models



    # Delete Users Models