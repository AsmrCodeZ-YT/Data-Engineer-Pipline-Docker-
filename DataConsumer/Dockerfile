FROM python:3.10-alpine

WORKDIR /app

COPY . .

ENV USERNAME=postgres
ENV PASSWORD=changeme
ENV PORT_POSTGRES=5432
ENV HOSTNAME=localhost
ENV DB_NAME=ecommerce_docker 
ENV PORT_REDIS=6379
ENV HOSTNAME_REDIS=localhost

RUN pip install --no-cache-dir redis

# Run app.py when the container launches
CMD ["python3", "consumer.py"]