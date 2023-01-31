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
    t = "Nu !"
else :
    t = "kl. " + new_time.strftime("%H") + ", altså om ca."

if ( new_time.minute >= 30 ) :
    h -= 0.5

st.title("Når er strøm billigste i dag før kl. 8.00 i Oslo?")
st.metric(t, str(h) + " timer")


timewindow = st.radio(
    "Time window currently selected:",
    ('3 hours', '2 hours', '1 hour'),
    horizontal=True)

if timewindow == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")
