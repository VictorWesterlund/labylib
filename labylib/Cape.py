import requests
import hashlib
import time

class RequestError(Exception): pass

class Texture:

	endpoint = "https://www.labymod.net/page/php/cape.php"

	def __init__(self,cookie,img):
		self.validate(cookie,img)

		self.body = b"" # Initialize request body
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
		
		self.appendBinaryFormData(b"cosmetic",b"cape")
		self.appendBinaryFormData(b"file",self.bOpen(img))

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
		content = f.read()
		f.close()

		return content

	# Append form-data to request body and boundary header
	def appendBinaryFormData(self,name,payload):
		body = contentType = b""
		eol = b"\r\n"

		disposition = b'name="' + name + b'"'
		if(name == b"file"):
			contentType = b"Content-Type: image/png" + eol
			
			# Use current epoch as filename. It has to be different from last request
			filename = str(round(time.time())) + ".png"
			filename = filename.encode()
			disposition += b'; filename="' + filename + b'"'

		body += b"--" + self.boundary.encode() + eol # Init data header
		body += b"Content-Disposition: form-data; " + disposition + eol
		body += contentType + eol
		body += payload + eol

		self.body += body

	# Last form-data has been set, add final post width for boundary header
	def closeBinaryFormData(self):
		self.body += b"--" + self.boundary.encode() + b"--\r\n\r\n"

	# -----------------------------------

	def update(self):
		self.closeBinaryFormData() # Add final boundary header

		request = requests.post(Texture.endpoint,
			headers = self.headers,
			cookies = self.cookies,
			data = self.body
		)

		# Raise exception if request fails
		# Use [3:5] to clean up junk chars from reponse body
		if(str(request.text)[3:5] != "OK"):
			raise RequestError(str(request.text))

class Visibility:

	endpoint = "https://www.labymod.net/api/change"

	def __init__(self,cookie,value):
		self.validate(cookie,value)

		self.cookies = dict(PHPSESSID = cookie)

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
			"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
		}

		self.body = ""

		# Payload
		self.addEncodedFormData("type","switch")
		self.addEncodedFormData("value",value)
		self.addEncodedFormData("item",459595)
		self.addEncodedFormData("site","control")

	# -----------------------------------

	def validate(self,cookie,file):
		return True

	# Add URLEncoded form data (x-www-form-urlencoded)
	def addEncodedFormData(self,key,value):
		body = "&"

		# Remove '&' delimiter for first item
		if(self.body == ""):
			body = ""

		body += f"{key}={value}"

		self.body += body

	# -----------------------------------

	def update(self):
		request = requests.post(Texture.endpoint,
			headers = self.headers,
			cookies = self.cookies,
			data = self.body
		)

		# Raise exception if request fails
		# Use [3:5] to clean up junk chars from reponse body
		if(str(request.text)[3:5] != "OK"):
			raise RequestError(str(request.text))