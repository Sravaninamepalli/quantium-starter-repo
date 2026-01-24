import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("pink_morsel_sales.csv")
df["date"] = pd.to_datetime(df["date"])

# Price increase date
price_increase_date = pd.to_datetime("2021-01-15")

app = Dash(__name__, assets_folder="assets")

app.layout = html.Div([
    html.Div([
        html.H1("Pink Morsel Sales Visualiser", className="header")
    ], className="app-container"),

    html.Div([
        html.Div([
            html.Label("Select Region:", className="radio-label"),
            dcc.RadioItems(
                id="region-radio",
                options=[
                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"},
                    {"label": "All", "value": "all"}
                ],
                value="all",
                labelStyle={"display": "inline-block", "margin-right": "20px"},
                inputStyle={"margin-right": "8px"}
            )
        ], className="card"),

        html.Div([
            dcc.Graph(id="sales-line-chart")
        ], className="chart-card")

    ], className="app-container"),

    html.Div([
        html.P("Data visualization by: Your Name", className="footer")
    ], className="app-container")
])


@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-radio", "value")
)
def update_chart(region):
    if region == "all":
        filtered_df = df.copy()
    else:
        filtered_df = df[df["region"] == region]

    fig = px.line(filtered_df, x="date", y="sales",
                  title=f"Sales Over Time - {region.capitalize()} Region")

    fig.update_layout(
        plot_bgcolor="#0B1220",
        paper_bgcolor="#0B1220",
        font_color="white",
        xaxis_title="Date",
        yaxis_title="Sales ($)"
    )

    fig.add_shape(
        type="line",
        x0=price_increase_date,
        x1=price_increase_date,
        y0=0,
        y1=1,
        yref="paper",
        line=dict(color="red", dash="dash")
    )

    fig.add_annotation(
        x=price_increase_date,
        y=1,
        yref="paper",
        text="Price Increase",
        showarrow=False,
        xanchor="right",
        yanchor="bottom"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
