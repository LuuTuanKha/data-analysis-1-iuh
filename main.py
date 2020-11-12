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
df_pop_london = pd.read_excel('./central_trend_2017_base.xlsx')
df_pop_london_10y_later = df_pop_london[['district', 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028,2029,2030]].query('district == "London"')
london_y1, london_y2, london_y3, london_y4, london_y5, london_y6, london_y7, london_y8, london_y9, london_y10,london_y11  = df_pop_london_10y_later[2020].sum(),df_pop_london_10y_later[2021].sum(), df_pop_london_10y_later[2022].sum(), df_pop_london_10y_later[2023].sum(), df_pop_london_10y_later[2024].sum(), df_pop_london_10y_later[2025].sum(), df_pop_london_10y_later[2026].sum(), df_pop_london_10y_later[2027].sum(), df_pop_london_10y_later[2028].sum(), df_pop_london_10y_later[2029].sum(),df_pop_london_10y_later[2030].sum()
arrLondonYear = np.arange(2020, 2031, 1)
arrLondonPop = [london_y1, london_y2, london_y3, london_y4, london_y5, london_y6, london_y7, london_y8, london_y9, london_y10,london_y11]
# London_10_year_fig = px.line( x=arrLondonYear, y=arrLondonPop,title='Population of London 10 years later')

#####

main = html.Div([
    # home page text
    html.Div('This is project of our team with Dash - plotly ', style={
        'height': '50px',
        'width': '100%',
        'backgroundColor': '#f5f5f5',
        'paddingLeft': '25px',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'display': 'flex',
        'alignItems': 'center'
    }),
    html.Div('Home page', style={
        'fontSize': '50px',
        'color': 'white',
        'textAlign': 'center'
    }),
    # link to another page
    html.Div([
        dcc.Link('Simple Chart', href='/simple-chart', style={
             'color': '#f5f5f5'
             }),
        dcc.Link('Data Analysis', href='/data-analysis', style={
            'color': '#f5f5f5'
        })
    ], style={
        'display': 'flex',
        'justify-content': 'space-evenly',

    }, className='mt-4'),

    # introduce tag
    html.Div([
        html.Div([
            html.Div('Giới thiệu về project: ', style={
                'fontSize': '25px',
                'fontWeight': 'bold',
            }),
            html.Div([
                html.Div( [
                    html.Div('- London population prediction (Dự đoán dân số london): nghiên cứu và dự đoán về sự gia tăng dân số của thành phố London (Anh - UK) cùng các vấn đề về dân số liên quan khác trong tương lai gần.'),
                    html.Div('- Project này sử dụng Framework Dash - Plotly để xây dựng và dữ liệu được lấy từ trang data.world để phân tích')
                ],className='col-8'),
                html.Img(src='./assets/pop.jpg', className='col-4')

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
                html.Img(src='./assets/team.jpg', className='col-4'),
                html.Div([
                html.Div('18081331 - Nguyễn Công Thành Đạt'),
                html.Div('18089811 - Mai kiên cường'),
                html.Div('18084791 - Trương Công Cường'),
                html.Div('18079251 - Đỗ Tùng Dương'),   
                ],className='col-4 team'),
                 html.Div( [
                html.Div('18092791 - Hoàng Hữu Huy'),
                html.Div('18084851 - Châu Quốc An'),
                html.Div('18072661 - Lại Văn Vượng')       
                ],className='col-4'),
            ], className='row', style={ 'fontSize': '15px' })
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
        'z-index': '-999'
    }, className='bg-dark'),
     # home page text
    html.Div('This is project of our team with Dash - plotly ', style={
        'height': '50px',
        'width': '100%',
        'backgroundColor': '#f5f5f5',
        'paddingLeft': '25px',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'display': 'flex',
        'alignItems': 'center'
    }),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Dash Plotly', href="/simple-chart", className='el'),
                dcc.Link('Line Chart', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
                dcc.Link('Dot Chart', href="/dot-chart", className='el'),
            ],className='listInside')
        ],
        className='col-3 listContainer bg-light'),
        html.Div([
            html.Div([
                html.Div('Dash - plotly', className='title'),
                dcc.Link('Home Page', href="/"),
            ], className='fl'),
            html.Div([
                 html.Span('Giới thiệu về Dash - Plotly:', className='introMatplotlib'),
                html.Span('Dash là một framework mã nguồn mở dành cho xây dựng ứng dụng phân tích dữ liệu mà không cần đến Ngôn ngữ JavaScript, và nó được tích hợp với thi viện Plotly - một thư viện đồ họa. ',className='content')
            ])
           
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')

##-----------------------------------------------------

df = pd.DataFrame({'PDD': ['Pop','Pop','Pop','Pop','Pop','Pop','Pop','Pop','Pop','Pop','Pop',
                                 'Birth','Birth','Birth','Birth','Birth','Birth','Birth','Birth','Birth','Birth','Birth',
                                'Death','Death','Death','Death','Death','Death','Death','Death','Death','Death','Death'],
                   'Units': [9121350.692, 9211390.569,9298979.218,9384393.559,9467486.975,9548200.152,9626818.38,9703526.175,9778659.789,9852408.599,9924970.291,
                            127533.3476,127885.153,128324.9541,128801.6843,129233.04,129600.5457,129961.0983,130317.1128,130663.6129,131047.3682,131487.2486,
                            51176.87663,51135.29448,51177.02141,51294.318,51485.16367,51803.97713,52212.18212,52673.59493,53184.19643,53741.82139,54315.44647
],
                   'Year':[2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,
                             2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,
                             2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,]})

groups = df.groupby(by='PDD')

data = []
colors=['red', 'blue', 'green']

for group, dataframe in groups:
    dataframe = dataframe.sort_values(by=['Year'])
    trace = go.Scatter(x=dataframe.Year.tolist(), 
                       y=dataframe.Units.tolist(),
                       marker=dict(color=colors[len(data)]),
                       name=group)
    data.append(trace)

layout =  go.Layout(xaxis={'title': 'Year'},
                    yaxis={'title': 'Population'},
                    margin={'l': 40, 'b': 40, 't': 50, 'r': 50},
                    hovermode='closest')

lineChartType2 = go.Figure(data=data, layout=layout)  

##-----------------------------------------------------
# Line Chart Link
lineChart = html.Div([
     # home page text
    html.Div('This is project of our team with Dash - plotly ', style={
        'height': '50px',
        'width': '100%',
        'backgroundColor': '#f5f5f5',
        'paddingLeft': '25px',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'display': 'flex',
        'alignItems': 'center'
    }),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Dash Plotly', href="/simple-chart", className='el'),
                dcc.Link('Line Chart', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
                  dcc.Link('Dot Chart', href="/dot-chart", className='el'),
            ],className='listInside')
        ],
        className='col-3 listContainer bg-light'),
        html.Div([
            html.Div([
                html.Div('Line Chart', className='title'),
                dcc.Link('Home Page', href="/"),
            ], className='fl'),
            html.Div([
                 html.Span('Mô tả:', className='introMatplotlib'),
                html.Span('Đây là dạng biểu đồ để thể hiện tiến trình phát triển, động thái phát triển của một đối tượng hay một nhóm đối tượng nào đó qua thời gian. Vì vậy với các bài vẽ biểu đồ đường thường có các cụm từ thể hiện sự phát triển, tốc độ tăng trưởng… với các mốc thời gian nhất định. ',className='content')
            ]),
            html.Div([
                 html.Span('Sử dụng khi nào?:', className='introMatplotlib'),
                html.Span('Line chart (biểu đồ đường): được sử dụng khi dữ liệu được mô tả phụ thuộc vào thời gian với trục hoành biểu diễn thời gian và trục tung biểu diễn đại lượng.',className='content')
            ]),
            html.Div([
                 html.Span('Type of Charts:', className='introMatplotlib')
            ]),
            html.Div([
                html.Div('Type 1:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= {
                        'data' : [
                            { 'x': arrLondonYear , 'y': arrLondonPop, 'type' : 'line', 'name' : 'Line Chart'}
                        ] ,
                        'layout' : {
                            'title' : 'Population of London 10 years later',
                            'xaxis' : { 'title': 'year'},
                            'yaxis' : { 'title': 'population'}
                        }
                    }), className='col-12'
                )
            ], className='row'),

             html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= lineChartType2), className='col-12'
                )
            ], className='row'),
            
    
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')

# ##-----------------------------------------------------
# # Bar Chart Link
df_hackney = df_pop_london[['district', 2020]].query('district == "Hackney"')[[2020]].sum()
df_haringey = df_pop_london[['district', 2020]].query('district == "Haringey"')[[2020]].sum()

df_hackney_int = int(df_hackney)
df_haringey_int = int(df_haringey)
df_london_int = int(df_pop_london[['district', 2020]].query('district == "London"')[[2020]].sum())

array_pop_city = [df_hackney_int,df_haringey_int,df_london_int]
arr_3_city = ['Hackney','Haringey','London']
go3city = go.Figure([go.Bar(x=arr_3_city, y=array_pop_city, marker_color=['red','green','blue'])])

#type 2 chart
df_male_london = pd.read_excel('./central_trend_2017_base.xlsx', sheet_name=1)
df_female_london = pd.read_excel('./central_trend_2017_base.xlsx', sheet_name=2)


df_bar_male = int(df_male_london[['district', 2020]].query('district == "London"')[[2020]].sum())
df_bar_male1 = int(df_male_london[['district', 2021]].query('district == "London"')[[2021]].sum())
df_bar_male2 = int(df_male_london[['district', 2022]].query('district == "London"')[[2022]].sum())
df_bar_male3 = int(df_male_london[['district', 2023]].query('district == "London"')[[2023]].sum())
df_bar_male4 = int(df_male_london[['district', 2024]].query('district == "London"')[[2024]].sum())
df_bar_male5 = int(df_male_london[['district', 2025]].query('district == "London"')[[2025]].sum())
df_bar_male6 = int(df_male_london[['district', 2026]].query('district == "London"')[[2026]].sum())
df_bar_male7 = int(df_male_london[['district', 2027]].query('district == "London"')[[2027]].sum())
df_bar_male8 = int(df_male_london[['district', 2028]].query('district == "London"')[[2028]].sum())
df_bar_male9 = int(df_male_london[['district', 2029]].query('district == "London"')[[2029]].sum())
df_bar_male10 = int(df_male_london[['district', 2030]].query('district == "London"')[[2030]].sum())
df_bar_male11 = int(df_male_london[['district', 2031]].query('district == "London"')[[2031]].sum())

df_bar_female = int(df_female_london[['district', 2020]].query('district == "London"')[[2020]].sum())
df_bar_female1 = int(df_female_london[['district', 2021]].query('district == "London"')[[2021]].sum())
df_bar_female2 = int(df_female_london[['district', 2022]].query('district == "London"')[[2022]].sum())
df_bar_female3 = int(df_female_london[['district', 2023]].query('district == "London"')[[2023]].sum())
df_bar_female4 = int(df_female_london[['district', 2024]].query('district == "London"')[[2024]].sum())
df_bar_female5 = int(df_female_london[['district', 2025]].query('district == "London"')[[2025]].sum())
df_bar_female6 = int(df_female_london[['district', 2026]].query('district == "London"')[[2026]].sum())
df_bar_female7 = int(df_female_london[['district', 2027]].query('district == "London"')[[2027]].sum())
df_bar_female8 = int(df_female_london[['district', 2028]].query('district == "London"')[[2028]].sum())
df_bar_female9 = int(df_female_london[['district', 2029]].query('district == "London"')[[2029]].sum())
df_bar_female10 = int(df_female_london[['district', 2030]].query('district == "London"')[[2030]].sum())
df_bar_female11 = int(df_female_london[['district', 2031]].query('district == "London"')[[2031]].sum())
years = np.arange(2020, 2032, 1)
arr_bar_male = [
    df_bar_male,df_bar_male1, df_bar_male2, df_bar_male3,
    df_bar_male4, df_bar_male5, df_bar_male6,
    df_bar_male7, df_bar_male8, df_bar_male9, df_bar_male10,df_bar_male11
]
arr_bar_female= [
      df_bar_female,df_bar_female1, df_bar_female2, df_bar_female3,
    df_bar_female4, df_bar_female5, df_bar_female6,
    df_bar_female7, df_bar_female8, df_bar_female9, df_bar_female10,df_bar_female11
]

bar_type2_fig = go.Figure()
bar_type2_fig.add_trace(go.Bar(x=years,
                y=arr_bar_male,
                name='Nam',
                marker_color='rgb(55, 83, 109)'
                ))
bar_type2_fig.add_trace(go.Bar(x=years,
                y=arr_bar_female,
                name='Nữ',
                marker_color='rgb(26, 118, 255)'
                ))

bar_type2_fig.update_layout(
    title='So sánh dân sô giữa nam và nữ của thành phố London',
    xaxis_tickfont_size=14,
    xaxis = dict(
         title='Years',
        titlefont_size=16,
        tickfont_size=14,
    ),
    yaxis=dict(
        title='pop (population)',
        titlefont_size=16,
        tickfont_size=14,
        range=[4000000,5000000]
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.2, # gap between bars of adjacent location coordinates.
    bargroupgap=0.15, # gap between bars of the same location coordinate.
    height= 700
)


#---------------------------------------------
barChart = html.Div([
     # home page text
    html.Div('This is project of our team with Dash - plotly ', style={
        'height': '50px',
        'width': '100%',
        'backgroundColor': '#f5f5f5',
        'paddingLeft': '25px',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'display': 'flex',
        'alignItems': 'center'
    }),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Dash Plotly', href="/simple-chart", className='el'),
                dcc.Link('Line Chart', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
                dcc.Link('Dot Chart', href="/dot-chart", className='el'),
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
                html.Span('Dạng biểu đồ này được thể hiện động thái phát triển, so sánh tương quan về độ lớn giữa các đại lượng hoặc thể hiện một thành phần cơ cấu trong một tổng thể.',className='content')
            ]),
            html.Div([
                 html.Span('Sử dụng khi nào?:', className='introMatplotlib'),
                html.Span('Bar chart (biểu đồ cột): thường được dùng khi cần phân loại dữ liệu và so sánh độ tương quản giữa chúng ',className='content')
            ]),
            html.Div([
                 html.Span('Type of Charts:', className='introMatplotlib')
            ]),
            html.Div([
                html.Div('Type 1:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= go3city), className='col-12'
                )
            ], className='row'),

             html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= bar_type2_fig), className='col-12'
                )
            ], className='row'),
            
    
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')


##-----------------------------------------------------
## pie chart draw
##
df_compareAge2020_Pie_u18 = int(df_pop_london[['district', 'age',2020]].query('district == "London" and age < 18')[2020].sum())
df_compareAge2020_Pie_u60 = int(df_pop_london[['district', 'age',2020]].query('district == "London" and age < 60 and age >=18 ')[2020].sum())
df_compareAge2020_Pie_u90 = int( df_pop_london[['district', 'age',2020]].query('district == "London"and age < 90 and age >=60 ')[2020].sum())


pieType1Fig = go.Figure(data=[go.Pie(labels=['Trẻ em & vị thành niên', 'Người trưởng thành', 'người lớn tuổi'], values=[df_compareAge2020_Pie_u18, df_compareAge2020_Pie_u60,df_compareAge2020_Pie_u90])])
pieType1Fig.update_layout(
    title_text="Biểu đồ so sánh dân số 3 độ tuổi của thành phố london trong năm 2020 ",
    # Add annotations in the center of the donut pies.
    )


df_pop_westminster_2020  = int(df_pop_london[['district', 2020]].query('district == "Westminster"')[[2020]].sum())
df_pop_london_2020  = int(df_pop_london[['district', 2020]].query('district == "London"')[[2020]].sum())
df_pop_wandsworth_2020  = int(df_pop_london[['district', 2020]].query('district == "Wandsworth"')[[2020]].sum())
df_pop_towerHamlets_2020  = int(df_pop_london[['district', 2020]].query('district == "Tower Hamlets"')[[2020]].sum())
df_pop_havering_2020  = int(df_pop_london[['district', 2020]].query('district == "Havering"')[[2020]].sum())
df_pop_waltham_2020  = int(df_pop_london[['district', 2020]].query('district == "Waltham Forest"')[[2020]].sum())
df_pop_hillingdon_2020  = int(df_pop_london[['district', 2020]].query('district == "Hillingdon"')[[2020]].sum())
df_pop_harrow_2020  = int(df_pop_london[['district', 2020]].query('district == "Harrow"')[[2020]].sum())

labels = ['Westminster','London','Wandsworth','Tower Hamlets','Havering','Waltham Forest','Hillingdon','Harrow']
values = [df_pop_westminster_2020, df_pop_london_2020, df_pop_wandsworth_2020, df_pop_towerHamlets_2020,df_pop_havering_2020,
         df_pop_waltham_2020,df_pop_waltham_2020,df_pop_hillingdon_2020,df_pop_harrow_2020]

# Use `hole` to create a donut-like pie chart
compare_8_city_pie = go.Figure(data=[go.Pie(labels=labels, values=values,title='population' , hole=.5, pull=[0, 0.2, 0, 0,0])])
compare_8_city_pie.update_layout(
    title_text="So sánh các thành phố xung quanh london",
    # Add annotations in the center of the donut pies.
    )
##-----------------------------------------------------
## pie chart
##
pieChart = html.Div([
     # home page text
    html.Div('This is project of our team with Dash - plotly ', style={
        'height': '50px',
        'width': '100%',
        'backgroundColor': '#f5f5f5',
        'paddingLeft': '25px',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'display': 'flex',
        'alignItems': 'center'
    }),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Dash Plotly', href="/simple-chart", className='el'),
                dcc.Link('Line Chart', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
                  dcc.Link('Dot Chart', href="/dot-chart", className='el'),
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
                html.Span('Đây là dạng biểu đồ thường được dùng để vẽ các biểu đồ liên quan đến cơ cấu, tỷ lệ các thành phần trong một tổng thể chung hoặc cũng có thể vẽ biểu đồ tròn khi tỷ lệ % trong bảng số liệu cộng lại tròn 100.',className='content')
            ]),
            html.Div([
                 html.Span('Sử dụng khi nào?:', className='introMatplotlib'),
                html.Span('Pie chart (biểu đồ tròn) được sử dụng khi cần biểu diễn dữ liệu dưới dạng % ',className='content')
            ]),
            html.Div([
                 html.Span('Type of Charts:', className='introMatplotlib'),
            ]),
            html.Div([
                html.Div('Type 1:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= pieType1Fig), className='col-12'
                )
            ], className='row'),

             html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= compare_8_city_pie), className='col-12'
                )
            ], className='row'),
            
    
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')

##______________________________________________________
#scatter charts

df_scatter_citylondon = int(df_pop_london[['district', 2020]].query('district == "City of London"')[[2020]].sum())
df_scatter_BaD = int(df_pop_london[['district', 2020]].query('district == "Barking and Dagenham"')[[2020]].sum())
df_scatter_barnet = int(df_pop_london[['district', 2020]].query('district == "Barnet"')[[2020]].sum())
df_scatter_Bexley = int(df_pop_london[['district', 2020]].query('district == "Bexley"')[[2020]].sum())
df_scatter_Brent = int(df_pop_london[['district', 2020]].query('district == "Brent"')[[2020]].sum())
df_scatter_Bromley = int(df_pop_london[['district', 2020]].query('district == "Bromley"')[[2020]].sum())
df_scatter_Camden = int(df_pop_london[['district', 2020]].query('district == "Camden"')[[2020]].sum())
df_scatter_Croydon = int(df_pop_london[['district', 2020]].query('district == "Croydon"')[[2020]].sum())
df_scatter_Ealing = int(df_pop_london[['district', 2020]].query('district == "Ealing"')[[2020]].sum())
df_scatter_Enfield = int(df_pop_london[['district', 2020]].query('district == "Enfield"')[[2020]].sum())
df_scatter_Greenwich = int(df_pop_london[['district', 2020]].query('district == "Greenwich"')[[2020]].sum())
df_scatter_Hammer = int(df_pop_london[['district', 2020]].query('district == "Hammersmith and Fulham"')[[2020]].sum())
df_scatter_Haringey = int(df_pop_london[['district', 2020]].query('district == "Haringey"')[[2020]].sum())
df_scatter_Harrow = int(df_pop_london[['district', 2020]].query('district == "Harrow"')[[2020]].sum())
df_scatter_Havering = int(df_pop_london[['district', 2020]].query('district == "Havering"')[[2020]].sum())
df_scatter_Hillingdon = int(df_pop_london[['district', 2020]].query('district == "Hillingdon"')[[2020]].sum())
df_scatter_Hounslow = int(df_pop_london[['district', 2020]].query('district == "Hounslow"')[[2020]].sum())
df_scatter_Islington = int(df_pop_london[['district', 2020]].query('district == "Islington"')[[2020]].sum())
df_scatter_Kensington = int(df_pop_london[['district', 2020]].query('district == "Kensington and Chelsea"')[[2020]].sum())
df_scatter_Kingston = int(df_pop_london[['district', 2020]].query('district == "Kingston upon Thames"')[[2020]].sum())
df_scatter_Lambeth = int(df_pop_london[['district', 2020]].query('district == "Lambeth"')[[2020]].sum())
df_scatter_Lewisham = int(df_pop_london[['district', 2020]].query('district == "Lewisham"')[[2020]].sum())
df_scatter_Merton = int(df_pop_london[['district', 2020]].query('district == "Merton"')[[2020]].sum())
df_scatter_Newham = int(df_pop_london[['district', 2020]].query('district == "Newham"')[[2020]].sum())
df_scatter_Redbridge = int(df_pop_london[['district', 2020]].query('district == "Redbridge"')[[2020]].sum())
df_scatter_Richmond = int(df_pop_london[['district', 2020]].query('district == "Richmond upon Thames"')[[2020]].sum())
df_scatter_Southwark = int(df_pop_london[['district', 2020]].query('district == "Southwark"')[[2020]].sum())
df_scatter_Hamlets = int(df_pop_london[['district', 2020]].query('district == "Tower Hamlets"')[[2020]].sum())
df_scatter_Sutton = int(df_pop_london[['district', 2020]].query('district == "Sutton"')[[2020]].sum())
df_scatter_Waltham = int(df_pop_london[['district', 2020]].query('district == "Waltham Forest"')[[2020]].sum())
df_scatter_Wandsworth = int(df_pop_london[['district', 2020]].query('district == "Wandsworth"')[[2020]].sum())
df_scatter_Westminster = int(df_pop_london[['district', 2020]].query('district == "Westminster"')[[2020]].sum())
df_scatter_London = int(df_pop_london[['district', 2020]].query('district == "London"')[[2020]].sum())
yScatter_withoutLondon = [ df_scatter_citylondon, df_scatter_BaD,df_scatter_barnet,
          df_scatter_Bexley, df_scatter_Brent, df_scatter_Bromley, df_scatter_Camden, df_scatter_Croydon, 
           df_scatter_Ealing , df_scatter_Enfield, df_scatter_Greenwich, df_scatter_Hammer, df_scatter_Haringey,df_scatter_Harrow , 
            df_scatter_Havering, df_scatter_Hillingdon, df_scatter_Hounslow,df_scatter_Islington ,df_scatter_Kensington , df_scatter_Kingston,
            df_scatter_Lambeth, df_scatter_Lewisham,df_scatter_Merton ,df_scatter_Newham , df_scatter_Redbridge, df_scatter_Richmond,df_scatter_Southwark ,
           df_scatter_Hamlets , df_scatter_Sutton, df_scatter_Waltham,df_scatter_Wandsworth , df_scatter_Westminster, 
           ]

scatterWithoutLondon = go.Figure(data=go.Scatter(x=['City of London','Barking and Dagenham','Barnet','Bexley','Brent','Bromley','Camden',
                                   'Croydon','Ealing','Enfield','Greenwich','Hammersmith and Fulham','Haringey','Harrow','Havering',
                                   'Hillingdon','Hounslow','Islington','Kensington and Chelsea','Kingston upon Thames','Lambeth',
                                   'Lewisham','Merton',
                                  'Newham','Redbridge','Richmond upon Thames','Southwark','Tower Hamlets','Sutton'
                                   ,'Waltham Forest','Wandsworth','Westminster'],
                                y=yScatter_withoutLondon,
                                mode='markers',
                                marker_color=yScatter_withoutLondon,
                                marker=dict(
        size=16,
        color=np.random.randn(500), #set color equal to a variable
        colorscale='Viridis', # one of plotly colorscales
        showscale=True
    ),
                                
                                text=['City of London','Barking and Dagenham','Barnet','Bexley','Brent','Bromley','Camden',
                                   'Croydon','Ealing','Enfield','Greenwich','Hammersmith and Fulham','Haringey','Harrow','Havering',
                                   'Hillingdon','Hounslow','Islington','Kensington and Chelsea','Kingston upon Thames','Lambeth',
                                   'Lewisham','Merton',
                                  'Newham','Redbridge','Richmond upon Thames','Southwark','Tower Hamlets','Sutton'
                                   ,'Waltham Forest','Wandsworth','Westminster'])) # hover text goes here

scatterWithoutLondon.update_layout(title='Dân số tất cả thành phố trừ London')

yScatter_HaveLondon = [ df_scatter_citylondon, df_scatter_BaD,df_scatter_barnet,
          df_scatter_Bexley, df_scatter_Brent, df_scatter_Bromley, df_scatter_Camden, df_scatter_Croydon, 
           df_scatter_Ealing , df_scatter_Enfield, df_scatter_Greenwich, df_scatter_Hammer, df_scatter_Haringey,df_scatter_Harrow , 
            df_scatter_Havering, df_scatter_Hillingdon, df_scatter_Hounslow,df_scatter_Islington ,df_scatter_Kensington , df_scatter_Kingston,
            df_scatter_Lambeth, df_scatter_Lewisham,df_scatter_Merton ,df_scatter_Newham , df_scatter_Redbridge, df_scatter_Richmond,df_scatter_Southwark ,
           df_scatter_Hamlets , df_scatter_Sutton, df_scatter_Waltham,df_scatter_Wandsworth , df_scatter_Westminster, df_scatter_London
           ]

yScatter_HaveLondon = go.Figure(data=go.Scatter(x=['City of London','Barking and Dagenham','Barnet','Bexley','Brent','Bromley','Camden',
                                   'Croydon','Ealing','Enfield','Greenwich','Hammersmith and Fulham','Haringey','Harrow','Havering',
                                   'Hillingdon','Hounslow','Islington','Kensington and Chelsea','Kingston upon Thames','Lambeth',
                                   'Lewisham','Merton',
                                  'Newham','Redbridge','Richmond upon Thames','Southwark','Tower Hamlets','Sutton'
                                   ,'Waltham Forest','Wandsworth','Westminster','london'],
                                y=yScatter_HaveLondon,
                                mode='markers',
                                marker_color=yScatter_HaveLondon,                              
                                text=['City of London','Barking and Dagenham','Barnet','Bexley','Brent','Bromley','Camden',
                                   'Croydon','Ealing','Enfield','Greenwich','Hammersmith and Fulham','Haringey','Harrow','Havering',
                                   'Hillingdon','Hounslow','Islington','Kensington and Chelsea','Kingston upon Thames','Lambeth',
                                   'Lewisham','Merton',
                                  'Newham','Redbridge','Richmond upon Thames','Southwark','Tower Hamlets','Sutton'
                                   ,'Waltham Forest','Wandsworth','Westminster','london'])) # hover text goes here

yScatter_HaveLondon.update_layout(title='Dân số tất cả thành phố')



#-------------------------
scatterChart = html.Div([
     # home page text
    html.Div('This is project of our team with Dash - plotly ', style={
        'height': '50px',
        'width': '100%',
        'backgroundColor': '#f5f5f5',
        'paddingLeft': '25px',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'display': 'flex',
        'alignItems': 'center'
    }),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Dash Plotly', href="/simple-chart", className='el'),
                dcc.Link('Line Chart', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
                  dcc.Link('Dot Chart', href="/dot-chart", className='el'),
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
                 html.Span('Type of Charts:', className='introMatplotlib'),
            ]),
            html.Div([
                html.Div('Type 1:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= scatterWithoutLondon), className='col-12'
                )
            ], className='row'),

             html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= yScatter_HaveLondon), className='col-12'
                )
            ], className='row'),
            
    
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')


##-----------------------------------------------------
##dot chart


u18_dot_2020 = int(df_pop_london[['district', 'age',2020]].query('district == "London" and age < 18')[2020].sum())
u18_dot_2021 = int(df_pop_london[['district', 'age',2021]].query('district == "London" and age < 18')[2021].sum())
u18_dot_2022 = int(df_pop_london[['district', 'age',2022]].query('district == "London" and age < 18')[2022].sum())
u18_dot_2023 = int(df_pop_london[['district', 'age',2023]].query('district == "London" and age < 18')[2023].sum())
u18_dot_2024 = int(df_pop_london[['district', 'age',2024]].query('district == "London" and age < 18')[2024].sum())
u18_dot_2025 = int(df_pop_london[['district', 'age',2025]].query('district == "London" and age < 18')[2025].sum())
u18_dot_2026 = int(df_pop_london[['district', 'age',2026]].query('district == "London" and age < 18')[2026].sum())
u18_dot_2027 = int(df_pop_london[['district', 'age',2027]].query('district == "London" and age < 18')[2027].sum())
u18_dot_2028 = int(df_pop_london[['district', 'age',2028]].query('district == "London" and age < 18')[2028].sum())
u18_dot_2029 = int(df_pop_london[['district', 'age',2029]].query('district == "London" and age < 18')[2029].sum())
u18_dot_2030 = int(df_pop_london[['district', 'age',2030]].query('district == "London" and age < 18')[2030].sum())
u18_dot_2031 = int(df_pop_london[['district', 'age',2031]].query('district == "London" and age < 18')[2031].sum())

u60_dot_2020 = int(df_pop_london[['district', 'age',2020]].query('district == "London" and age < 60 and age >=18 ')[2020].sum())
u60_dot_2021 = int(df_pop_london[['district', 'age',2021]].query('district == "London" and age < 60 and age >=18 ')[2021].sum())
u60_dot_2022 = int(df_pop_london[['district', 'age',2022]].query('district == "London" and age < 60 and age >=18 ')[2022].sum())
u60_dot_2023 = int(df_pop_london[['district', 'age',2023]].query('district == "London" and age < 60 and age >=18 ')[2023].sum())
u60_dot_2024 = int(df_pop_london[['district', 'age',2024]].query('district == "London" and age < 60 and age >=18 ')[2024].sum())
u60_dot_2025 = int(df_pop_london[['district', 'age',2025]].query('district == "London" and age < 60 and age >=18 ')[2025].sum())
u60_dot_2026 = int(df_pop_london[['district', 'age',2026]].query('district == "London" and age < 60 and age >=18 ')[2026].sum())
u60_dot_2027 = int(df_pop_london[['district', 'age',2027]].query('district == "London" and age < 60 and age >=18 ')[2027].sum())
u60_dot_2028 = int(df_pop_london[['district', 'age',2028]].query('district == "London" and age < 60 and age >=18 ')[2028].sum())
u60_dot_2029 = int(df_pop_london[['district', 'age',2029]].query('district == "London" and age < 60 and age >=18 ')[2029].sum())
u60_dot_2030 = int(df_pop_london[['district', 'age',2030]].query('district == "London" and age < 60 and age >=18 ')[2030].sum())
u60_dot_2031 = int(df_pop_london[['district', 'age',2031]].query('district == "London" and age < 60 and age >=18 ')[2031].sum())


u90_dot_2020 = int( df_pop_london[['district', 'age',2020]].query('district == "London"and age < 90 and age >=60 ')[2020].sum())
u90_dot_2021 = int( df_pop_london[['district', 'age',2021]].query('district == "London"and age < 90 and age >=60 ')[2021].sum())
u90_dot_2022 = int( df_pop_london[['district', 'age',2022]].query('district == "London"and age < 90 and age >=60 ')[2022].sum())
u90_dot_2023 = int( df_pop_london[['district', 'age',2023]].query('district == "London"and age < 90 and age >=60 ')[2023].sum())
u90_dot_2024 = int( df_pop_london[['district', 'age',2024]].query('district == "London"and age < 90 and age >=60 ')[2024].sum())
u90_dot_2025 = int( df_pop_london[['district', 'age',2025]].query('district == "London"and age < 90 and age >=60 ')[2025].sum())
u90_dot_2026 = int( df_pop_london[['district', 'age',2026]].query('district == "London"and age < 90 and age >=60 ')[2026].sum())
u90_dot_2027 = int( df_pop_london[['district', 'age',2027]].query('district == "London"and age < 90 and age >=60 ')[2027].sum())
u90_dot_2028 = int( df_pop_london[['district', 'age',2028]].query('district == "London"and age < 90 and age >=60 ')[2028].sum())
u90_dot_2029 = int( df_pop_london[['district', 'age',2029]].query('district == "London"and age < 90 and age >=60 ')[2029].sum())
u90_dot_2030 = int( df_pop_london[['district', 'age',2030]].query('district == "London"and age < 90 and age >=60 ')[2030].sum())
u90_dot_2031 = int( df_pop_london[['district', 'age',2031]].query('district == "London"and age < 90 and age >=60 ')[2031].sum())

u18_array_dot = [u18_dot_2020,u18_dot_2021,u18_dot_2022,
                u18_dot_2023,u18_dot_2024,u18_dot_2025,
                u18_dot_2026,u18_dot_2027,u18_dot_2028,
                u18_dot_2029,u18_dot_2030,u18_dot_2031]

u60_array_dot = [u60_dot_2020,u60_dot_2021,u60_dot_2022,
                u60_dot_2023,u60_dot_2024,u60_dot_2025,
                u60_dot_2026,u60_dot_2027,u60_dot_2028,
                u60_dot_2029,u60_dot_2030,u60_dot_2031]

u90_array_dot = [u90_dot_2020,u90_dot_2021,u90_dot_2022,
                u90_dot_2023,u90_dot_2024,u90_dot_2025,
                u90_dot_2026,u90_dot_2027,u90_dot_2028,
                u90_dot_2029,u90_dot_2030,u90_dot_2031]


arangeDot = np.arange(2020, 2032, 1)


dot_chart_1_fig = go.Figure()
dot_chart_1_fig.add_trace(go.Scatter(
    x=u18_array_dot,
    y=arangeDot,
    marker=dict(color="crimson", size=12),
    mode="markers",
    name="dưới 18 tuổi",
))

dot_chart_1_fig.add_trace(go.Scatter(
    x=u60_array_dot,
    y=arangeDot,
    marker=dict(color="gold", size=12),
    mode="markers",
    name="từ 18 tới 59 tuổi",
))
dot_chart_1_fig.add_trace(go.Scatter(
    x=u90_array_dot,
    y=arangeDot,
    marker=dict(color="green", size=12),
    mode="markers",
    name="từ 60 tới 90 tuổi",
))
dot_chart_1_fig.update_layout(title="Biểu đồ dự đoán 3 lứa tuổi của thành phố london trong 10 năm sau",
                  xaxis_title="population",
                  yaxis_title="years")

#--------
#--------

schools = ["2020", "2021", "2022", "2023", "2024", "2025",
           "2026", "2027", "2028", "2029", "2030",
           "2031"]
n_schools = len(schools)

men_salary = arr_bar_male
women_salary = arr_bar_female

df = pd.DataFrame(dict(year=schools*2, population=men_salary + women_salary,
                       gender=["Men"]*n_schools + ["Women"]*n_schools))

# Use column names of df for the different parameters x, y, color, ...
dot_chart_2_fig = px.scatter(df, x="population", y="year", color="gender",
                 title="Biểu đồ thể hiện sự chênh lệch giữa nam và nữ của london 10 năm sau",
                 labels="population" # customize axis label
                )
#------------------------------------------------------
dotChart = html.Div([
     # home page text
    html.Div('This is project of our team with Dash - plotly ', style={
        'height': '50px',
        'width': '100%',
        'backgroundColor': '#f5f5f5',
        'paddingLeft': '25px',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'display': 'flex',
        'alignItems': 'center'
    }),
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('Dash Plotly', href="/simple-chart", className='el'),
                dcc.Link('Line Chart', href="/line-chart", className='el'),
                dcc.Link('Bar Chart', href="/bar-chart", className='el'),
                dcc.Link('Pie Chart', href="/pie-chart", className='el'),
                dcc.Link('Scatter Chart', href="/scatter-chart", className='el'),
                dcc.Link('Dot Chart', href="/dot-chart", className='el'),
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
                html.Span('Dot chart (biểu đồ chấm) là một dạng biểu đồ phân tán (Scatter chart) thể hiện sự khác biệt giữa hai hoặc nhiều loại dữ liệu trong cùng một thời điểm hoặc giữa hai hay nhiều điều kiện (condition). Hãy so sánh với Biểu đồ cột (Bar chart), biểu đồ chấm (dot chart) dễ nhìn hơn và cho phép người phân tích dễ dàng so sánh các loại dữ liệu.  ',className='content')
            ]),
            html.Div([
                 html.Span('Sử dụng khi nào?:', className='introMatplotlib'),
                html.Span('Dot chart (biểu đồ chấm) sử dụng khi so sánh dữ liệu phân loại trong cùng một thời gian.',className='content')
            ]),
            html.Div([
                 html.Span('Type of Charts:', className='introMatplotlib')
            ]),
            html.Div([
                html.Div('Type 1:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= dot_chart_1_fig), className='col-12'
                )
            ], className='row'),

             html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure= dot_chart_2_fig), className='col-12'
                )
            ], className='row'),  
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')

##---------------------------------------------------------
DataAnalysis = html.Div([
     # home page text
    html.Div('This is project of our team with Dash - plotly ', style={
        'height': '50px',
        'width': '100%',
        'backgroundColor': '#f5f5f5',
        'paddingLeft': '25px',
        'position': 'absolute',
        'top': '0',
        'left': '0',
        'display': 'flex',
        'alignItems': 'center'
    }),
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
