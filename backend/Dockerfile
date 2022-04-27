# start by pulling the python image
FROM python:3

# switch working directory
WORKDIR /app

RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev

ENV FLASK_APP=app.py 

# copy the requirements file into the image
COPY ./requirements.txt .

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . .


CMD ["python","rest.py" ]