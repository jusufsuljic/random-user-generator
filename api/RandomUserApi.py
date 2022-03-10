from flask_restful import Resource
import random

class RandomUserApi(Resource):
    def randomUser(cls):
        with open('api/names.txt') as namesFile:
            randomNames = namesFile.readlines()

        with open('api/lastnames.txt') as lastnamesFile:
            randomLastNames = lastnamesFile.readlines()

        with open('api/addresses.txt') as addressesFile:
            randomAddresses = addressesFile.readlines()

        return {
            'firstName': random.choice(randomNames).rstrip(),
            'lastName': random.choice(randomLastNames).rstrip().lower().capitalize(),
            'address':  random.choice(randomAddresses).rstrip().split(",", 1)[0],
            'age': random.randint(18, 99),
            'gender': random.choice(['Male', 'Female'])
        }

    def get(self):
        user = self.randomUser()
        if(user):
            return user
        else:
            return {'error': 'Something went wrong'}
