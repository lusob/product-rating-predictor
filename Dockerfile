FROM python:3
ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt
ADD . /
ENV FLASK_APP=main.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]