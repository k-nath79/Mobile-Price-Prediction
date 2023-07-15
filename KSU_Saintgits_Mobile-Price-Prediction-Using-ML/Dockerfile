FROM jupyter/base-notebook
WORKDIR /app
COPY /code/mobileprice.ipynb /app/
COPY /data/final.csv/ /app/
COPY /code/requirements.txt /app/
RUN pip install -r requirements.txt
EXPOSE 8888
CMD ["jupyter","notebook","--ip=0.0.0.0","--no-browser","--allow-root"]


