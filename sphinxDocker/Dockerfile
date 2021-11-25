# in your Dockerfile
FROM sphinxdoc/sphinx

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git \
    apt-get install -y nano

RUN apt-get autoremove \
    apt-get clean \
    rm -rf /var/lib/apt/lists/*

#RUN pip3 install git+https://github.com/shomah4a/sphinxcontrib.youtube.git#egg=httpie
RUN pip3 install 'recommonmark' \
                'sphinxcontrib.youtube' \
                'sphinx_rtd_theme' \
                'urllib3'

# u will need to fix urlparse in a youtube.py file.
# apt update before installing nano 

CMD ["make", "html"]
