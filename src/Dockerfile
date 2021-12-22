FROM python

# RUN apt-get update -y && \
#     apt-get install -y python-pip python-dev \

RUN pip install flask

WORKDIR /app

#COPY requirements.txt /app/requirements.txt

#RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

#ENTRYPOINT [ "python" ]

CMD [ "python","app.py" ]