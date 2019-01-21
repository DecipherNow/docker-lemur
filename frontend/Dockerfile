FROM alpine:3.8 as builder

ARG VERSION

RUN apk --no-cache add \
  autoconf \
  automake \
  bash \
  curl \
  cyrus-sasl-dev \
  gcc \
  git \
  libffi-dev \
  libressl-dev \
  make \
  musl-dev \
  nasm \
  nodejs \
  npm \
  openldap-dev \
  postgresql-dev \
  python3-dev \
  tar \
  zlib-dev

RUN pip3 install -U virtualenv

WORKDIR /usr/local/src

RUN git clone https://github.com/netflix/lemur.git

WORKDIR /usr/local/src/lemur

RUN git reset --hard ${VERSION}
RUN virtualenv -p python3 venv && source venv/bin/activate && make release

FROM alpine:3.8

LABEL maintainer="Joshua Rutherford <joshua.rutherfor@deciphernow.com>"

ENV LOG_LEVEL "warn"
ENV LEMUR_BACKEND_HOST "localhost"
ENV LEMUR_BACKEND_PORT "8000"
ENV TLS_CA_CERTIFICATE ""
ENV TLS_SERVER_CERTIFICATE ""
ENV TLS_SERVER_KEY ""

RUN apk --no-cache add \
  nginx

COPY --from=builder /usr/local/src/lemur/lemur/static/dist /var/lib/nginx/html
COPY files/ /

RUN mkdir -p /var/run/nginx
RUN chown -R 0:0 /etc/nginx /var/lib/nginx /var/log/nginx /var/run/nginx /var/tmp/nginx
RUN chmod -R g=u /etc/nginx /var/lib/nginx /var/log/nginx /var/run/nginx /var/tmp/nginx

EXPOSE 8443
USER 1000
VOLUME /etc/nginx/tls

ENTRYPOINT ["/usr/local/bin/entrypoint"]

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
