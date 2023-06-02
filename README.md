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
-