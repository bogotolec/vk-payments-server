from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import json

disable_ads = {
	"response": {
		"title": "Disable ads",
		"price": 10
	}
}

class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def do_POST(self):
        self.send_response(200)

        response = json.dumps(disable_ads)

        self.send_header("Content-type", "text/json")
        self.end_headers()
        self.wfile.write(response.encode("UTF-8"))

def run(server_class=HTTPServer, handler_class=HttpGetHandler):
	server_address = ('', 80)
	httpd = server_class(server_address, handler_class)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		httpd.server_close()

if __name__=="__main__":
	run()