[[_TOC_]]
# pythonwebapp
Python Flask Web App

# Overview
- Build a front end in Flask
- The landing page must contain a nice display of links to child pages

---

# Source code structure

## Top level folders
- devops
- webfrontend
- 

## Detailed structure

```
---devops
    |
    |---deploy.ps1
    |
    |---armtemplates
    |        |
    |        |
    |        ----[web app, app insight, key vault, storage account perhaps]
    |
    |
---webrontend
    |
    |
    |---app.py
    |
---cicd.yml
```
---
# Next step
- ~~CICD version in template~~
- ~~bootstrap~~
- Simple dash demo 1
- Simple dash demo 2
- Simple plotly demo with  plotly .js
- Single dashboard page with narration and embedded IFRAME based charts
- Simple bootstrap form submission demo using Flask postback
- 

---

# Change the folder structure - probable idea

The basic idea 
- Mono repo approach
- Every project within the repo has its top level folder
- Every project has its own **devops** folde
- Where should you put the **app.py** file and what about **tests** folder

```
---
    |
    |
    |---webfrontend--|
    |                |
    |                |
    |                |
    |                |--devops
    |                |
    |                |
    |                |--cicd.yml
    
    |
    |
    |---sharedinfra--
    |                |
    |                |
    |                |--devops
    |                |
    |                |
    |                |--cicd.yml
    |
    |
    |---comonvariables.ps1
```
---

# Landing page
- Use bootstrap nav bar
- Have an **Abbout** page
- How was this **site constructed page** and technologies involved, ci/cd
- Plotly demo page
- **PyScript** demo page
- Links to all your articles on the landing page (link and summary)


# Challenges with Dash and integrating with Flask

## Key take aways
Dash works in a very different way to Flask. 
- **Easy** - If you want to make Dash as the primary web server
- **Not so easy** - If Flask is your primary web server and you want to have a few pages which are Dash implementation

## Lesson - Dash app should be created only once
https://community.plotly.com/t/limit-on-multiple-dash-apps-running-simultaneously/74477/7

## Lesson - Multi pages (official sample)
Demonstrates the usage of `register_page` to register multiple routes
- https://dash.plotly.com/urls

## Lesson - Another example of register_page
- https://stackoverflow.com/questions/73505769/is-it-possible-to-register-dash-pages-from-an-external-module

```
app.py
/modules
  foo.py
  home.py
```
## Reference   -Integrating Dash with Flask
https://hackersandslackers.com/plotly-dash-with-flask/
Good article and hilights some of the challenges. But,this does not use `multi pages` approach

https://github.com/tzelleke/flask-dash-app/blob/master/app/dash/demo.py
Good sample. But, this too does not use `multi pages` approach

## Dash - Basic callbacks
This is a nice demo. Restrict to single Dash instance.
https://dash.plotly.com/basic-callbacks

## Flask and Dash - integrating via IFRAME
Looks like a sensible approach to keep compexity low
https://stackoverflow.com/questions/74762322/integrating-dash-and-flask-by-inserting-dash-chart-into-div-block-of-flask-templ


## Lesson - Multiple Dash instances - What did I try in the app.py and did not owrk
This does not work. You can only create a single instance of Dash

```python
#First dash page registration
from views.dashdemo1 import make_dash, make_layout, define_callbacks
dash_app = make_dash(app)
dash_app.layout = make_layout()
define_callbacks()

#Second dash page registration
import views.dashdemo2 as dashdemo2
dashdemo2.DashDemo2.register_page()
#dashdemo2.DashDemo2.make_dash(server=app)

```

## Sample using IFRAME approach
https://towardsdatascience.com/embed-multiple-dash-apps-in-flask-with-microsoft-authenticatio-44b734f74532
This uses Bootstrap extensively. Need to read in depth

---

# Plotly Express demo code
Nice demo. This embeds a `graphJSON` variable from the route handler
https://www.geeksforgeeks.org/create-a-bar-chart-from-a-dataframe-with-plotly-and-flask/
