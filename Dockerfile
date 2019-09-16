FROM python:3
WORKDIR /app
COPY . /app
RUN mkdir -p log
RUN pip install --trusted-host pypi.python.org -r requirements.txt
CMD ["python", "my_script.py"]
