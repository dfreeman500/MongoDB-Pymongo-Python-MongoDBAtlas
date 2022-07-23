# Practice with Mongodb, Python, Pymongo, and MongoDB Atlas


## Some References


* https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb
* https://www.youtube.com/watch?v=UpsZDGutpZc&list=PLzMcBGfZo4-nX-NCYorkatzBxjqRlPkKB&index=2
* https://www.mongodb.com/cloud/atlas/register
* https://www.mongodb.com/languages/python
* https://pypi.org/project/pymongo/

#
## Set up Virtual Environment
* python -m venv env
* source env/Scripts/activate
* pip install items
* pip freeze > requirements.txt
#
## Set up the Database
Python 3.10.4

1. sign up on mongodb.com
2. Create a shared cluster on cloud atlas
3. Choose region closest to you that is free
4. create user ( username and password)

5. Click on "Add my current IP address" to access from local environment
6. Click on overview
7. Click on Connect
8. get connection string (ex: Connect Your Application), Choose language/version 
mongodb+srv://\<user\>:\<password\>@\<database_name\>.chjgl.mongodb.net/?retryWrites=true&w=majority
9. pip install pymongo[srv]pip3 install python-dotenv   (allows to access environment variable file which to store credentials for signing into mongodb).
10. Install vscode extension: mongodb for vscode
11. create environment variable file .env in same directory as python file. 
12. Put password into password variable inside .env file (ex: MONGODB_PWD = "")
13. Load the environment variable automatically without specifying path. In python file: from dotenv import load_dotenv, find_dotenvload_dotenv(find_dotenv())
14. import:
import os
import pprint
from pymongo import MongoClient

15. grab password in python file:password = os.environ.get("MONGODB_PWD")

16. create connection string with f string (ex: switch \<password\> for {password}connection_string = f"   {password}    "
17. Now that there is a connection string, then connect.
client = MongoClient(connection_string)

18. run main.py (should have no errors).
19. Download mongodb compass, get mongodb compass connection string, paste into mongodb compass connection string section with password in \<password\> space, hit connect(if doesn't work make sure IP address is in the IP access list)
20. create database (db and collection) ex: 'test', 'test'




Database
    ^
   Collections
       ^
      Documents

MongoDB uses BSON, very similar to JSON


20:53