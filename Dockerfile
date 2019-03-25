FROM python:3.7.2-slim
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ENV PYTHONPATH $(pwd)
CMD ["python", "dataset/dataset_getter.py"]
