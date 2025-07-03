FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE ${PORT}

CMD ["sh", "-c", "streamlit run app.py --server.port=${PORT} --server.address=0.0.0.0"]
