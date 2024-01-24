FROM python:3.11

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

RUN pip install ultralytics

RUN pip install flask

WORKDIR /app

COPY final_algorithm /app/

EXPOSE 5000
ENV PORT 3000
ENV HOSTNAME "0.0.0.0"
CMD [ "python", "./app.py" ]




