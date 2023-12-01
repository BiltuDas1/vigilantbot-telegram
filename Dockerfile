FROM python:3.10.13-alpine
LABEL version="0.1.3-alpha"
LABEL build_date="2023-12-01"
LABEL maintainer="Biltu Das <billionto@gmail.com>"
LABEL license="MPL-2.0"

COPY --chown=root:root start.sh /app/run
COPY --chown=root:root requirements.txt /app/requirements.txt
COPY --chown=root:root *.py /app/
COPY --chown=root:root bot /app/bot
CMD [ "/bin/sh", "/app/run" ]
