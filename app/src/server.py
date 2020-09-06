from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
 return "My names is Ahmad it is Devops Course !!!!"  
if __name__ == "__main__":
   server.run(host='0.0.0.0')