FROM python:3.10.13-slim-bullseye
LABEL version="0.1.3-alpha"
LABEL build_date="2023-12-01"
LABEL maintainer="Biltu Das <billionto@gmail.com>"
LABEL license="MPL-2.0"
LABEL description="A self hosted telegram bot for managing large groups"

COPY --chown=root:root start.sh /app/run
COPY --chown=root:root requirements.txt /app/requirements.txt
COPY --chown=root:root *.py /app/
COPY --chown=root:root bot /app/bot
CMD [ "/bin/sh", "/app/run" ]
