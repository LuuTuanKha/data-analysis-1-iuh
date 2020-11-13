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
# Change the bar mode
bar_char_01.update_layout(barmode='group',title ="Biểu đồ biểu diễn số giường bệnh cần có  trong vòng 6, 12 và 18 tháng tới tại các bang.")


## end bar char 01

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
    html.Div(
    ),
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
                    dcc.Graph(), className='col-12'
                )
            ], className='row'),

             html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    ##dcc.Graph(figure= lineChartType2), className='col-12'
                )
            ], className='row'),
            
    
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')

# ##-----------------------------------------------------
# # Bar Chart Link


#type 2 chart


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
                    dcc.Graph(figure= bar_char_01), className='col-12'
                )
            ], className='row'),
            
    
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')


##-----------------------------------------------------
## pie chart draw
##










# Use `hole` to create a donut-like pie chart

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
                    dcc.Graph(), className='col-12'
                )
            ], className='row'),

             html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(), className='col-12'
                )
            ], className='row'),
            
    
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')

##______________________________________________________
#scatter charts








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
                    dcc.Graph(), className='col-12'
                )
            ], className='row'),

             html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(), className='col-12'
                )
            ], className='row'),
            
    
        ],className='col-8 matplotlib bg-light'),
    ], className = 'row cc')
], className='container cc')


##-----------------------------------------------------
##dot chart




#--------
#--------


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
                    dcc.Graph(), className='col-12'
                )
            ], className='row'),

             html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(), className='col-12'
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
