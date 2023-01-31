FROM python:3.10-slim

RUN useradd -ms /bin/bash twitter_enterer
USER twitter twitter_enterer

WORKDIR /giveaway_enterer

COPY ./requirements.txt /giveaway_enterer/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /giveaway_enterer/requirements.txt

COPY . /giveaway_enterer

EXPOSE 8080

CMD ["python3", "./src/main.py"]