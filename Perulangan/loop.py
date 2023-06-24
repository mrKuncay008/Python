import time

secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
# while True :
#     magican = int(input("Masukan Number: "))
    
#     if magican == secret_number:
#         print("Well done, muggle! You are free now.")
#     else:
#         print("Ha Ha Ha you stack in my loop\n")

magican = int(input("Masukan Number: "))

while magican:
    print("Ha Ha Ha you stack in my loop")
    print("The Number : ", magican)
    magican += 1
    time.sleep(1)
    
    if magican == secret_number:
        print ("Well done, muggle! You are free now.")
        break
