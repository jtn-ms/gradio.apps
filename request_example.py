import requests

# Replace with the URL of your API
api_url = 'http://localhost:8080/embedding'

# Replace with the path to the image file you want to upload
image_path = 'path_to_your_image.jpg'

# Prepare the image file as a multipart form-data
files = {'file': ('image.jpg', open(image_path, 'rb'))}

# Send the POST request to the API
response = requests.post(api_url, files=files)

# Check the response
if response.status_code == 200:
    result = response.json()
    print('OCR Result:')
    print(result['result'])
else:
    print('Error:', response.text)
