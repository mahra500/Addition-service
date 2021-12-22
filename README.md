# Addition-service

This project helps with addition of two integers.

# Contents

(1) `app.py` : The main python script
(2) Folder-Blueprints : Contains modules with required functions
(3) Dockerfile

# Api endpoint
- /addition : accepts two numbers in a GET request and returns the sum of them
for example : http://192.168.1.59:8000/addition?number_1=345&number_2=12 will return 357

# How to use?

- Clone the repository 
- Build image using "docker build -t addition-service:1.0.0 ."
- Run image using "docker run -p 5000:5000 addition-service:1.0.0"
