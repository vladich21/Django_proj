import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import requests
import pandas as pd

# Инициализация Dash-приложения
app = dash.Dash(__name__)

@app.callback(
    dash.dependencies.Output('role-chart', 'figure'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_role_chart(n):
    try:
        # Ваш API URL
        api_url = "https://legendary-carnival-gp75wwr5xx5cwv5j-8000.app.github.dev/api/users/"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)

            # Подсчитываем количество пользователей по ролям
            role_counts = df['role'].value_counts().reset_index()
            role_counts.columns = ['Роль', 'Количество']

            # Строим график
            fig = px.bar(role_counts, x='Роль', y='Количество', title='Распределение пользователей по ролям',
                         color='Роль', text_auto=True)

            return fig
        else:
            return px.bar(title="Ошибка загрузки данных")
    except Exception as e:
        return px.bar(title=f"Ошибка: {str(e)}")

# Делаем график доступным для отображения в Dash
app.layout = html.Div([
    dcc.Graph(id='role-chart'),
    dcc.Interval(
        id='interval-component',
        interval=60*1000,  # Обновление каждую минуту
        n_intervals=0
    )
])

if __name__ == '__main__':
    app.run(debug=True)
