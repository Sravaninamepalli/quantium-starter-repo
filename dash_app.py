import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go

# Load data
df = pd.read_csv("pink_morsel_sales.csv")
df["date"] = pd.to_datetime(df["date"])

# Price increase date
price_increase_date = pd.to_datetime("2021-01-15")

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Analysis"),

    html.Div([
        html.Label("Select Region:"),
        dcc.Dropdown(
            id="region-dropdown",
            options=[{"label": r, "value": r} for r in sorted(df["region"].unique())],
            value="north"
        )
    ]),

    dcc.Graph(id="sales-line-chart")
])

@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-dropdown", "value")
)
def update_chart(region):
    filtered_df = df[df["region"] == region]

    fig = px.line(filtered_df, x="date", y="sales",
                  title=f"Sales Over Time - {region.capitalize()} Region")

    # Add vertical line for price increase date
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
