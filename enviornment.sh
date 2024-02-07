#conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
conda create -n chesscpu python=3.11
conda install pytorch torchvision torchaudio cpuonly -c pytorch
conda install -c conda-forge ultralytics
pip install chess flask==3.0.1