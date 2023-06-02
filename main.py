from cmsimde import flaskapp51133125githubio.zhenyulin1.repl.co
from gevent.pywsgi import WSGIServer

#flaskapp.app.run(host="0.0.0.0", debug=True)
http_server = WSGIServer(('0.0.0.0', 8080), flaskapp.app)
http_server.serve_forever()