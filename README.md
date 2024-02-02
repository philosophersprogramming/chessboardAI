# chessboard Computer Vison 

This program finds what pieces moved from an intial image of a chessboard that is given to it and updates the board as the next image containing the next move is given and only reports the change in moves from the images. The program can also be used with an AI (ex stockfish) moving the pieces on the actual board by giving the move that was played to program so that it will ignore that move as change on the image but still update what pieces have moved, so that it only reports the change that the player made to the AI. Note the images provided to this program have to be from a top angle view of the chessboard.

## How to run?

### Nvidia GPU (Faster Runtime)
1. install docker on your system https://docs.docker.com/engine/install/
2. follow the guide at https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html  and install for your system. 
3. run ```docker build -t chessai .``` in directory Nvidia containing the Dockerfile 
4. run ```docker run --gpus all chessai```

### CPU (Slower Runtime) 

1. install docker on your system https://docs.docker.com/engine/install/ 
2. run ```docker build -t chessai .``` in directory Not-optimized containing the Dockerfile 
4. run ```docker run chessai```


## The API 

### Calling the API to grab the moves from the image example in python: 
```
import requests

url = "http://localhost:9081/upload" # change to the server address

payload = {}
files=[
  ('file',('NAMEOFFILE',open('FILEPATH','rb'),'image/jpeg')) # replace NAMEOFFILE with the name of the file and replace FILEPATH with the path to file
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
```

### Updating moves to not counted as changes in image (if your using an AI to move pieces)

```
import requests

url = "http://localhost:9081/chessmove" # change to server address

payload = {'move': 'd7d5'}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)

```

### Unrelated: how to export conda environment
```conda env export  --from-history > linux_environment.yml```

