
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
        
    @classmethod
    def get_ninjas_in_dojo(cls, dojo_id):
        query = """
            SELECT ninjas.*
            FROM ninjas
            JOIN dojos ON ninjas.dojo_id = dojos.id
            WHERE dojos.id = %(dojo_id)s
        """
        data = {
            'dojo_id': dojo_id
        }

        db = connectToMySQL(cls.db)
        results = db.query_db(query, data)

        ninjas_in_dojo = []
        for row in results:
            ninja_data = {
                "id": row['id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "age": row['age'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at']
            }
            ninja_instance = ninja.Ninja(ninja_data)
            ninjas_in_dojo.append(ninja_instance)

        return ninjas_in_dojo

    # Create Users Models



    # Read Users Models



    # Update Users Models



    # Delete Users Models