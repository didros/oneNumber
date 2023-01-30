import streamlit as st
from datetime import datetime
import datetime as dt
import requests

URL = "https://" + st.secrets.jeedom_host + "/core/api/jeeApi.php"
PARAMS = {'apikey':st.secrets.jeedom_api_key, 'type':'cmd', 'id':'2241'}

r = requests.get(url = URL, params = PARAMS)

now = datetime.now()
offset = dt.timedelta(minutes=int(r.text))
new_time= now + offset

st.title("Når er strøm billigste i dag?")

st.metric("kl. " + new_time.strftime("%H:%M") + ", dvs. om", r.text + " timer")
