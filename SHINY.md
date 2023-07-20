# Interactive Analytics with Shiny

Earlier, you installed Python and verified it with:

```shell
python --version
python3 --version
py --version
```

Use the command that works instead of `python` in the following instructions. 
You're encouraged to modify these Markdown (.md) files to reflect the commands that work on your machine. 

## Install and Upgrade Python Tools Globally

Install some additional content into your global Python for best results. 
open your terminal (PowerShell on Windows, Terminal on Mac/Linux) and
install these to your default Python using the commands below. 


```shell
python -m pip install --upgrade pip wheel
python -m pip install --upgrade black ruff pyright
python -m pip install --upgrade rsconnect-python
```

You must have reconnect-python installed for the next step.

## Authorize shinyapps.io

Using Chrome (recommended), sign in to your free shinyapps.io account (I use GitHub to sign in.)

1. On the Getting Started page, click on the "Start with Python" tab. 
1. Click "Show Secret"
1. Click "Copy to Clipboard". Follow the instructions. Mine said
1. Hit Ctrl c / ENTER to copy the provided command to the clipboard. 
1. Open a terminal window. (Terminal on Mac/Linux, PowerShell on Windows).
1. Click in the terminal window to paste the command and hit ENTER to run it.

![Get the Command to Authorize shinyapps.io](images/GetCommandToAuthorizeShinyAppsdotIO.PNG)

## Create a Virtual Environment

```shell
python -m venv .venv
```

When VS Code asks if it should add the new virtual environment, click yes.


## Activate the Virtual Environment

- Activate it on Windows: `.venv\Scripts\activate`
- Activate it on macOS/Linux `source .venv/bin/`

## Install Libraries into Virtual Environment

This gives a good selection of options. You only need to install the ones you use.

```shell
python -m pip install --upgrade pip wheel
python -m pip install --upgrade -r requirements.txt
```

## Run the App

Verify your virtual environment is activated. Run the app. 

```shell
shiny run --reload app.py
```

Open the app by following the instructions provided in the terminal. 
For example, try CTRL CLICK (at the same time) on the URL displayed (http://127.0.0.1:8000).

Hit CTRL c (at the same time) to quit the app. 
If it won't stop, close the terminal window.
Reopen the terminal window and be sure the virtual environment is activated
before running the app again.

## Deploy the App

Verify repository name in .github/workflows/deploy.yml.
Login to [shinyapps.io](https://www.shinyapps.io/) then Account / Tokens to find values for 3 repo secrets.
See the earlier [SHINYAPPS.md](https://github.com/wadebryson/cintel-02-app/blob/main/SHINYAPPS.md) for details.

- Name: SHINYAPPS_ACCOUNT, Secret: Paste shinyapps.io account name
- Name: SHINYAPPS_TOKEN, Secret: (paste token )
- Name: SHINYAPPS_SECRET, Secret: (paste secret)

-----

## ⚠️ Delete Hosted App Before Pushing to GitHub

Reminder: The GitHub action deploy.yml may not automatically delete an existing app from shinyapps.io so we can redeploy.

Before pushing to GitHub, login to [shinyapps.io](https://www.shinyapps.io/) and view the list of applications. 

- First archive the app.
- Then delete the archived app.
