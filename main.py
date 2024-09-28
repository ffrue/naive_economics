from flask import Flask, render_template, request, send_file, jsonify
import pandas as pd
import MySQLdb
from build_your_mu import mu_diagram
from balances_map import balances_map
from efficient_unemployment import efficient_unemployment
from eurozone_assembly import eurozone_assembly_sunburst
from gdp_decomposition import figure_annual, figure_decade

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/area51")
def area51():
    return render_template("area51.html")

@app.route("/email", methods=['GET', 'POST'])
def email():
    db = MySQLdb.connect('flofrue.mysql.pythonanywhere-services.com', 'flofrue', 'subscribers', 'flofrue$naive-economics')
    cur = db.cursor()
    cur.execute("INSERT INTO subscribers (email) VALUES (%s)",[request.form['email']])
    db.commit()
    db.close()
    return render_template("email.html")

@app.route("/about-me")
def about():
    return render_template("about-me.html")

@app.route("/articles")
def articles():
    return render_template("articles.html")

@app.route("/models")
def models():
    return render_template("models.html")

@app.route("/datawork")
def datawork():
    return render_template("dashboard.html")



# Articles

@app.route("/wirtschaft-naiv-denken")
def wirtschaft_naiv_denken():
    return render_template("/articles/wirtschaft-naiv-denken.html")

@app.route("/the-euro")
def the_euro():
    return render_template("/articles/the-euro.html")

@app.route("/learning-from-econ-academia")
def learning_from_econ_academia():
    return render_template("/articles/learning-from-econ-academia.html")

@app.route("/stopping-the-swing")
def stopping_the_swing():
    return render_template("/articles/stopping-the-swing.html")

@app.route("/understanding-mmt-through-models")
def understanding_mmt_through_models():
    return render_template("/articles/understanding-mmt-through-models.html")

@app.route("/garantien-statt-verunsicherung")
def garantien_statt_verunsicherung():
    return render_template("/articles/garantien-statt-verunsicherung.html")

@app.route("/projekt-cybersyn")
def projekt_cybersyn():
    return render_template("/articles/projekt-cybersyn.html")

@app.route("/unattraktivster-sixpack-der-welt")
def unattraktivster_sixpack_der_welt():
    return render_template("/articles/unattraktivster-sixpack-der-welt.html")

@app.route("/fiscal-policy-in-a-sfc-model")
def fiscal_policy_in_a_sfc_model():
    return render_template("/articles/fiscal-policy-in-a-sfc-model.html")

@app.route("/ideengeschichte-der-vwl")
def ideengeschichte():
    return render_template("/articles/ideengeschichte-der-vwl.html")

@app.route("/neue-finanzpolitik-europa")
def neue_finanzpolitik_europa():
    return render_template("/articles/neue-finanzpolitik-europa.html")

@app.route("/das-ende-des-kapitalismus")
def das_ende_des_kapitalismus():
    return render_template("/articles/das-ende-des-kapitalismus.html")

@app.route("/investment-needs-green-transition")
def investment_needs_green_transition():
    return render_template("/articles/investment-needs-green-transition.html")

@app.route("/fiscalflation")
def fiscalflation():
    return render_template("/articles/fiscalflation.html")
@app.route("/fiscalflation-download")
def download_fiscalflation():
    return send_file("/home/flofrue/mysite/static/fiscalflation.zip", as_attachment=True)

@app.route("/kommunale-finanzen")
def kommunale_finanzen():
    return render_template("/articles/kommunale-finanzen.html")

@app.route("/goldene-regel")
def goldene_regel():
    return render_template("/articles/goldene-regel.html")

# Datawork

@app.route("/growth-decomposition", methods=['GET', 'POST'])
def growth_decomposition():
    annual_data = pd.read_csv("/home/flofrue/mysite/static/gdp_growth_annual.csv")
    decade_data = pd.read_csv("/home/flofrue/mysite/static/gdp_growth_decades.csv")

    if request.method == 'POST':
        input_button = request.form['submit_button']
        if input_button[0] == '1':
            decade = input_button
            c='Germany'
        elif input_button[0] == '2':
            decade = input_button
            c='Germany'
        else:
            decade = '2010s'
            c = input_button
        code_decade = figure_decade(decade_data=decade_data,decade=decade)
        code_annual = figure_annual(annual_data=annual_data,c=c)
    else:
        code_decade = figure_decade(decade_data=decade_data,decade='2010s')
        code_annual = figure_annual(annual_data=annual_data,c='Germany')
    return render_template("/datawork/gdp_decomposition.html", code_decade=code_decade, code_annual=code_annual)

@app.route("/build-your-mu", methods=['GET', 'POST'])
def diagram():
    data = pd.read_csv("/home/flofrue/mysite/static/data-build-your-mu.csv")
    selected_raw = []
    if request.method == 'POST':
        for i in range(1,25):
            selected_raw.append(request.form.get(str("cntry" + str(i))))
        countries = list(filter(None,selected_raw))
        if len(countries) > 1:
            code = mu_diagram(data=data,selected=countries,measure="gap_potential")
    else:
        countries = ['Belgium','Germany','Estonia','Ireland','Greece','Spain','France','Italy','Cyprus','Latvia',
                    'Lithuania','Luxembourg','Malta','Netherlands','Austria','Portugal','Slovenia','Finland']
        code = mu_diagram(data=data, selected=countries, measure="gap_potential")
    return render_template("/datawork/build-your-mu.html", code=code)

@app.route("/balances-map", methods=['GET', 'POST'])
def map():
    data = pd.read_csv("/home/flofrue/mysite/static/data-balances-map.csv")
    selected_raw = []
    year = 2019
    if request.method == 'POST':
        for i in range(1,28):
            selected_raw.append(request.form.get(str("cntry" + str(i))))
        countries = list(filter(None,selected_raw))
        year = int(request.form.get("mapyear"))
        code = balances_map(data=data,countries=countries,year=year)
    else:
        countries = ['Germany','Greece','France','Italy','Netherlands','Spain']
        code = balances_map(data=data,countries=countries,year=2019)
    return render_template("/datawork/balances_map.html", code=code)

@app.route("/efficient-unemployment", methods=['GET', 'POST'])
def unemployment_gap():
    data = pd.read_csv("/home/flofrue/mysite/static/data-efficient-employment.csv")
    if request.method == 'POST':
        country = request.form['submit_button']
        code = efficient_unemployment(data=data,country=country)
    else:
        code = efficient_unemployment(data=data,country='Germany')
    return render_template("/datawork/efficient-unemployment.html", code=code)

@app.route("/eurozone-assembly")
def eurozone_assembly():
    data = pd.read_csv("/home/flofrue/mysite/static/eurozone-assembly.csv")
    code = eurozone_assembly_sunburst(data=data)
    return render_template("/datawork/eurozone-assembly.html", code=code)


# Models

@app.route("/micro-macro-elasticities")
def micro_macro_elasticities():
    return render_template("/models/micro-macro-elasticities.html")

@app.route("/michaillat-saez")
def michaillat_saez():
    return render_template("/models/michaillat-saez.html")


# Notes

