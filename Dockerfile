FROM continuumio/miniconda3  	
WORKDIR /home/app			
RUN apt-get update			
RUN pip install -r requirements.txt
COPY . /home/app		
CMD streamlit run --server.port $PORT Home.py 	