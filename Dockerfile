FROM stopback/python-alpine
COPY --chown=root:root requirements.txt /app/requirements.txt
COPY --chown=root:root *.py /app