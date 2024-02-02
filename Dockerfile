FROM continuumio/miniconda3  	
WORKDIR /home/app			
RUN apt-get update	
COPY requirements.txt /home/app/requirements.txt	
RUN pip install -r /home/app/requirements.txt
COPY . /home/app		
CMD mlflow server -p $PORT --default-artifact-root $ARTIFACT_STORE_URI --backend-store-uri $BACKEND_STORE_URI