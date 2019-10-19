FROM aaftio/face_recognition:latest
RUN mkdir /code
COPY . /code/
WORKDIR /code/
RUN pip install --upgrade pip && \
    pip install flask
RUN pip install Flask-Cors
RUN pip install Flask-Security
RUN easy_install bson
EXPOSE 5000
CMD ["python", "run.py"]


