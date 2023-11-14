from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import dojo

class Ninja:
    db = "dojos_and_ninjas_schema" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def show_all_ninjas(cls, dojo_id):
        query = """
            SELECT ninjas.* FROM ninjas
            JOIN dojos ON ninjas.dojo_id = dojos.id
            WHERE dojos.id = %(dojo_id)s
        """
        data = {
            'dojo_id': dojo_id
        }

        db = connectToMySQL(cls.db)
        results = db.query_db(query, data)

        ninjas = []
        for row in results:
            ninja_data = {
                "id": row['id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "age": row['age'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at']
            }
            ninja = cls(ninja_data)
            ninjas.append(ninja)

        return ninjas

    @classmethod
    def create_ninja(cls, data):
        query = """
            INSERT INTO ninjas (dojo_id, first_name, last_name, age)
            VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s)
        """
        db = connectToMySQL(cls.db)
        result = db.query_db(query, data)

        if result:
            return result 
        else:
            return None
