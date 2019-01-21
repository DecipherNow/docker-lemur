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

ENV LEMUR_ENCRYPTION_KEYS "RR9MHofNA017H_6OI4p6yo4xGEV7DNa1PgQaoIj_hew="
ENV LEMUR_SECRET_KEY "wzY0jNuEETKLYyNkRqWj2nbz5Lh4iu2AHDXzfCODIgmCaaiS/2yMVA=="
ENV LEMUR_TOKEN_SECRET "hnaxJ/ErddxQRDS6k/vZ9GmFzBPZVuYiVJkzy747+etlcNzCggag4w="
ENV LEMUR_EMAIL "martin.brenner@hnl.gov"
ENV LEMUR_DEFAULT_COUNTRY = "US"
ENV LEMUR_DEFAULT_STATE = "Indiana"
ENV LEMUR_DEFAULT_LOCATION = "Hawkins"
ENV LEMUR_DEFAULT_ORGANIZATION = "Hawkins National Laboratory"
ENV LEMUR_DEFAULT_ORGANIZATIONAL_UNIT = "Research"
ENV LEMUR_LOG_LEVEL "WARN"
ENV LEMUR_PASSWORD "password"
ENV LEMUR_POSTGRES_HOST "localhost"
ENV LEMUR_POSTGRES_PORT "5432"
ENV LEMUR_POSTGRES_USERNAME "lemur"
ENV LEMUR_POSTGRES_PASSWORD "lemur"
ENV LEMUR_POSTGRES_DATABASE "lemur"
ENV LEMUR_POSTGRES_ADMIN_USERNAME "lemur"
ENV LEMUR_POSTGRES_ADMIN_PASSWORD "lemur"
ENV LEMUR_CFSSL_URL "http://localhost:8888"
ENV LEMUR_CFSSL_ROOT_CERTIFICATE ""
ENV LEMUR_CFSSL_INTERMEDISTE_CERTIFICATE ""

RUN apk --no-cache add \
  libldap \
  openssl \
  postgresql-client \
  python3 \
  tzdata

COPY --from=builder /usr/local/src/lemur /usr/local/src/lemur
COPY files/ /

RUN ln -s /usr/local/src/lemur/venv/bin/lemur /usr/local/bin/lemur

RUN mkdir -p /var/log/lemur
RUN chown -R 0:0 /etc/lemur/tls /var/log/lemur
RUN chmod -R g=u /etc/lemur/tls /var/log/lemur

EXPOSE 8000
USER 1000
VOLUME /etc/lemur/tls

ENTRYPOINT ["/usr/local/bin/entrypoint"]

CMD ["/usr/local/bin/lemur", "start", "-b", "0.0.0.0:8000", "--config", "/etc/lemur/lemur.conf.py"]
