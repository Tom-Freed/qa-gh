<h3>ERD:</h3>

![image](https://github.com/Tom-Freed/qa-gh/assets/91968539/bf86ef30-b8c4-4df6-96cd-b75760c737b1)

<h3>Jenkins:</h3>

I was unable to get Jenkins to work before the presentation, but managed to resolve the issue after the presentation

<h4>Build steps:</h4>

![image](https://github.com/Tom-Freed/qa-gh/assets/91968539/4967fdd7-5ab8-4c6b-9d75-e145108fa2f2)

<h4>Console output:</h4>

```Started by user admin
Running as SYSTEM
Building in workspace C:\Users\Tom\AppData\Local\Jenkins\.jenkins\workspace\project1
The recommended git tool is: NONE
No credentials specified
 > git.exe rev-parse --resolve-git-dir C:\Users\Tom\AppData\Local\Jenkins\.jenkins\workspace\project1\.git # timeout=10
Fetching changes from the remote Git repository
 > git.exe config remote.origin.url https://github.com/Tom-Freed/qa-gh.git # timeout=10
Fetching upstream changes from https://github.com/Tom-Freed/qa-gh.git
 > git.exe --version # timeout=10
 > git --version # 'git version 2.41.0.windows.2'
 > git.exe fetch --tags --force --progress -- https://github.com/Tom-Freed/qa-gh.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git.exe rev-parse "refs/remotes/origin/main^{commit}" # timeout=10
Checking out Revision 20124fb338b129783a79e54430456d4a485cca69 (refs/remotes/origin/main)
 > git.exe config core.sparsecheckout # timeout=10
 > git.exe checkout -f 20124fb338b129783a79e54430456d4a485cca69 # timeout=10
Commit message: "adding pytest to requirements"
 > git.exe rev-list --no-walk 20124fb338b129783a79e54430456d4a485cca69 # timeout=10
[project1] $ cmd /c call C:\Users\Tom\AppData\Local\Temp\jenkins18439838395593293080.bat
>
C:\Users\Tom\AppData\Local\Jenkins\.jenkins\workspace\project1>cd Project1 
>
C:\Users\Tom\AppData\Local\Jenkins\.jenkins\workspace\project1\Project1>pip install -r requirements.txt 
Requirement already satisfied: flask in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from -r requirements.txt (line 1)) (2.3.2)
Requirement already satisfied: flask-sqlalchemy in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from -r requirements.txt (line 2)) (3.0.5)
Requirement already satisfied: flask-wtf in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from -r requirements.txt (line 3)) (1.1.1)
Requirement already satisfied: flask-testing in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from -r requirements.txt (line 4)) (0.8.1)
Requirement already satisfied: Flask-Bcrypt in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from -r requirements.txt (line 5)) (1.0.1)
Requirement already satisfied: pytest in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from -r requirements.txt (line 6)) (7.4.0)
Requirement already satisfied: Werkzeug>=2.3.3 in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from flask->-r requirements.txt (line 1)) (2.3.6)
Requirement already satisfied: Jinja2>=3.1.2 in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from flask->-r requirements.txt (line 1)) (3.1.2)
Requirement already satisfied: itsdangerous>=2.1.2 in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from flask->-r requirements.txt (line 1)) (2.1.2)
Requirement already satisfied: click>=8.1.3 in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from flask->-r requirements.txt (line 1)) (8.1.6)
Requirement already satisfied: blinker>=1.6.2 in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from flask->-r requirements.txt (line 1)) (1.6.2)
Requirement already satisfied: sqlalchemy>=1.4.18 in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from flask-sqlalchemy->-r requirements.txt (line 2)) (2.0.19)
Requirement already satisfied: WTForms in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from flask-wtf->-r requirements.txt (line 3)) (3.0.1)
Requirement already satisfied: bcrypt>=3.1.1 in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from Flask-Bcrypt->-r requirements.txt (line 5)) (4.0.1)
Requirement already satisfied: iniconfig in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from pytest->-r requirements.txt (line 6)) (2.0.0)
Requirement already satisfied: packaging in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from pytest->-r requirements.txt (line 6)) (23.1)
Requirement already satisfied: pluggy<2.0,>=0.12 in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from pytest->-r requirements.txt (line 6)) (1.2.0)
Requirement already satisfied: colorama in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from pytest->-r requirements.txt (line 6)) (0.4.6)
Requirement already satisfied: MarkupSafe>=2.0 in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from Jinja2>=3.1.2->flask->-r requirements.txt (line 1)) (2.1.3)
Requirement already satisfied: typing-extensions>=4.2.0 in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from sqlalchemy>=1.4.18->flask-sqlalchemy->-r requirements.txt (line 2)) (4.7.1)
Requirement already satisfied: greenlet!=0.4.17 in c:\users\tom\appdata\local\programs\python\python311-32\lib\site-packages (from sqlalchemy>=1.4.18->flask-sqlalchemy->-r requirements.txt (line 2)) (2.0.2)

[notice] A new release of pip is available: 23.1.2 -> 23.2.1
[notice] To update, run: python.exe -m pip install --upgrade pip

C:\Users\Tom\AppData\Local\Jenkins\.jenkins\workspace\project1\Project1>set DATABASE_URI=mysql+pymysql://root:pass@localhost/project1 

C:\Users\Tom\AppData\Local\Jenkins\.jenkins\workspace\project1\Project1>python -m pytest --cov=app --cov-report term-missing 
============================= test session starts =============================
platform win32 -- Python 3.11.4, pytest-7.4.0, pluggy-1.2.0
rootdir: C:\Users\Tom\AppData\Local\Jenkins\.jenkins\workspace\project1\Project1
plugins: cov-4.1.0
collected 10 items

tests\test_app.py ..........                                             [100%]

============================== warnings summary ===============================
..\..\..\..\..\Programs\Python\Python311-32\Lib\site-packages\flask_wtf\recaptcha\widgets.py:2
..\..\..\..\..\Programs\Python\Python311-32\Lib\site-packages\flask_wtf\recaptcha\widgets.py:2
  C:\Users\Tom\AppData\Local\Programs\Python\Python311-32\Lib\site-packages\flask_wtf\recaptcha\widgets.py:2: DeprecationWarning: 'flask.Markup' is deprecated and will be removed in Flask 2.4. Import 'markupsafe.Markup' instead.
    from flask import Markup

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html

---------- coverage: platform win32, python 3.11.4-final-0 -----------
Name     Stmts   Miss  Cover   Missing
--------------------------------------
app.py     149     31    79%   134-139, 144-154, 169-177, 189, 198-210, 233
--------------------------------------
TOTAL      149     31    79%

======================= 10 passed, 2 warnings in 21.49s =======================

C:\Users\Tom\AppData\Local\Jenkins\.jenkins\workspace\project1\Project1>python app.py 
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.0.102:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 141-657-353
127.0.0.1 - - [16/Aug/2023 16:41:27] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [16/Aug/2023 16:41:29] "GET /products HTTP/1.1" 200 -
127.0.0.1 - - [16/Aug/2023 16:41:29] "GET /static/plant1.jpg HTTP/1.1" 304 -
127.0.0.1 - - [16/Aug/2023 16:41:31] "GET /categories HTTP/1.1" 200 -
127.0.0.1 - - [16/Aug/2023 16:41:32] "GET /basket HTTP/1.1" 200 -
127.0.0.1 - - [16/Aug/2023 16:41:33] "GET /checkout HTTP/1.1" 200 -
127.0.0.1 - - [16/Aug/2023 16:41:34] "GET /contact HTTP/1.1" 200 -
127.0.0.1 - - [16/Aug/2023 16:41:34] "GET /about HTTP/1.1" 200 -
127.0.0.1 - - [16/Aug/2023 16:41:36] "GET / HTTP/1.1" 200 -
```

<h3>Testing:</h3>

![image](https://github.com/Tom-Freed/qa-gh/assets/91968539/c4cd11ee-ac8a-4767-8335-626c2799ce53)

<h3>Still to do:</h3>

- Create individual product pages
- Create Categories page
- Create About Us page
- Improve styling
- Different images for each product
- More in depth testing
- More specific validators


