# Chessboard AI 

This program finds what pieces moved from an intial image of a chessboard and gives that move to stockfish which makes a move and returns that value.


# Visual representation of piece detection model
![Alt text](chessAImodel.png?raw=true "neutron app image")

## How to run?

### Nvidia GPU (Faster Runtime)
1. install docker on your system https://docs.docker.com/engine/install/
2. follow the guide at https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html  and install for your system. 
3. run ```docker build -t chessai .``` in directory Nvidia containing the Dockerfile 
4. run ``` docker run  -p 9081:9081 --gpus all chessai```

### CPU (Slower Runtime) 

1. install docker on your system https://docs.docker.com/engine/install/ 
2. run ```docker build -t chessai .``` in directory Not-optimized containing the Dockerfile 
4. run ``` docker run  -p 9081:9081 --gpus all chessai```


## The API 

### Calling the API to grab the moves from the image example in python: 

Set the strenght to the depth you want in this case it is set to 1.
```
import requests

url = "http://localhost:9081/upload"

payload = {'strength': '1'}
files=[
  ('file',('20240126_143131_HDR_(1) 2.jpg',open('/Users/akash/Source/chessAI/chessboard/Testing/20240126_143131_HDR_(1) 2.jpg','rb'),'image/jpeg'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
```

### Reset the chessboard
  ```
import requests

url = "http://localhost:9081/gamestat"

payload = {'reset': 'true'}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
```
### Unrelated: how to export conda environment
```conda env export  --from-history > linux_environment.yml```

