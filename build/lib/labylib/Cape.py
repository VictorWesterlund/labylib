import requests
import hashlib
import time

class Texture:

	endpoint = "https://www.labymod.net/page/php/cape.php"

	def __init__(self,cookie):
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

	# -----------------------------------

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

	def update(self,img):
		self.appendBinaryFormData(b"file",self.bOpen(img))

		self.closeBinaryFormData() # Add final boundary header

		request = requests.post(Texture.endpoint,
			headers = self.headers,
			cookies = self.cookies,
			data = self.body
		)

		# Raise exception if request fails
		request.raise_for_status()

class Template:

	endpoint = "https://www.labymod.net/page/php/setCapeTpl.php"
	templates = {
		"labymod": "10_LABYMOD.png",
		"minecon2011": "30_MINECON2011.png",
		"minecon2012": "30_MINECON2012.png",
		"minecon2013": "30_MINECON2013.png",
		"minecon2015": "30_MINECON2015.png",
		"minecon2016": "30_MINECON2016.png",
		"minecon2019": "30_MINECON2019.png",
		"prismarine": "30_PRISMARINE.png",
		"christmas2010": "40_CHRISTMAS2010.png",
		"cobalt": "40_COBALT.png",
		"julianclark": "40_JULIANCLARK.png",
		"mapmaker": "40_MAPMAKER.png",
		"mojira": "40_MOJIRA.png",
		"mrmessiah": "40_MRMESSIAH.png",
		"newyear": "40_NEWYEAR.png",
		"scrolls": "40_SCROLLS.png",
		"translator": "40_TRANSLATOR.png",
		"turtle": "40_TURTLE.png",
		"winner": "40_WINNER.png"
	}

	def __init__(self,cookie):
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
		self.addEncodedFormData("cosmetic","cape")

	# -----------------------------------

	# Add URLEncoded form data (x-www-form-urlencoded)
	def addEncodedFormData(self,key,value):
		body = "&"

		# Remove '&' delimiter for first item
		if(self.body == ""):
			body = ""

		body += f"{key}={value}"

		self.body += body

	# -----------------------------------

	def update(self,value):
		value = value.lower()

		if(value not in Template.templates):
			raise ValueError(f"'{value}' is not a valid template.")

		texture = Template.templates[value]

		self.addEncodedFormData("cape",texture)

		request = requests.post(Template.endpoint,
			headers = self.headers,
			cookies = self.cookies,
			data = self.body
		)

		# Raise exception if request fails
		request.raise_for_status()

class Visibility:

	endpoint = "https://www.labymod.net/api/change"

	def __init__(self,cookie):
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
		self.addEncodedFormData("item",459595)
		self.addEncodedFormData("site","control")

	# -----------------------------------

	# Add URLEncoded form data (x-www-form-urlencoded)
	def addEncodedFormData(self,key,value):
		body = "&"

		# Remove '&' delimiter for first item
		if(self.body == ""):
			body = ""

		body += f"{key}={value}"

		self.body += body

	# -----------------------------------

	def update(self,value):
		# Interpret strings 
		if(type(value) != int):
			if(value == "show"):
				value = 1
			elif(value == "hide"):
				value = 0
			else:
				raise ValueError(f"'{value}' is not a valid visibility state.")

		self.addEncodedFormData("value",value)

		request = requests.post(Visibility.endpoint,
			headers = self.headers,
			cookies = self.cookies,
			data = self.body
		)

		# Raise exception if request fails
		request.raise_for_status()