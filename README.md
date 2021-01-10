# Python for Data Analysis Project
# Page Block Classification

[1 - Prerequisite](#prerequisite)  
[2 - Installation](#installation)  
[3 - Launch the application](#start)  
[4 - Architecture](#architecture) 


## <a name="prerequisite"></a>1 - Prerequisite

Check that your python version is up to date and to clone the project use this command:

```
git clone https://github.com/mounir-hammouti/python_project_DIA3.git
```

It is better to create a virtual environment for the project, so you will not encounter versioning problems. First, go into the directory where you have cloned the repository then:

```
cd python_project_DIA3
python3 -m venv .
.\Scripts\activate.bat.
```
If you are using powershell, use this command instead :
```
cd python_project_DIA3
python3 -m venv .
. .\Scripts\Activate.ps1
```
For MAC users :
```
cd python_project_DIA3
python3 -m venv .
. bin/activate
```

Note to disable the environment, use this command :
```
deactivate
```



## <a name="installation"></a>2 - Installation

After cloning the project, it is necessary to install the packages it uses:

```
 pip3 install -r requirements.txt
```

In case of problems, please refer to the [documentation].(https://pip.pypa.io/en/stable/reference/pip_install/).

Please note that we have decided to install only exact versions of the libraries in order to minimize the differences that could occur in the application.



## <a name="start"></a>3 - Launch the application

```
python3 app.py
```

This command launches the app.py file that starts a server on `http://localhost:5000`. Each change on this file leads to a new compilation and a page update in the browser. Open your browser with this url and you will have access to the Page Block Classification API.

If you are struggling with the launch of the app, maybe use conda instead of your command prompt and launch again the above command.

## <a name="architecture"></a>4 - Architecture

The project is composed of 3 main folders, the folder <b>Templates<b> for displaying the pages, the folder <b>static</b> which contains the css files for stylizing the web pages and the folder <b>model</b> which contains the prediction and the notebook file. 

![logo](https://github.com/mounir-hammouti/python_project_DIA3/blob/main/images/predictPage.png)