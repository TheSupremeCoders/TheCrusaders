FROM selenium/standalone-chrome-debug

USER root

RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip install --upgrade google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2 bs4 emoji tqdm gspread oauth2client selenium pytz

COPY . /app
WORKDIR /app

CMD ["python3", "main.py"]
