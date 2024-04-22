FROM python

WORKDIR /app

COPY word_frequency_analysis.py /app
COPY paragraphs.txt /app

RUN pip install nltk

RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords

CMD ["python", "word_frequency_analysis.py"]