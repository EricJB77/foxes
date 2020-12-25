import requests

response = requests.get("http://randomfox.ca/floof")

#print(response.status_code)
#print(response.text)
#print(response.json())

fox = response.json()
#print(fox['image'])


from PIL import Image
from io import BytesIO

url = fox['image']
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.show()
