import streamlit as st
from datetime import datetime
import datetime as dt
import pytz
import requests

def fetch():

    try:
        if "input_timew" not in st.session_state:
            timewindow = '3 hours'
        else:
            timewindow = st.session_state.input_timew

        if timewindow == '1 hour' :
            st.session_state.jeedom_cmd = "2048" 
        if timewindow == '2 hours' :
            st.session_state.jeedom_cmd = "2049" 
        if timewindow == '3 hours' :
            st.session_state.jeedom_cmd = "2046" 
        if timewindow == '4 hours' :
            st.session_state.jeedom_cmd = "2047"

        PARAMS = {'apikey':st.secrets.jeedom_api_key, 'type':'cmd', 'id':st.session_state.jeedom_cmd}
        URL = "https://" + st.secrets.jeedom_host + "/core/api/jeeApi.php"
        st.session_state.result = requests.get(url = URL, params = PARAMS).text

    except Exception:
        "Oups .... backend down!"

def show():

    h = float(st.session_state.result)

    now = datetime.now(pytz.timezone('Europe/Oslo'))
    offset = dt.timedelta(hours=h)
    new_time= now + offset
        
    if h == 0:
        t = "Nu !"
    else:
        t = "kl. " + new_time.strftime("%-H.00") + ", dvs. om ca."

    if ( new_time.minute >= 30 ) :
        h -= 0.5

    st.metric(t, str(h) + " timer")


def main():

    st.title("Når er strøm billigste i dag (i Oslo)?")

    if "input_timew" not in st.session_state:
        fetch()

    show()

    selVal = ['1 hour','2 hours','3 hours','4 hours']
    timewindow = st.radio(
        "Tidsvindu valgt:",
        selVal,
        index=2,
        horizontal=True,
        key="input_timew",
        on_change=fetch)


if __name__ == '__main__' :
    main()
