from src.SDTLClient import SDTLClient
from pathlib import Path


# Create an SDTL client, passing the API endpoint in
client = SDTLClient("")

# Add everything in the scripts folder to the client
script_directory = Path('./scripts')
client.add_directory(script_directory)

# Generate the SDTL transformations
client.transform()

# Save the transformations to the sdtl/ directory
client.save()
