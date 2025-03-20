from dash import Dash, html, dcc, dash_table, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# Загружаем данные (используем локальный CSV или API)
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Создаем приложение Dash с Bootstrap
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Описание макета
app.layout = dbc.Container([
    dbc.Row([
        html.H3('Приложение Dash в микросервисе', className="text-center text-primary mb-4")
    ]),

    dbc.Row([
        dbc.Col([
            dash_table.DataTable(data=df.to_dict('records'), page_size=10, style_table={'overflowX': 'auto'})
        ], width=6),
        dbc.Col([
            dcc.Graph(id='bar-chart')
        ], width=6),
    ]),

    dbc.Row([
        dbc.Col([
            dcc.RadioItems(
                options=[{"label": x, "value": x} for x in ['pop', 'lifeExp', 'gdpPercap']],
                value='lifeExp',
                inline=True,
                id='select-metric'
            )
        ])
    ])
], fluid=True)

# Callback для обновления графика
@app.callback(
    Output('bar-chart', 'figure'),
    Input('select-metric', 'value')
)
def update_chart(selected_metric):
    fig = px.bar(df, x='continent', y=selected_metric, title="Средние показатели по континентам", barmode='group')
    return fig

# Запуск сервера
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
