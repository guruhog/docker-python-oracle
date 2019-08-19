from flask import Flask
import cx_Oracle
Import os

app = Flask(__name__)

application = app.server


@app.route('/')
def index():

    #user = "system"
    #pw = "oracle"
    #dsn = "192.168.56.101/orclcdb" 

    user = os.environ.get('DB_USER')
    pw = os.environ.get('DB_PASSWORD')
    host = os.environ.get('DB_HOST', '192.168.56.101')
    sid = os.environ.get('DB_SID')

    con = cx_Oracle.connect(user, pw, host+"/"+sid)

    cur = con.cursor()
    cur.execute('select person_id from people')
    temp = ''
    for person_id in cur:
      temp=temp+"Person ID: "+''.join(str(person_id))+"\r\n"
    return temp


if __name__ == '__main__':
    app.run_server(debug=True)
