FROM selenium/standalone-chrome-debug

USER root

# Install MySQL Client
RUN apt-get update && \
    apt-get install -y mysql-client && \
    rm -rf /var/lib/apt/lists/*

# Install required Python packages
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip install --upgrade google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2 bs4 emoji notion tqdm gspread oauth2client selenium pytz mysql-connector-python

# Set environment variables for MySQL connection
ENV MYSQL_HOST=172.25.81.163
ENV MYSQL_PORT=3306
ENV MYSQL_USER=princesharma74
ENV MYSQL_PASSWORD=3P@Bmeera#
ENV MYSQL_DATABASE=sync_notion

# Copy your application files to the container
COPY . /app
WORKDIR /app

CMD ["python3", "main.py"]
