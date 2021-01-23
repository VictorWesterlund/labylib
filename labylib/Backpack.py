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
		self.addEncodedFormData("item",525800)
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
		self.values = (000000,000000)

		# Payload
		self.addEncodedFormData("type","multi")
		self.addEncodedFormData("item",525800)
		self.addEncodedFormData("site","control")

	# -----------------------------------

	def color(color,color2 = None):
		if(color2):
			self.values[0] = color
			self.values[1] = color2
			return
		
		self.values[0] = color[0]
		self.values[1] = color[1]

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