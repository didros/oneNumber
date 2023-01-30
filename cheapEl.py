import streamlit as st
from datetime import datetime
import datetime as dt
import requests

URL = "https://" + st.secrets.jeedom_host + "/core/api/jeeApi.php"
PARAMS = {'apikey':st.secrets.jeedom_api_key, 'type':'cmd', 'id':'2240'}

r = requests.get(url = URL, params = PARAMS)

now = datetime.now()
offset = dt.timedelta(hours=float(r.text))
new_time= now + offset

st.text("At approximatly : " + new_time.strftime("%H:%M"))

st.title("Når er strøm billiste i dag?")

st.metric("kl. " + new_time.strftime("%H:%M") + ", om", "om " + r.text + " timer")
