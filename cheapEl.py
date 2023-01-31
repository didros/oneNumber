import streamlit as st
from datetime import datetime
import datetime as dt
import pytz
import requests

URL = "https://" + st.secrets.jeedom_host + "/core/api/jeeApi.php"
PARAMS = {'apikey':st.secrets.jeedom_api_key, 'type':'cmd', 'id':'2046'}

r = requests.get(url = URL, params = PARAMS)
h = float(r.text)

now = datetime.now(pytz.timezone('Europe/Oslo'))
offset = dt.timedelta(hours=float(r.text))
#offset = dt.timedelta(hours=float("3"))
new_time= now + offset

if h == 0 :
    t = "Nu ! altså om :"
else :
    t = "kl. " + new_time.strftime("%H:%M") + "m dvs. om"

st.title("Når er strøm billigste i dag før kl. 8.00 i Oslo?")

st.metric(t, r.text + " timer")
