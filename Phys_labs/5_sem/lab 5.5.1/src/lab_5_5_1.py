import plotly
import pandas as pd
import plotly.express as px

x_name = "d, cm"
x_err_name = "\sigma_{d}, см"

y_name2 = "ln(N_0/N)"
y_err_name2 = "\sigma_{ln(N_0/N)}"

lab_name = "lab_5_5_1.xlsx"
sheets_list = [("Лист4", "алюминий"), ("Лист5", "свинец"), ("Лист6", "железо")]


for sheets_it in sheets_list:

    sh      = sheets_it[0]
    sh_desc = sheets_it[1]

    data = pd.read_excel(lab_name, sheet_name=sh)

    x_data = data[x_name]
    y_data = data[y_name2]

    x_err = data[x_err_name]
    y_err = data[y_err_name2]

    fig = px.scatter(x=x_data, y=y_data, error_x=x_err,
                 error_y=y_err, trendline="ols", title=sh_desc)

    fig.update_xaxes(title_text="d, см")
    fig.update_xaxes(title_font=dict(size=18))

    fig.update_yaxes(title_text="ln(N_0/N)")
    fig.update_yaxes(title_font=dict(size=18))

    fig.show()

