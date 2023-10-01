
## Image
```sh
# img2str
curl -F "file=@path_to_your_image.jpg" http://localhost/embedding

# imgs2str
curl -F "file1=@path_to_image1.jpg" -F "file2=@path_to_image2.jpg" http://localhost:8080/verify
```