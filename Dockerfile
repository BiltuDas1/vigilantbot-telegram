FROM stopback/python-alpine
COPY --chown=root:root requirements.txt /app
COPY --chown=root:root *.py /app