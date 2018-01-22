from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    with open('static/drugs.json') as demographics_data:
        counties = json.load(demographics_data)
    if 'State' in request.args:
        selected_state = request.args["State"]
        return render_template('home.html', response_options = get_state_options(counties), percentOver65 = percentOver65(counties, selected_state), response_state = selected_state)
    return render_template('home.html', response_options = get_state_options(counties))

def get_state_options(counties):
    states = []
    options = ""
    for c in counties:
        if c["State"] not in states:
            states.append(c["State"])
            options += Markup("<option value=\"" + c["State"] + "\">" + c["State"] + "</option>")
    return options

def percentOver65(counties, selected_state):
    percentOver65 = 0
    for c in counties:
        if c["State"] == selected_state:
            percentOver65 = c["Dependence Past Year"]["18-25"]
    return str(percentOver65)

if __name__=="__main__":
    app.run(debug=False, port=54321)
