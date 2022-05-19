FROM ramadhani892/ramubot:master
RUN git clone -b master https://github.com/yusrilrnld/ram home/ram/

WORKDIR home/ram/

CMD ["python3", "-m", "userbot"]


