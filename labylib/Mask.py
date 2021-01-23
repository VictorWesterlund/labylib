import requests

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
		self.addEncodedFormData("item",544349)
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
			else:
				value = 0

		self.addEncodedFormData("value",value)

		request = requests.post(Visibility.endpoint,
			headers = self.headers,
			cookies = self.cookies,
			data = self.body
		)

		# Raise exception if request fails
		request.raise_for_status()

class Multi:

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
		self.values = (000000,000000,0,0) # Color,Color,Size,Texture

		# Payload
		self.addEncodedFormData("type","multi")
		self.addEncodedFormData("item",544349)
		self.addEncodedFormData("site","control")

	# -----------------------------------

	def color(color,color2 = None):
		if(color2):
			self.values[0] = color
			self.values[1] = color2
			return
		
		self.values[0] = color[0]
		self.values[1] = color[1]

	def size(size):
		# Interpret strings 
		if(type(size) != int):
			if(size == "big"):
				size = 1
			else:
				size = 0

		self.values[2] = size

	def template(value):
		templates = {
			"None": "null",
			"3": "26b459ce-2f09-4b50-97ad-c589262b0268",
			":3": "3b7492c6-4239-4e4b-9906-d510e722a96b",
			":*)": "4120f1eb-19e6-4f34-8417-d7bd6a01d85a",
			":#)": "43e1b6bf-2a18-40f4-b0b0-38b7c74a6ddb",
			":'3": "4b498414-5894-4124-98f6-b6c5a531b6e8",
			":)": "84456b05-85ba-48bf-a0c8-ca4ba981ff8e",
			":p)": "a387dde9-a1a8-41b8-9e77-8446f8d6d3cd",
			":P": "aaa3db95-6537-4ef0-aa66-050b20412ef6",
			":')": "bb9006f9-b67c-4fff-996b-6d74a1b691d6",
			"::)": "c6aa01db-bd10-4948-9632-afe6bd0c3f3c",
			"X": "e93ec7b5-4148-4d1c-aefd-26c3f125cec7",
			";p": "ed2c847c-5b2b-4916-843d-438b6c039804",
			":~)": "f9e4f616-e697-441e-be57-1b64cc5c5e41"
		}

		if(value not in templates):
			raise ValueError(f"'{value}' is not a valid template.")
			
		self.values[3] = templates[value]

	# -----------------------------------

	# Add URLEncoded form data (x-www-form-urlencoded)
	def addEncodedFormData(self,key,value):
		body = "&"

		# Remove '&' delimiter for first item
		if(self.body == ""):
			body = ""

		body += f"{key}={value}"

		self.body += body

	def update(self,value):
		value = ",".join(self.values)

		self.addEncodedFormData("value",value)

		request = requests.post(Visibility.endpoint,
			headers = self.headers,
			cookies = self.cookies,
			data = self.body
		)

		# Raise exception if request fails
		request.raise_for_status()