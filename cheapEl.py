import streamlit as st
from datetime import datetime
import datetime as dt
import pytz
import requests

if "jeedom_cmd" not in st.session_state:
    st.session_state.jeedom_cmd = '2046'

URL = "https://" + st.secrets.jeedom_host + "/core/api/jeeApi.php"
PARAMS = {'apikey':st.secrets.jeedom_api_key, 'type':'cmd', 'id':st.session_state.jeedom_cmd}

r = requests.get(url = URL, params = PARAMS)
h = float(r.text)
"debug : " + r.text

now = datetime.now(pytz.timezone('Europe/Oslo'))
offset = dt.timedelta(hours=float(r.text))
#offset = dt.timedelta(hours=float("3"))
new_time= now + offset
    
if h == 0 :
    t = "Nu !"
else :
    t = "kl. " + new_time.strftime("%H") + ", altså om ca."

if ( new_time.minute >= 30 ) :
    h -= 0.5

st.title("Når er strøm billigste i dag før kl. 8.00 i Oslo?")
st.metric(t, str(h) + " timer")


selVal = ['1 hour','2 hours','3 hours','4 hours']
timewindow = st.radio(
    "Time window currently selected:",
    selVal,
    index=2,
    horizontal=True)


if timewindow == '1 hour' :
    st.session_state.jeedom_cmd = "2048" 
if timewindow == '2 hours' :
    st.session_state.jeedom_cmd = "2049" 
if timewindow == '3 hours' :
    st.session_state.jeedom_cmd = "2046" 
if timewindow == '4 hours' :
    st.session_state.jeedom_cmd = "2047" 

timewindow
st.session_state.jeedom_cmd