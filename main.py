import flask
from flask_cors import CORS
from flask import Flask
from main_hw import app_hw

app = Flask(__name__)
app.register_blueprint(app_hw)
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app)

@app.route('/')
def index():
    return flask.send_from_directory('static', 'index.html')

@app.route('/demo')
def chartdemo():
    return flask.send_from_directory('static', 'demo.html')

@app.route('/barchart')
def barchart():
    return flask.send_from_directory('static', 'barchart.html')

@app.route('/barchart-tutorial')
def barcharttutorial():
    return flask.send_from_directory('static', 'd3-tutorial/barchart.html')

# 柱形图
@app.route('/baraxes')
def baraxes():
    return flask.send_from_directory('static', 'baraxes.html')

# 堆叠图
@app.route('/stack_histogram')
def stack_histogram():
    return flask.send_from_directory('static', 'stack_histogram.html')

# 散点图
@app.route('/scatter')
def scatter():
    return flask.send_from_directory('static', 'scatter.html')

# 散点图
@app.route('/scatternxt')
def scatternxt():
    return flask.send_from_directory('static', 'scatternxt.html')

# 世界地图
@app.route('/renderearth')
def renderearth():
    return flask.send_from_directory('static', 'renderearth.html')

@app.route('/rendergeojson')
def rendergeojson():
    return flask.send_from_directory('static', 'rendergeojson.html')

# 柱形图
@app.route('/barcscginteraction')
def barcscginteraction():
    return flask.send_from_directory('static', 'barcscginteraction.html')

@app.route('/nCov')
def nCov():
    return flask.send_from_directory('static', 'nCov.html')

@app.route('/nCovnxt')
def nCovnxt():
    return flask.send_from_directory('static', 'nCovnxt.html')

@app.route('/lineDiagram')
def lineDiagram():
    return flask.send_from_directory('static', 'first_lineDiagram.html')

@app.route('/nCovnxt-world')
def nCovnxtworld():
    return flask.send_from_directory('static', 'nCovnxt-world.html')

# 动态散点图
@app.route('/pie-world')
def pieworld():
    return flask.send_from_directory('static', 'Pie-world.html')

# 动态散点图
@app.route('/nCovnxt-province')
def nCovnxtprovince():
    return flask.send_from_directory('static', 'nCovnxt-province.html')

# 流图
@app.route('/themeriver')
def themeriver():
    return flask.send_from_directory('static', 'themeriver.html')

@app.route('/themeriver-lr')
def themeriverlr():
    return flask.send_from_directory('static', 'themeriver-lr.html')

@app.route('/themeriver-lr-custom')
def themeriverlrcus():
    return flask.send_from_directory('static', 'themeriver-lr-custom.html')

@app.route('/themeriver-lr-hubei')
def themeriverlrhubei():
    return flask.send_from_directory('static', 'themeriver-lr-hubei.html')

@app.route('/themeriver-lr-world')
def themeriverlrworld():
    return flask.send_from_directory('static', 'themeriver-lr-world.html')

@app.route('/colorgradient')
def colorgradient():
    return flask.send_from_directory('static', 'color-gradient.html')

@app.route('/scatter-animation')
def scatteranimation():
    return flask.send_from_directory('static', 'Scatter-Animation.html')

@app.route('/multi-channel')
def multichannel():
    return flask.send_from_directory('static', 'Multi-Channel.html')

# 纹理填充案例
@app.route('/multi-channel-texture')
def multichanneltexture():
    return flask.send_from_directory('static', 'multi-channel-texture.html')

# 折线图
@app.route('/line')
def line():
    return flask.send_from_directory('static', 'lineChart.html')

# 旭日图
@app.route('/sunburst')
def sunburst():
    return flask.send_from_directory('static', 'Sunburst.html')

# 树形柱图
@app.route('/icicle')
def icicle():
    return flask.send_from_directory('static', 'icicle.html')

# 树图
@app.route('/tree')
def tree():
    return flask.send_from_directory('static', 'tree.html')

# 力的相互作用图
@app.route('/graph')
def graph():
    return flask.send_from_directory('static', 'graph.html')

@app.route('/scatter-tutorial')
def scatter_tutorial():
    return flask.send_from_directory('static', 'd3-tutorial/scatter.html')

@app.route('/scatter-tutorial-simple')
def scatter_tutorial_simple():
    return flask.send_from_directory('static', 'd3-tutorial/scatter-simple.html')

@app.route('/static/<fname>')
def sendfile(fname):
    return flask.send_from_directory('static', fname)

# https://icon-icons.com/icon/heart-love-like-favourite-follow/131237
# https://icon-icons.com/icon/heart-love-favorite-favourite/13187
@app.route('/favicon.ico') 
def favicon(): 
    return flask.send_from_directory('static', 'loveheart.ico', mimetype='image/vnd.microsoft.icon')

app.run(host='0.0.0.0', port=11666, debug=True)
