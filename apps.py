import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dropbox
from datetime import datetime
import pytz
from time import time
from dropbox.files import SearchMode
from pprint import pprint 
import xlwt
from xlwt import Workbook
from pprint import pprint
from urllib.request import urlopen
wb=Workbook()
sheet1=wb.add_sheet('sheet1')
link_save=[]
link_save1=[]
end_time = datetime.now()
start_time = datetime(2021,3,6)
dbx = dropbox.Dropbox("ivQfY-JHUqgAAAAAAAAPJgN-QxsMaKslNyaohgGPZsfYymal9uisjIf1iy83lox3")
start = time()
Line_Number = 0
k=1;
critical=0;
import datetime
start_time = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%d-%b-%Y")
#start_time = datetime.datetime(2021,3,12).strftime("%d-%b-%Y")
print(start_time)
Search_Results = dbx.files_search_v2(start_time, options=dropbox.files.SearchOptions(path='/Statistics'))
for result in Search_Results.matches:
    file = result.metadata.get_metadata()
    file_name = file.name
    file_link = dbx.files_get_temporary_link('/Statistics/'+file_name).link
    if start_time in file_name :
        Line_Number += 1
        #print("%s: File Name: %s \n File Link:%s"%(Line_Number, file_name,file_link))
        link_save.append(file_name)
        link_save1.append(file_link)
        sheet1.write(k,0,file_link)
        k=k+1;
link3=link_save
link4=link_save1
link5=[]
numinde=[]
Total_link=[]
for i in link3:
    sp=i.split('_')
    sp1=sp[1:5]
    link5.append(sp1)
l1=[]
for i in link5:
    if i not in l1:
        l1.append(i)
for i in l1:
    numindex=link5.index(i)
    numinde.append(numindex)
for i in numinde:
    link6=link4[i]
    Total_link.append(link6)
for j in Total_link:
    webp=urlopen(j)
    data1=(webp.read())
    data2=data1.decode('utf-8')
    data3=data2.splitlines()
    data5=[]
    data7=[]
    data9=[]
    for i in data3:
        data4=i.split('#')[-1]
        data5.append(data4)
    for i in data5:
        data6=i.split(':')[0]
        data8=i.split(':')[-1]
        data7.append(data6)
        data9.append(data8)
    list5=['CurrentScore','LyfasCAMSscore']
    index1=data7.index(list5[1])
    index2=data7.index(list5[0])
    current=float(data9[index2])
    lyfam=float(data9[index1])
    if current<50 and lyfam<50:
        critical=critical+1;
count=len(Total_link)
start_times = (datetime.datetime.now()-datetime.timedelta(days=1))
List=[start_times,count,critical]
df1=pd.read_excel('Dashboard.xlsx')
df=pd.DataFrame([[List[0],List[1],List[2]]],columns=['Date','Count','Critical'])
df3=df1.append(df)
df3.to_excel('Dashboard.xlsx',index=False)
data=pd.read_csv("Dashboard.xlsx")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)
app = dash.Dash(__name__)
server=app.server
app.layout = html.Div(
    children=[
        html.H1(children="Acculi Lbas Pvt.Ltd.",),
        html.H2(children="March Data Analytics",),
        html.P(
            children=""
            ""
            " ",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Count"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Total Test in March"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Critical"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Total Test in March"},
            },
        ),
    ]
)






