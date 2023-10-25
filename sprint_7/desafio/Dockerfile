FROM python

WORKDIR /home

RUN mkdir /dados

COPY series.csv /dados/
COPY movies.csv /dados/
COPY programa.py /dados/

RUN pip install boto3

WORKDIR /dados

ENTRYPOINT ["python","programa.py"]

CMD ["python","programa.py"]

