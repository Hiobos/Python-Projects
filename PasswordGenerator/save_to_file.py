import os
import json

class Save:
    def __init__(self):
        pass

    def to_file(self, website, email, password):
        data_file = {
            website: {
                'email': email,
                'password': password,
            }
        }

        new_data = {
            website: {
                'email': email,
                'password': password,
            }
        }

        if not os.path.exists('passwords.json'):  # checks if file exists
            with open('passwords.json', "w") as file:  # creates new json file
                json.dump(data_file, file, indent=4)
        else:
            with open('passwords.json', "r") as file:
                data = json.load(file)
                data.update(new_data)
            with open('passwords.json', "w") as file:
                json.dump(data, file, indent=4)

    def search(self):
        with open('passwords.json', "r") as file:
            data = json.load(file)
            print(data)
