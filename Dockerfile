FROM python:3.9-slim
VOLUME /my_vol
COPY src/opt/code src/opt/code
COPY src/opt/input src/opt/input
COPY src/opt/local_output src/opt/local_output
RUN pip install -r src/opt/code/requirements.txt
ENTRYPOINT ["python3","src/opt/code/main.py"]
