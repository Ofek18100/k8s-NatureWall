HOW TO ADD CODE

update the code and the rerun the docker build -t command (make sure to add version to tag name)
after you made a new docker image - docker push the image to docker hub.
then go to deploy.yaml in kubernetes folder and edit the image it should take from cloud
finally - kubectl apply -f .

and you new website will be on....
