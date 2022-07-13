FROM ubuntu:latest
WORKDIR /home/user

RUN apt-get update && apt-get install -y python3 python3-pip



RUN pip install streamlit
RUN pip install joblib
RUN pip install sklearn

COPY model_dashboard.py /home/user/
COPY regression.joblib /home/user/

CMD streamlit run model_dashboard.py
