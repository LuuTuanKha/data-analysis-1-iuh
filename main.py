import dash_bootstrap_components as dbc
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
app = dash.Dash(__name__, suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])

#####

data = pd.read_excel('./data.xlsx')

##BAR CHAR 01
data=pd.read_excel('./data.xlsx')
df=pd.DataFrame(data, columns=['State','Hospital Beds Needed, Six Months','Hospital Beds Needed, Twelve Months','Hospital Beds Needed, Eighteen Months'])
df_s=np.array(df['State']) #animals
df_6T=np.array(df['Hospital Beds Needed, Six Months'])
df_12T=np.array(df['Hospital Beds Needed, Twelve Months'])
df_18T=np.array(df['Hospital Beds Needed, Eighteen Months'])
index= np.arange(len(df_s))
width=0.26
bar_char_01 = go.Figure(data=[
    go.Bar(name='Six Months', x=df_s, y=df_6T),
    go.Bar(name='Twelve Months', x=df_s, y=df_12T),
    go.Bar(name='Eighteen Months', x=df_s, y=df_18T)
])
##
bar_char_01.update_layout(barmode='group',title ="Biểu đồ biểu diễn số giường bệnh cần có  trong vòng 6, 12 và 18 tháng tới tại các bang.")
##bar_char_02
df=pd.DataFrame(data, columns=['State','ICU Beds Needed, Six Months','ICU Beds Needed, Twelve Months','ICU Beds Needed, Eighteen Months'])
df_sicu=np.array(df['State'])
df_6TICU=np.array(df['ICU Beds Needed, Six Months'])
df_12TICU=np.array(df['ICU Beds Needed, Twelve Months'])
df_18TICU=np.array(df['ICU Beds Needed, Eighteen Months'])
bar_char_02 = go.Figure(data=[
    go.Bar(name='6 tháng', x=df_sicu, y=df_6TICU),
    go.Bar(name='12 tháng', x=df_sicu, y=df_12TICU),
    go.Bar(name='18 tháng', x=df_sicu, y=df_18TICU)
])

# Change the bar mode
bar_char_02.update_layout(barmode='stack',title='Số giường chuẩn ICU cần thiết trong vòng 6,12,18 tháng',xaxis_title='Bang',
                   yaxis_title='Giường')

## end bar char 01

# London_10_year_fig = px.line( x=arrLondonYear, y=arrLondonPop,title='Population of London 10 years later')

#####

main = html.Div([
    # home page text
    html.Div(),
    html.Div('Home page', style={
        'fontSize': '50px',
        'color': 'black',
        'textAlign': 'center'

    }),
    # link to another page
    html.Div([
        dcc.Link('Simple Chart', href='/simple-chart', style={
             'color': 'black'
             }),
        dcc.Link('Data Analysis', href='/data-analysis', style={
            'color': 'black'
        })
    ], style={
        'display': 'flex',
        'justify-content': 'space-evenly',

    }, className='mt-4'),

    # introduce tag
    html.Div([
        html.Div([
            html.Div('Introduction to project: ', style={
                'fontSize': '25px',
                'fontWeight': 'bold',
            }),
            html.Div([
                html.Div( [
                    html.Div('- Hospital capacity data from HGHI (Phân tích số liệu giường bệnh từ HGHI): Phân tích và Ước tính công suất bệnh viện theo thời gian (6, 12, 18 tháng), nếu 20%, 40% hoặc 60% dân số Mỹ mắc phải COVID-19.'),
                    html.Div('- Nền tảng của project:  '),
                    html.Div(' + Framework: Dash '),
                    html.Div(' + Ngôn ngữ: Python '),
                    html.Div(' + Môi trường:  Google Co-Lab, Jupyter Notebook & PyCharm '),
                    html.Div(' + Hosting: Heroku '),
                    html.Div(' + Raw Data Source: data.world ')

                ],className='col-8'),
                html.Img(src='./assets/img/doctor.jpg', className='col-4')

            ], className='row', style={ 'fontSize': '15px' })
        ])
    ], className='mt-5 bg-light intro'),
     html.Div([
        html.Div([
            html.Div('About my team:', style={
                'fontSize': '25px',
                'fontWeight': 'bold',
            }),
            html.Div([
                html.Img(src='./assets/img/myteam.png', className='col-4'),
                html.Div([
                html.Div('18093751 - Lưu Tuấn Kha'),
                html.Div('18080931  - Nguyễn Tấn Hưng'),
                html.Div('18086141 - Phan Thị Tứ Thi'),
                html.Div('18077551 - Nguyễn Huỳnh Công Lý'),
                html.Div('18093421 - Lê Văn Tài'),
                html.Div('18094051 - Nguyễn Tấn Minh'),


                ],className='col-4 team'),
                 html.Div( [
                html.Div(''),
                html.Div(''),
                html.Div('')
                ],className='col-4'),
            ], className='row', style={ 'fontSize': '25 px' })
        ])
    ], className='mt-5 bg-light intro'),

    #my team
    # background
], className='container mt-5')

##-----------------------------------------------------
#Simple Chart Link
simpleChart = html.Div([
     html.Div(style={
        'width': '100%',
        'height': '100%',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'z-index': '-999',

    }),
     # home page text
    html.Div(
    ),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Dash Plotly', href="/simple-chart", className='el'),
                dcc.Link('2D-Histogram', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
                dcc.Link('Dot Chart', href="/dot-chart", className='el'),
                dcc.Link('Line Chart', href="/line2-chart", className='el'),

                
            ],className='listInside')
        ],
        className='col-3 listContainer bg-light'),
        html.Div([
            html.Div([
                html.Div('Dash - plotly', className='title'),
                dcc.Link('Home Page', href="/"),
            ], className='fl'),
            html.Div([
                 html.Span('Introductionto  Dash - Plotly:', className='introMatplotlib'),
                html.Span('Dash là Framework Python hiệu quả để xây dựng các ứng dụng phân tích dữ liệu trên web. Được viết bằng Flask, Plotly.js và React.js, Dash rất lý tưởng để xây dựng các ứng dụng trực quan hóa dữ liệu với giao diện người dùng dễ dàng tuỳ chỉnh bằng Python thuần. Nó đặc biệt phù hợp cho bất kỳ ai làm việc với dữ liệu bằng Python. Dash loại bỏ tất cả các công nghệ và giao thức cần thiết để xây dựng một ứng dụng dựa trên web tương tác. Dash đủ đơn giản để bạn có thể liên kết giao diện người dùng của mình bằng  Python trong một thời gian ngắn. Dash triển khai ứng dụng của mình tới các máy chủ và sau đó chia sẻ chúng thông qua các URL.',className='content')
            ])
           
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')

##-----------------------------------------------------

## 2D-Histogram

df_his = pd.DataFrame(data, columns=['Available Hospital Beds','Projected Infected Individuals'])

fig_his_01 = px.density_heatmap(df_his, x="Available Hospital Beds", y="Projected Infected Individuals",nbinsx=20, nbinsy=20, color_continuous_scale="Viridis", title="Tỷ lệ bệnh nhân dự kiến và số giường bệnh trống, dữ liệu tổng hợp từ từng bang")
df_his = pd.DataFrame(data, columns=['Total Hospital Beds','Total ICU Beds','Adult Population'])

fig_his_02 = px.density_heatmap(df_his, x="Total Hospital Beds", y="Total ICU Beds", z= 'Adult Population',marginal_x="histogram", marginal_y="histogram",histfunc="avg",title="Tỷ lệ người trưởng thành, số giường bệnh  và số giường bệnh đạt chuẩn ICD , dữ liệu tổng hợp từ từng bang")










##-----------------------------------------------------
# 2D-Histogram Link
lineChart = html.Div([
     # home page text
    html.Div(
    ),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Dash Plotly', href="/simple-chart", className='el'),
                dcc.Link('2D-Histogram', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
                  dcc.Link('Dot Chart', href="/dot-chart", className='el'),
                dcc.Link('Line Chart', href="/line2-chart", className='el'),
            ],className='listInside')
        ],
        className='col-3 listContainer bg-light'),
        html.Div([
            html.Div([
                html.Div('2D-Histogram', className='title'),
                dcc.Link('Home Page', href="/"),
            ], className='fl'),
            html.Div([
                 html.Span('Mô tả:', className='introMatplotlib'),
                html.Span('Biểu đồ 2D rất giống với biểu đồ 1D. Các khoảng lớp của tập dữ liệu được vẽ trên cả trục x và y. Không giống như biểu đồ 1D, biểu đồ này được vẽ bằng cách bao gồm tổng số kết hợp của các giá trị xảy ra trong khoảng thời gian x và y, đồng thời đánh dấu các mật độ đó.',className='content')
            ]),
            html.Div([
                 html.Span('Sử dụng khi nào?:', className='introMatplotlib'),
                html.Span('Histogram được sử dụng để phân tích mối quan hệ giữa hai biến dữ liệu có nhiều giá trị.',className='content')
            ]),
            html.Div([
                 html.Span('Type of charts:', className='introMatplotlib')
            ]),
            html.Div([
                html.Div('Type 1:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= fig_his_01), className='col-12'
                )
            ], className='row'),

             html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= fig_his_02), className='col-12'
                )
            ], className='row'),
            
    
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')
#####------------------------------------------------------------------------------

# # Bar Chart Link


#Type 2 chart


#---------------------------------------------
barChart = html.Div([
     # home page text
    html.Div(),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Dash Plotly', href="/simple-chart", className='el'),
                dcc.Link('2D-Histogram', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
                dcc.Link('Dot Chart', href="/dot-chart", className='el'),
                dcc.Link('Line Chart', href="/line2-chart", className='el'),
            ],className='listInside')
        ],
        className='col-3 listContainer bg-light'),
        html.Div([
            html.Div([
                html.Div('Bar Chart', className='title'),
                dcc.Link('Home Page', href="/"),
            ], className='fl'),
            html.Div([
                 html.Span('Mô tả:', className='introMatplotlib'),
                html.Span('Biểu đồ bar chart là biểu đồ hình cột dùng để mô phỏng xu hướng thay đổi của các đối tượng theo thời gian hoặc để so sánh các số liệu/yếu tố của các đối tượng. Biểu đồ bar chart thường có hai trục: một trục là đối tượng/yếu tố cần được phân tích, trục còn lại là thông số của các đối tượng. .',className='content')
            ]),
            html.Div([
                 html.Span('Sử dụng khi nào?:', className='introMatplotlib'),
                html.Span('Bar chart (biểu đồ cột): thường được dùng khi cần phân Type dữ liệu và so sánh độ tương quản giữa chúng ',className='content')
            ]),
            html.Div([
                 html.Span('Type of charts:', className='introMatplotlib')
            ]),
            html.Div([
                html.Div('Type 1:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure=bar_char_01), className='col-12'
                )
            ], className='row'),
                html.Div([
                 html.Span('Ý nghĩa:', className='introMatplotlib'),
                ##html.Span('Biểu đồ biểu diễn số giường bệnh cần có, để phục vụ bệnh mắc bệnh trong 6, 12, 18 tháng tại các bang.',className='content'),
                html.Span('# Thông qua biểu đồ, ta thấy được tại tất cả các bang, số giường bệnh cần có trong 6 tháng đầu mắc dịch Covid là cao nhất và nó thấp dần trong 12 tháng, 18 tháng. Như vậy, chúng ta thấy rằng số bệnh nhân mắc bệnh trong 6 tháng tại các bang rất cao , số người mắc trong thời gian tiếp theo sẽ giảm dần do đó nhà nước thông qua số liệu này sẽ tìm ra giải pháp phân bổ nhân sự là bác sĩ đến công tác đúng nơi và đúng vị trí công tác của mình những nơi tập trung,khoảng thời gian người mắc bệnh nhiều thì số bác sĩ giỏi nhiều hơn bác sĩ khác cung những nơi người mắc bệnh nặng thì cần điều chuyển những bác sĩ giỏi để nâng cao viện chữa bệnh',className='content')

            ]),

             html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= bar_char_02), className='col-12'
                )
            ], className='row'),
            
    
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')


##-----------------------------------------------------
## pie chart draw
##

df_pie=pd.DataFrame(data, columns=['State','Total Hospital Beds'])
df_state=np.array(df_pie['State']) #animals
df_beds=np.array(df_pie['Total Hospital Beds'])
fig_pie_01 = px.pie(df_state, values=df_beds, names=df_state, title="Tỉ lệ giường bệnh của các bang")
fig_pie_01.update_traces(textposition='inside')
fig_pie_01.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')

#========== pie 02
df_bed=pd.DataFrame(data, columns=['Potentially Available Hospital Beds*','Proejcted Hospitalized Individuals'])
data_PAH=sum(df_bed['Potentially Available Hospital Beds*'])
data_PHI=sum(df_bed['Proejcted Hospitalized Individuals'])
data_AI= data_PHI - data_PAH
labels = ['tỉ lệ giường bệnh dự kiến có thể có để sử dụng','tỉ lệ giường bệnh thiếu']
values = [data_PAH,data_AI]

pie_char_02 = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='percent',
                             insidetextorientation='radial',pull=[0.05, 0],hole=.3
                            )])









# Use `hole` to create a donut-like pie chart

##-----------------------------------------------------
## pie chart
##
pieChart = html.Div([
     # home page text
    html.Div(),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Dash Plotly', href="/simple-chart", className='el'),
                dcc.Link('2D-Histogram', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
                  dcc.Link('Dot Chart', href="/dot-chart", className='el'),
                dcc.Link('Line Chart', href="/line2-chart", className='el'),
            ],className='listInside')
        ],
        className='col-3 listContainer bg-light'),
        html.Div([
            html.Div([
                html.Div('Pie Chart', className='title'),
                dcc.Link('Home Page', href="/"),
            ], className='fl'),
            html.Div([
                 html.Span('Mô tả:', className='introMatplotlib'),
                html.Span('Một biểu đồ pie (hoặc một biểu đồ hình tròn ) là một hình tròn đồ họa thống kê , được chia thành lát để minh họa tỷ lệ số. Trong biểu đồ hình tròn, độ dài cung của mỗi lát cắt (và do đó là góc và diện tích trung tâm của nó ), tỷ lệ với số lượng mà nó biểu diễn.',className='content')
            ]),
            html.Div([
                 html.Span('Sử dụng khi nào?:', className='introMatplotlib'),
                html.Span('Pie chart (biểu đồ tròn) được sử dụng khi cần biểu diễn dữ liệu liên quan về mặt tỷ lệ dưới dạng % ',className='content')
            ]),
            html.Div([
                 html.Span('Type of charts:', className='introMatplotlib'),
            ]),
            html.Div([
                html.Div('Type 1:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= fig_pie_01), className='col-12'
                )
            ], className='row'),

             html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= pie_char_02), className='col-12'
                )
            ], className='row'),
            
    
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')

##______________________________________________________
#scatter charts
p = data['Projected Infected Individuals']
state  = df_s
PII = data['Projected Infected Individuals']
scatt_char_01 = go.Figure(data=go.Scatter(
    y = PII,
    x = state,
    mode='markers',
    marker=dict(
        size=15,
        color=-p,
        colorscale='Viridis',
        showscale=True
    )
))
scatt_char_01.update_layout(title='Projected Infected Individuals of USA States')

# scatt #2
pop65 = data['Population 65+']
scatt_char_02 = go.Figure(data=go.Scatter(x=state,
                                y=pop65,
                                mode='markers',
                                marker_color=pop65,
                                text=state))

scatt_char_02.update_layout(title='Population 65+ of USA States')
#scatter #3
ICUbeds = df_his['Total ICU Beds']
country = state
beds = df_his['Total Hospital Beds']
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=country,
    y=beds,
    name='Total Hospital Beds',
    marker=dict(
        color='rgba(156, 165, 196, 0.95)',
        line_color='rgba(156, 165, 196, 1.0)',
    )
))
fig.add_trace(go.Scatter(
    x=country, y=ICUbeds,
    name='Total ICU Beds',
    marker=dict(
        color='rgba(204, 204, 204, 0.95)',
        line_color='rgba(217, 217, 217, 1.0)'
    )
))

fig.update_traces(mode='markers', marker=dict(line_width=1, symbol='circle', size=16))

fig.update_layout(
    title="Biểu đồ so sánh giường bệnh thường và giường bệnh chuẩn ICU",
    xaxis=dict(
        showgrid=False,
        showline=True,
        linecolor='rgb(102, 102, 102)',
        tickfont_color='rgb(102, 102, 102)',
        showticklabels=True,
        ticks='outside',
        tickcolor='rgb(102, 102, 102)',
    ),
    margin=dict(l=140, r=40, b=50, t=80),
    legend=dict(
        font_size=10,
        yanchor='middle',
        xanchor='right',
    ),
    paper_bgcolor='white',
    plot_bgcolor='white',
    hovermode='closest',
)

#-------------------------
scatterChart = html.Div([
     # home page text
    html.Div(),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Dash Plotly', href="/simple-chart", className='el'),
                dcc.Link('2D-Histogram', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
                  dcc.Link('Dot Chart', href="/dot-chart", className='el'),
                dcc.Link('Line Chart', href="/line2-chart", className='el'),
            ],className='listInside')
        ],
        className='col-3 listContainer bg-light'),
        html.Div([
            html.Div([
                html.Div('Scatter chart', className='title'),
                dcc.Link('Home Page', href="/"),
            ], className='fl'),
            html.Div([
                 html.Span('Mô tả:', className='introMatplotlib'),
                html.Span('Biểu đồ phân tán trong tiếng Anh là Scatter diagram. Biểu đồ phân tán thực chất là một đồ thị biểu hiện mối tương quan giữa nguyên nhân và kết quả hoặc giữa các yếu tố ảnh hưởng đến chất lượng.',className='content')
            ]),
            html.Div([
                 html.Span('Sử dụng khi nào?:', className='introMatplotlib'),
                html.Span('Scatter chart (biểu đồ phân tán) thường được sử dụng để thể hiện mối tương quan giữa các yếu tố trên đồ thị. ',className='content')
            ]),
            html.Div([
                 html.Span('Type of charts:', className='introMatplotlib'),
            ]),
            html.Div([
                html.Div('Type 1:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure=scatt_char_01), className='col-12'
                )
            ], className='row'),

             html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure=scatt_char_02), className='col-12'
                )
            ], className='row'),
html.Span('---- Sử dụng chức năng Zoom trên thanh công cụ để xem chi tiết hơn ---- ',className='content')
            ], className='col-8 matplotlib bg-light'),
            
    

    ], className = 'row cc')
], className='container cc')
##=====================================================================
k=0
h=0

Bang=df_s
THB=beds
PII=ICUbeds
THB[2]
for i in range(52):
    THB[i]=THB[i]+k
    k=THB[i]
    PII[i]=PII[i]+h
    h=PII[i]
line_char_01 = go.Figure()
line_char_01.add_trace(go.Scatter(x=Bang, y=THB, name='Giường Phổ Thông',
                         line=dict(color='firebrick', width=4)))
line_char_01.add_trace(go.Scatter(x=Bang, y=PII, name='Giường ICU',
                         line=dict(color='Blue', width=4)))
line_char_01.update_layout(title='Sơ đồ tần số tích luỹ của số giường bệnh phổ thông và giường đạt chuẩn ICU',
                   xaxis_title='State',
                   yaxis_title='Giường')

##line2char
df=pd.DataFrame(data, columns=['State','Adult Population','Population 65+'])
Bang=np.array(df['State'])
THB=np.array(df['Adult Population'])
PII=np.array(df['Population 65+'])
line02 = go.Figure()
line02.add_trace(go.Scatter(x=Bang, y=THB, name='Người trưởng thành',
                         line=dict(color='firebrick', width=4)))
line02.add_trace(go.Scatter(x=Bang, y=PII, name='người già',
                         line=dict(color='Blue', width=4)))
line02.update_layout(title='Biểu đồ ',
                   xaxis_title='State',
                   yaxis_title='Người')

#_________________________

line2Chart = html.Div([
    # home page text
    html.Div(
    ),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Dash Plotly', href="/simple-chart", className='el'),
                dcc.Link('2D-Histogram', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
                dcc.Link('Dot Chart', href="/dot-chart", className='el'),
                dcc.Link('Line Chart', href="/line2-chart", className='el'),
            ], className='listInside')
        ],
            className='col-3 listContainer bg-light'),
        html.Div([
            html.Div([
                html.Div('2D-Histogram', className='title'),
                dcc.Link('Home Page', href="/"),
            ], className='fl'),
            html.Div([
                html.Span('Mô tả:', className='introMatplotlib'),
                html.Span(
                    'Đây là dạng biểu đồ để thể hiện tiến trình phát triển, động thái phát triển của một đối tượng hay một nhóm đối tượng nào đó qua thời gian. Vì vậy với các bài vẽ biểu đồ đường thường có các cụm từ thể hiện sự phát triển, tốc độ tăng trưởng… với các mốc thời gian nhất định. ',
                    className='content')
            ]),
            html.Div([
                html.Span('Sử dụng khi nào?:', className='introMatplotlib'),
                html.Span(
                    '2D-Histogram (biểu đồ đường): được sử dụng khi dữ liệu được mô tả phụ thuộc vào thời gian với trục hoành biểu diễn thời gian và trục tung biểu diễn đại lượng.',
                    className='content')
            ]),
            html.Div([
                html.Span('Type of charts:', className='introMatplotlib')
            ]),
            html.Div([
                html.Div('Type 1:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure=line_char_01), className='col-12'
                )
            ], className='row'),

            html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure=line02), className='col-12'
                )
            ], className='row'),

        ], className='col-8 matplotlib bg-light'),
    ], className='row cc')
], className='container cc')

# ##-----------------------------------------------------
##-----------------------------------------------------
##dot chart
df= pd.DataFrame(data, columns=['State','Hospital Bed Occupancy Rate','ICU Bed Occupancy Rate'])
df_State=[]
df1=np.array(df['State'])
for i in df1:
    df_State.append(i)
df_H=[]
df2= np.array(df['Hospital Bed Occupancy Rate']*100,int)
for i in df2:
    df_H.append(i)
df_ICU=[]
df3= np.array(df['ICU Bed Occupancy Rate']*100,int)
for i in df3:
    df_ICU.append(i)
l = len(df_ICU)
df = pd.DataFrame(dict(Bang=df_State*2, beds=df_H + df_ICU,
                       bed_kind=["Hospital Bed Occupancy Rate"]*l + ["ICU Bed Occupancy Rate"]*l))

# Use column names of df for the different parameters x, y, color, ...
dot_char_01 = px.scatter(df, x="beds", y="Bang", color="bed_kind",
                 title="Biểu đồ biểu diễn tỉ lệ phủ đầy giường",
                 labels={"beds":"Tỉ lệ phủ đầy(phần trăm)"} # customize axis label
                )

dot_char_01.show()
# biểu đồ cho ta thấy tỉ lệ lấp đầy giường chiếm tỉ lệ rất cao từ 50% -80%, như vậy số giường hiện có
#sử dụng để chữa bệnh đang dần hết và nếu bệnh dịch diễn biến phức tạp hơn thì khả năng đáp ứng giường bệnh
# là không có, do đó cần phải tăng cường thêm các giường bệnh giã chiến để phục vụ việc khám và chữa
# hầu hết tại các bang đều cảnh báo về số bệnh nhân mắc mới và giường bệnh.



#--------
#--------


#------------------------------------------------------
dotChart = html.Div([
     # home page text
    html.Div(),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Dash Plotly', href="/simple-chart", className='el'),
                dcc.Link('2D-Histogram', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
                dcc.Link('Dot Chart', href="/dot-chart", className='el'),
                dcc.Link('Line Chart', href="/line2-chart", className='el'),
            ],className='listInside')
        ],
        className='col-3 listContainer bg-light'),
        html.Div([
            html.Div([
                html.Div('Dot chart', className='title'),
                dcc.Link('Home Page', href="/"),
            ], className='fl'),
            html.Div([
                 html.Span('Mô tả:', className='introMatplotlib'),
                html.Span('Dot chart (biểu đồ chấm) là một dạng biểu đồ phân tán (Scatter chart) thể hiện sự khác biệt giữa hai hoặc nhiều Type dữ liệu trong cùng một thời điểm hoặc giữa hai hay nhiều điều kiện (condition). Hãy so sánh với Biểu đồ cột (Bar chart), biểu đồ chấm (dot chart) dễ nhìn hơn và cho phép người phân tích dễ dàng so sánh các Type dữ liệu.  ',className='content')
            ]),
            html.Div([
                 html.Span('Sử dụng khi nào?:', className='introMatplotlib'),
                html.Span('Dot chart (biểu đồ chấm) sử dụng khi so sánh dữ liệu phân Type trong cùng một thời gian.',className='content')
            ]),
            html.Div([
                 html.Span('Type of charts:', className='introMatplotlib')
            ]),
            html.Div([
                html.Div('Type 1:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure=dot_char_01), className='col-12'
                )
            ], className='row'),

             html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure=fig), className='col-12'
                )
            ], className='row'),  
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')

##---------------------------------------------------------
DataAnalysis = html.Div([
     # home page text
    html.Div(),
    html.Div([
        html.Div([
            html.Div([
                html.Div('Data Analysis', className='title'),
                dcc.Link('Home Page', href="/"),
            ], className='fl'),
            html.Div([
                 html.Span('- Dữ liệu thu thập được:', className='introMatplotlib'),
                 html.Div('dữ liệu thứ cấp',className='content')
            ]),
             html.Div([
                 html.Span('- Định nghĩa các biến số:', className='introMatplotlib'),
                 html.Div('gss_code: (Government Statistical Service code): mã dịch vụ thống kê của chính phủ',className='content'),
                 html.Div('component: dân số',className='content'),
                 html.Div('year: năm',className='content'),
                 html.Div('Births:  sinh',className='content'),
                 html.Div('Deaths: tử',className='content'),
                 html.Div('international_in: nhập cư',className='content'),
                 html.Div('international_out: xuất cư',className='content'),
                 html.Div('domestic_in: trong nước',className='content'),
                 html.Div('domestic_out: ngoài nước',className='content'),
                 html.Div('district: thành phố',className='content'),
                 html.Div('sex: giới tính',className='content'),
                 html.Div('age: tuổi',className='content'),
                 html.Div('2010, 2011,... 2050: các năm dự đoán',className='content'),     
            ]),
             html.Div([
                 html.Span('- Dạng dữ liệu:', className='introMatplotlib'),
                 html.Div('Định tính: sex, district, component ',className='content'),
                 html.Div('Định lượng: age, 2010, 2011, … 2050, year, births, deaths, international_in, international_out, domestic_in, domestic_out',className='content'),
            ]),
             html.Div([
                 html.Span('- Thang do cho dữ liệu: ', className='introMatplotlib'),
                 html.Div('Thang do định danh (norminal): district, sex, component ',className='content'),
                html.Div('Thang đo khoảng( (interval): 2010, 2011,… 2050 ,year, births, deaths, international_in, international_out, domestic_in, domestic_out ',className='content')
            ]),
             html.Div([
                 html.Span('Kiểu dữ liệu: ', className='introMatplotlib'),
                 html.Div('String: District, component,sex. ',className='content'),
                 html.Div('Integer: Age. ',className='content'),
                 html.Div('Decimal: 2010, 2011, 2012,.. 2050 year, births, deaths, international_in, international_out, domestic_in, domestic_out ',className='content'),
            ]),
             html.Div([
                 html.Span('Mục tiêu nghiên cứu: ', className='introMatplotlib'),
                 html.Div('nghiên cứu về dân số cùa thành phố london cùng với các thành phố khác trong khu vực và dự đoán dân số. ',className='content')
            ]),
             html.Div([
                 html.Span('Phạm vi nghiên cứu:', className='introMatplotlib'),
                 html.Div('10 năm sau ( 2020 -> 2031 ).',className='content')
            ]),
             html.Div([
                 html.Span('Nhóm biến tham gia quá trình nghiên cứu:', className='introMatplotlib'),
                 html.Div('district, sex, age, 2020,… 2031, births, deaths ',className='content')
            ])
        ],className='col-12 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')



##---------------------------------------------------------
# and this code to transfer to another link
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/simple-chart':
        return simpleChart
    elif pathname == '/line-chart':
        return lineChart
    elif pathname == '/line2-chart':
        return line2Chart
    elif pathname =='/bar-chart':
        return barChart
    elif pathname =='/pie-chart':
        return pieChart
    elif pathname =='/scatter-chart':
        return scatterChart
    elif pathname =='/dot-chart':
        return dotChart
    elif pathname =='/data-analysis':
        return DataAnalysis
    else:
        return main

server = app.server

if __name__ == "__main__":
    app.run_server()
