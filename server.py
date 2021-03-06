from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import json

disable_ads = {
	"response": {
		"title": "Disable ads",
		"price": 10
	}
}

confirm_purchase = {
	"response": {
		"order_id": 123,
		"app_order_id": 123
	}
}

class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def do_POST(self):
        self.send_response(200)

        print(self.headers)
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length)

        print(post_data)

        request = dict()

        for s in post_data.split(b"&"):
        	splitted = s.split(b"=")
        	request[splitted[0]] = splitted[1]

        print(request)

        if b"get_item" in request[b'notification_type']:
        	response = json.dumps(disable_ads)
        elif b"order_status_change" in request[b'notification_type']:
        	response = confirm_purchase
        	response["response"]["order_id"] = int(request[b'order_id'].decode())
        	response["response"]["app_order_id"] = response["response"]["order_id"]
        	response = json.dumps(response)

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