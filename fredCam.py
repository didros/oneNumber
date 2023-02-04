import streamlit as st

from streamlit_echarts import st_echarts
from datetime import datetime
import datetime as dt

global budget
global depense


HoursPerWeek = 37.5
HoursPerDay  = HoursPerWeek / 5
salaryPerMonth = 20000

perHour= salaryPerMonth / (HoursPerWeek*4)

"Du tjener ca. " + str(int(perHour)) + " kr per time."

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

options_week = {
    "title": {"text": "Arbeidsuke", "subtext": str(round(100*((t))/HoursPerWeek))+"%", "left": "center"},
    "tooltip": {"trigger": "item"},
#    "legend": {"orient": "vertical", "left": "left",},
    "series": [
        {
            #"name": "Detalje",
            "type": "pie",
            "radius": "50%",
            "data": [
                {"value": round(t,ndigits=1), "name": "Tid du må jobbe (t)"},
                {"value": round(HoursPerWeek - t,ndigits=1)}
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


st_echarts(
    options=options_dag, height="300px",
)

st_echarts(
    options=options_week, height="300px",
)

