import plotly.express as px


def df_preparator(df):
    df = df.drop(df[df['timestep']%10 != 0].index)
    return df


year = dict(
        tick0 = 0,
        dtick = 365
    )


def linear_plot(df, _y):
    fig = px.line(
        df,
        x="timestep",
        y=_y,
        facet_col='simulation',
        template='seaborn'
    )
    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20), xaxis=year)
    fig.show()


def scatter_plot(df, _y):
    fig = px.scatter(
        df,
        x="timestep",
        y=_y,
        opacity=0.01,
        trendline="lowess",
        trendline_color_override="red",
        facet_col='simulation',
        labels={'color': _y}
    )
    fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20), xaxis=year)
    fig.show()