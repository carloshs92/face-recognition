FROM aaftio/face_recognition:latest
RUN mkdir /code
COPY . /code/
WORKDIR /code/
RUN pip install --upgrade pip && \
    pip install flask
EXPOSE 5000
CMD ["python", "main.py"]


