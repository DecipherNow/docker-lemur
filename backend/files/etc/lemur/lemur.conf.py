# This is just Python which means you can inherit and tweak settings

import os
_basedir = os.path.abspath(os.path.dirname(__file__))

THREADS_PER_PAGE = 8

# General

# These will need to be set to `True` if you are developing locally
CORS = False
debug = False

# this is the secret key used by flask session management
SECRET_KEY = os.environ['LEMUR_SECRET_KEY']

# You should consider storing these separately from your config
LEMUR_TOKEN_SECRET = os.environ['LEMUR_TOKEN_SECRET']
LEMUR_ENCRYPTION_KEYS = os.environ['LEMUR_ENCRYPTION_KEYS']

# List of domain regular expressions that non-admin users can issue
LEMUR_WHITELISTED_DOMAINS = []

# Mail Server
LEMUR_EMAIL = os.environ['LEMUR_EMAIL']
LEMUR_SECURITY_TEAM_EMAIL = [os.environ['LEMUR_EMAIL']]

# Certificate Defaults
LEMUR_DEFAULT_COUNTRY = os.environ['LEMUR_DEFAULT_COUNTRY']
LEMUR_DEFAULT_STATE = os.environ['LEMUR_DEFAULT_STATE']
LEMUR_DEFAULT_LOCATION = os.environ['LEMUR_DEFAULT_LOCATION']
LEMUR_DEFAULT_ORGANIZATION = os.environ['LEMUR_DEFAULT_ORGANIZATION']
LEMUR_DEFAULT_ORGANIZATIONAL_UNIT = os.environ['LEMUR_DEFAULT_ORGANIZATIONAL_UNIT']

# Authentication Providers
ACTIVE_PROVIDERS = []

# Metrics Providers
METRIC_PROVIDERS = []

# Logging
LOG_LEVEL = os.environ['LEMUR_LOG_LEVEL']
LOG_FILE = "/var/log/lemur/lemur.log"

# Database
SQLALCHEMY_DATABASE_URI = os.environ['LEMUR_POSTGRES_URL']

# Issuers
CFSSL_URL = os.environ['LEMUR_CFSSL_URL']

with open('/etc/lemur/tls/root.crt', 'r') as file:
    CFSSL_ROOT = file.read()
with open('/etc/lemur/tls/intermediate.crt', 'r') as file:
    CFSSL_INTERMEDIATE = file.read()
