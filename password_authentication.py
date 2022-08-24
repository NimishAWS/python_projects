import getpass
database = {"angel":"Angel@123","dopler":"Dopler@123"}
username= input("Enter your Username: ")
password = getpass.getpass("Enter your Password: ")

for i in database.keys():
    if username== i:
        print("in")
        while password != database.get(i):
            password = getpass.getpass("Enter your right password again: ")
        break
print("Verified")
