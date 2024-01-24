FROM continuumio/miniconda3

WORKDIR /app

# Create the environment:
COPY linux_environment.yml .
RUN conda env create -f linux_environment.yml
COPY final_algorithm .

SHELL ["conda", "run", "-n", "chesstorch", "/bin/bash", "-c"]

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "chesstorch", "python", "app.py"]

EXPOSE 5000

ENV PORT 5000
# set hostname to localhost
ENV HOSTNAME "0.0.0.0"
