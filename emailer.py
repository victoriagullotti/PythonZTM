from smtplib import SMTP
import json
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE

file_url = 'https://dummyjson.com/products'

get_file = requests.get(file_url)

config = list()
json_file = get_file.json()
config.append(json_filec)
