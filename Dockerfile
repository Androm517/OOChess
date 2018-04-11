FROM python:3.6
WORKDIR /app
ADD . /app
EXPOSE 9999

CMD ["python3", "game.py"]
