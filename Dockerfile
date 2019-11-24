FROM ubuntu

# Install Python.
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "python3-dev", "python3-pip"]
RUN ["python3", "-m", "pip", "install", "virtualenv"]
WORKDIR /var/jenkins_home/workspace/twitterbot
RUN ["bash"]
RUN ["virtualenv", "env"]
CMD ["./env/bin/python", "setup.py", "test"]
