FROM python:3.11

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip3 install torch torchvision torchaudio

RUN pip install ultralytics

RUN pip install tensorrt

RUN pip install tensorrt_lean

RUN pip install tensorrt_dispatch

RUN pip install flask

WORKDIR /app

COPY final_algorithm/Nvidia /app/

EXPOSE 9081
ENV PORT 9081
ENV HOSTNAME "0.0.0.0"
CMD [ "python", "./app.py" ]




