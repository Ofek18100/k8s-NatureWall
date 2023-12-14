**HOW TO ADD CODE**
1. update the code and then re run the
<code>docker build -t</code>     command (make sure to add version to tag name)
2. run: <code>docker push </code> to the image to docker hub.
3. go to deploy.yaml in kubernetes folder and edit the image it should take from cloud to the latest version you just pushed
4. finally run: <code>kubectl apply -f . --validate=false</code> to aplly the new configuration

and new website will be on....
