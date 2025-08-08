import platform,os
from gevent.pywsgi import WSGIServer
from flask import Flask,render_template,request
import requests,json,os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

local_ip = os.getenv('LOCAL_IP','192.168.10.9')
port    =  int(os.getenv('PORT',3001))
base_url = str(os.getenv('BASE_URL'))

# @app.route('/')
# def index():
#     return 'Index'

@app.route('/')
def serials():
    d = request.args.get('d')
    t = request.args.get('t')
    if d == None or t == None:
        return 'No req params',200
    else:
        url = base_url + '&doc_id=' + str(d) + '&tovar_id=' + str(t)
        response = requests.get(url)
        json_data = json.loads(response.content.decode('utf-8'))
        # Дістаємо серійні номери
        serials = [item['TOVAR_SER_NUM'] for item in json_data]

        # Формуємо відповідь — кожен номер з нового рядка
        text_output = '\n'.join(serials)
        return render_template('serials.html', serials=serials,d=d,t=t)



if __name__ == "__main__":
    if platform.system() == 'Windows':
        http_server = WSGIServer((local_ip, int(port)), app)
        print(f"Running HTTP-SERVER ver.  on port - http://" + local_ip + ':' + str(port))
    else:
        http_server = WSGIServer(('', int(port)), app)
        print(f"Running HTTP-SERVER ver.  on port :" + str(port))
    http_server.serve_forever()