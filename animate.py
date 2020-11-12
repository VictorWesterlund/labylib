import re
import json
import importlib
from pathlib import Path

# from labylib import Cape

# Don't forget to reflect in .gitignore if you change this
name = "animated-textures"

class Config:
	
	textures = f"./{name}/" # Cosmetic textures path
	f = f"./{name}/config.json" # JSON Config file
	default = '{"PHPSESSID": "","cosmetics": {"cape": {"interval": "15","randomOrder": "False"}}}' # Default config
	pattern = "^[-,a-zA-Z0-9]{1,128}$" # PHPSESSID pattern

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

	# Create config file from default template
	def create(self):
		self.exists = False

		Path(Config.textures).mkdir(parents=True,exist_ok=True)

		f = open(Config.f,"w")
		f.write(Config.default)
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

		# TODO: Attach labylib hook here

	def init(self):
		print("Labylib 0.0.1\n")

		if(self.config.exists and len(self.config.config["PHPSESSID"]) > 1):
			self.start()
			return

		for cosmetic in self.config.config["cosmetics"]:
			Path(Config.textures + cosmetic).mkdir(parents=True,exist_ok=True)

		# Prompt if user wants to use guided setup
		print("-- Labylib Animated Textures --\nSince this is your first time here, would you like to walk through the setup process?\n")
		wizard = input("Start guided setup? 'y/n':[y] ")
		if(wizard == "n"):
			print(f"A config file '{Config.f}' has been created for you. Run this command again when you're ready")
			return

		self.wizard()
		
# Start Labylib
labylib = Main()