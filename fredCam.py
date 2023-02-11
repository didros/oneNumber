import streamlit as st
import json

import streamlit_echarts as ec
#from streamlit_echarts import st_echarts
from datetime import datetime
import datetime as dt

from streamlit_javascript import st_javascript

global budget
global depense
global fcCon
js    = """localStorage.fcConfig || "{}" """
retJs = st_javascript(js)

if type(retJs).__name__ == "str":
    fcCon = json.loads(retJs)
#fcCon

with st.expander("Personlig info"):

    if "salary" not in fcCon:
        fcCon["salary"] = 50000
    fcCon["salary"] = st.number_input('Angi ditt lønn siste måned', step=100, value = int(fcCon["salary"]))

    if "perhour" not in fcCon:
        fcCon["perhour"] = 100
    else:
        if fcCon["perhour"] == 0 :
            fcCon["perhour"] = 100
    fcCon["perhour"] = st.number_input('Lønn per time', step=10, value = int(fcCon["perhour"]), min_value=100)

    HoursPerWeek = 37.5
    HoursPerDay  = HoursPerWeek / 5
    salaryPerMonth = fcCon["salary"]
    perHour= salaryPerMonth / (HoursPerWeek*4)
    hours = salaryPerMonth / fcCon["perhour"] 
    "Du har jobbet ca. " + str(int(hours)) + " timer forrige måned."

    js    = """localStorage.setItem( "fcConfig", "{\\"salary\\":"""
    js   += str(fcCon["salary"]) 
    js   += """, """
    js   += """\\"perhour\\":"""
    js   += str(fcCon["perhour"]) 
    js   += """}" )"""
    retJs = st_javascript(js)



depense = st.number_input('Angi pris (kr)', step=10)

t = depense/perHour # Number of hours to work
hh, mm = divmod(60*t, 60)
mm = round(mm)
if (mm==60):
    mm=0
    hh += 1
hh = round(hh)

strMin = ""
if (mm == 1):
    strMin = str(mm) + " minutt"
elif (mm > 1):
    strMin = str(mm) + " minutter"
 
strHour = ""
if (hh == 1):
    strHour = str(hh) + " time"
elif (hh > 1):
    strHour = str(hh) + " timer"

if len(strHour)!=0 and len(strMin)!=0:
    st.header("Du må jobbe " + strHour + " og " + strMin)
elif len(strHour) == 0:
    st.header("Du må jobbe " + strMin)
elif len(strMin) == 0:
    st.header("Du må jobbe " + strHour)

options_dag = {
    "title": {"text": "Arbeidsdag", "subtext": str(round(100*((t))/HoursPerDay))+"%", "left": "center"},
    "tooltip": {"trigger": "item"},
#    "legend": {"orient": "vertical", "left": "left",},
    "series": [
        {
            #"name": "Detalje",
            "type": "pie",
            "radius": "50%",
            "data": [
                {"value": round(t,ndigits=1), "name": "Tid du må jobbe (t)"},
                {"value": round(HoursPerDay - t,ndigits=1)}
            ],
            "emphasis": {
                "itemStyle": {
                    "shadowBlur": 10,
                    "shadowOffsetX": 0,
                    "shadowColor": "rgba(0, 0, 0, 0.5)",
                }
            },
        }
    ],
}


ec.st_echarts(
    options=options_dag, height="300px",
)
