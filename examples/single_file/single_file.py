from src.SDTLClient import SDTLClient
from pathlib import Path

script_file = Path('./script.sass')
client = SDTLClient("")
client.add_file(script_file)
client.transform()
client.save()
