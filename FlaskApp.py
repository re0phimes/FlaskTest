from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
import pandas as pd
from flask_nav import Nav
from flask_nav.elements import *

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TESTING'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
Bootstrap(app)


# nav = Nav()
# nav.register_element('top',
#                      Navbar(u'测试部',View(u'主页','Home'),
#                             View(u'测试','Test'),
#                             Subgroup(u'项目',
#                                      View(u'项目1','ProgramA'),
#                                      Separator(),
#                                      View(u'项目2','ProgramB')
#                             )),
#                      )#设置nav内容
# nav.init_app(app) #初始化nav实例


@app.route('/')
def index():
    return render_template("index.html", headers=headers, count=count, content=content)


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)



content = pd.read_csv("static/aaa.csv", index_col=0)
headers = content.columns
for header in headers:
    print(header)
count = content.count()[0]
# print(content)

if __name__ == "__main__":
    app.run(debug=True)

