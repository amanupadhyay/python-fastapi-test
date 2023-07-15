FROM python:3.11-slim 

# Update and upgrade
RUN apt-get -qq update && apt-get -y upgrade

WORKDIR /src

# Build and install python requirements
COPY ./requirements.txt /src
RUN pip install --upgrade pip
RUN pip install wheel && pip install --no-cache-dir -r /src/requirements.txt


# Copy app source
COPY . /src

ENV PYTHONPATH=/
EXPOSE 80

# For development use
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port","80", "--reload"]
# CMD ["gunicorn","-bind=0.0.0.0:8000", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app"]
# For production use
# CMD ["./start.sh"]