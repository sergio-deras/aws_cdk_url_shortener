FROM alpine

RUN apk add curl
ADD ping.sh /ping.sh

CMD ["bin/sh", "/ping.sh"]

# docker build -t pinger  .
# docker run -it -e URL=https://ft3oz2m2nb.execute-api.us-west-1.amazonaws.com/prod/ac4652f1 pinger