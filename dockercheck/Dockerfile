#use  lightweight linux image
FROM alpine:latest

#set the working directory
WORKDIR /textfolder 

#copy the file from host to container
COPY Welcome.txt /textfolder/Welcome.txt

#run the command to print the file
CMD ["cat", "/textfolder/Welcome.txt"]  