# Chessboard AI

This program finds what pieces moved from an intial image of a chessboard and gives that move to Leela Chess Zero which is Open source neural network based chess engine (https://lczero.org/) with Maias Weights (https://github.com/CSSLab/maia-chess):

# Visual representation of piece detection model

![Alt text](chessAImodel.png?raw=true "neutron app image")

## How to run?

Please change your config in .Example env in Cpu to match your Auth0 api settings and Lc0 config and rename '.Example env' to '.env'. 


## Broken right now 
### Nvidia GPU (Faster Runtime)

1. install docker on your system https://docs.docker.com/engine/install/
2. follow the guide at https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html and install for your system.
3. run `docker build -t chessai .` in directory Nvidia containing the Dockerfile
4. run ` docker run  -p 9081:9081 --gpus all chessai`

### CPU (Slower Runtime)

1. install docker on your system https://docs.docker.com/engine/install/
2. run `docker build -t chessai .` in directory Cpu directory containing the Dockerfile
3. run ` docker run  -p 9081:9081 --gpus all chessai`

## The API

### Calling the API to grab the moves from the image example in python:

Set the strenght to the depth you want in this case it is set to 1.

```
import requests

url = "http://localhost:9081/upload" #set your server address

payload = {}
files=[
  ('file',('test1.png',open('$PATHTOFILE','rb'),'image/png')) # replace $PATHTOFILE to the file path of the image
]
headers = {
  'authorization': $YOUROAuth2ClientSecretGoesHere # replace this value with your auth0 key

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)

```

### Reset the chessboard and setting the AI to play as white

This resets the entire board and starts a fresh game with option to let AI play as white

```
import requests

url = "http://localhost:9081/gamestat"  #set your server address

payload = {'reset': 'true',
'iswhite': 'true'} # change value iswhite to false if you are playing as white
files=[

]
headers = {
  'authorization': $YOURAuth0ClientSecretGoesHere # replace this value with your auth0 key
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)

```

### Unrelated: how to export conda environment

`conda env export  --from-history > linux_environment.yml`
