FROM python:3.12-slim
WORKDIR /shift_project
COPY requirements.txt /shift_project/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /shift_project
CMD ["python", "project.py"]