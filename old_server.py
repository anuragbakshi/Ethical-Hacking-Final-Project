import http.server

class Test307Handler(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		print("GET", self.path)
		print(self.headers)

		self.send_response(307)
		self.send_header("Location", "https://facebook.com" + self.path)
		self.end_headers()

	def do_POST(self):
		print("POST", self.path)
		print(self.headers)
		print(self.rfile.read(int(self.headers["Content-Length"])))

		self.send_response(307)
		self.send_header("Location", "https://facebook.com" + self.path)
		self.end_headers()


httpd = http.server.HTTPServer(("", 80), Test307Handler)
httpd.serve_forever()