import requests
import hashlib
import time

class BadRequestError(Exception): pass

class Cape:

	endpoint = "https://www.labymod.net/page/php/cape.php"

	def __init__(self,cookie,img):
		self.validate(cookie,img)

		self.body = "" # Initialize request body
		self.cookies = dict(PHPSESSID = cookie)
		self.boundary = self.boundary()

		self.headers = {
			"accept": "*/*",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "en-US,en;q=0.9,sv;q=0.8",
			"cache-control": "no-cache",
			"dnt": "1",
			"user-agent": "Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0",
			"origin": "https://www.labymod.net",
			"pragma": "no-cache",
			"referer": "https://www.labymod.net/dashboard",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"x-requested-with": "XMLHttpRequest",
			"Content-Type": "multipart/form-data; boundary=" + self.boundary
		}
		
		self.addFormData("cosmetic","cape")
		self.addFormData("file",self.bOpen(img))
		self.closeFormData()

	# -----------------------------------

	def validate(self,cookie,file):
		return True

	# Generate boundary header from MD5-hash of current time
	def boundary(self):
		seed = str(time.time())
		md5 = hashlib.md5(seed.encode("utf-8"))

		boundary = "----WebKitFormBoundary" + md5.hexdigest()
		return boundary

	# Open and return file binary as string
	def bOpen(self,file):
		f = open(file,"rb")
		content = str(f.read())
		f.close()

		length = len(content) - 1
		content = content[2:length]

		return content

	# Append form-data to request body and boundary header
	def addFormData(self,name,payload):
		body = contentType = ""
		eol = "\r\n"

		disposition = f'name="{name}"'
		if(name == "file"):
			contentType = "Content-Type: image/png" + eol
			
			# Use current epoch as filename. It has to be different from last request
			filename = str(round(time.time())) + ".png" 
			disposition += f'; filename="{filename}"'

		body += f"--{self.boundary}" + eol # Init data header
		body += f"Content-Disposition: form-data; {disposition}" + eol
		body += contentType + eol + eol
		body += payload + eol

		self.body += body

	# Last form-data has been set, add final post width for boundary header
	def closeFormData(self):
		self.body += f"--{self.boundary}--\r\n\r\n"

	# -----------------------------------

	def update(self):
		request = requests.post(Cape.endpoint,
			headers = self.headers,
			cookies = self.cookies,
			data = self.body
		)

		if(request.text != "OK"):
			raise BadRequestError(request.text)