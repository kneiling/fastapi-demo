From python:3.11

ENV CODE_DIR=/src
ENV APP=${CODE_DIR}/app/main.py
ENV HOST=0.0.0.0
ENV PORT=3000
ENV PYTHONPATH=/src

WORKDIR ${CODE_DIR}

COPY . ${CODE_DIR}
COPY ./requirements.txt ${CODE_DIR}/requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "/src/app/scripts/startup.sh"]
