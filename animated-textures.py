import re
import json
import importlib
from pathlib import Path

# from labylib import Cape

class Config:
	
	f = ".animate-config.json"
	pattern = "^[-,a-zA-Z0-9]{1,128}$" # PHPSESSID pattern

	template = '{\n\t"PHPSESSID": "",\n\t"cosmetics": {\n\t\t"cape": {\n\t\t\t"interval": 15,\n\t\t\t"random": false\n\t\t}\n\t}\n}'

	def __init__(self):
		self.config = None
		self.exists = True # Config file already exists
		self.load()

	# Example: getCosmetic("cape")
	def getCosmetic(self,key):
		return self.config["cosmetics"][key]

	# Example: setCosmetic("cape","interval",30)
	def setCosmetic(self,cosmetic,key,value):
		self.config["cosmetics"][cosmetic][key] = value
		self.save()

	def setPHPSESSID(self,phpsessid):
		self.config["PHPSESSID"] = phpsessid
		self.save()

	# -----------------------------------------------------

	# (Over)write config file
	def save(self):
		f = open(Config.f,"w")
		f.write(json.dumps(self.config))
		f.close()

	# Create config file from template
	def create(self):
		self.exists = False

		f = open(Config.f,"w")
		f.write(Config.template)
		f.close()

	# Load the config file from disk into memory
	def load(self):
		# Create config file if absent
		if(Path(Config.f).is_file() == False):
			self.create()

		f = open(Config.f,"r")
		self.config = json.load(f)
		f.close()
		return True

class Main:
	
	def __init__(self):
		self.config = Config()
		self.init()

	# Guided step-by-step setup
	def wizard(self):
		# +-----------+
		# |  Labylib  |
		# +-----------+
		def box(string):
			charset = ["+","-","|"] # Corner,borderX,borderY
			string = f"  {string}  " # Text padding

			box = charset[0]
			# Repeat 'borderX' char for string length
			for x in string:
				box += charset[1]
			box += charset[0]

			# Stitch it all together
			string = f"{charset[2]}{string}{charset[2]}"
			string = f"{box}\n{string}\n{box}"

			return string

		msgDone = "Done! Closing Wizard"

		print(box("Labylib Setup Wizard"))
		print("Make sure you read the README before you begin\n")

		self.config.setPHPSESSID(input("Paste your PHPSESSID here:\n"))

		advanced = input("\nDo you wish to modify the default cosmetic settings? 'y/n'[n]: ")
		if(advanced != "y"):
			print(box(msgDone))
			self.start()
			return
		
		wizard = self.config.config["cosmetics"]

		# Iterate over all cosmetics in config
		for cosmetic in wizard:
			print(box("Cosmetic > " + cosmetic.capitalize()))

			# Iterate over every cosmetic setting
			for key, default in wizard[cosmetic].items():
				value = input(f"Set value for '{key}'[{default}]: ")
				# Ignore input if empty or data type doesn't match default
				if(len(value) < 1):
					print(f"Input error: Expected data type '{type(default)}'. Falling back to default")
					value = default

				self.config.setCosmetic(cosmetic,key,value)
		
		print(box(msgDone))
		self.start()

		#for cosmetic in wizard:

	def start(self):
		phpsessid = self.config.config["PHPSESSID"]
		start = input(f"\nStart Labylib for PHPSESSID '{phpsessid}'? 'y/n/config'[y]: ")

		if(start == "n"):
			return

		if(start == "config"):
			self.wizard()
			return

		print("Labylib is running.. (type 'stop' to close Labylib)")

	def init(self):
		print("Labylib 0.0.1")

		if(self.config.exists and len(self.config.config["PHPSESSID"]) > 1):
			self.start()
			return

		# Prompt if user wants to use guided setup
		print("-- Welcome to Labylib --\nSince this is your first time here, would you like to walk through the setup process?\n")
		wizard = input("Start guided setup? 'y/n':[y] ")
		if(wizard == "n"):
			print(f"A config file '{Config.f}' has been created for you. Run this command again when you're ready")
			return

		self.wizard()
		
# Start Labylib
labylib = Main()