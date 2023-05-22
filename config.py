import os

_basedir = os.path.abspath(os.path.dirname(__file__))

# HEROKU ENV
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'bvevoziovkbuck')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'ad9c35854e81b21853829f1e13fee7d483efb7e454e1c56179e53aee2ab0fa3e')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'ec2-34-242-154-118.eu-west-1.compute.amazonaws.com')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'dcm44cv9ftqjk6')

SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}?sslmode=require"

# DEV ENV
# DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'postgres')
# DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'Panribou1')
# DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
# DATABASE_NAME = os.getenv('DATABASE_NAME', 'postgres')
#
# SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"

CONTENTFUL_SPACE_ID = 'ivu7p66elrjd'
CONTENTFUL_ACCESS_TOKEN = 'DQPKTv3cLkLLYkiZdubD4vrLAQgy0q1tVpepW3mbSKM'

del os
