from datetime import datetime
import os
import cv2 as cv
import pyecharts

from pyecharts import options as opts
from pyecharts.charts import Tree
from pyecharts.charts import Bar
from pyecharts.commons import utils


def showimage():
    s = os.getcwd()
    img = cv.imread("src/images/test.jpg", 1)
    cv.namedWindow('IMG')
    cv.imshow("IMG", img)
    cv.waitKey()
    cv.destroyAllWindows()


def echar():
    # V1 版本开始支持链式调用
    bar = Bar()
    bar.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
    bar.add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
    bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
    bar.set_global_opts(title_opts=opts.TitleOpts(title="商场销售情况"))
    bar.render("outdata/sell.html")


def echar_tree():
    import time

    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    data = [{
        "children": [
            {
                "name": "dd",
                "value": localtime
            },
            {
                "children": [{
                    "children": [{
                        "name": "I"
                    }],
                    "name": "E"
                }, {
                    "name": "F",
                    "value": localtime
                }],
                "name":
                "C",
            },
            {
                "children": [
                    {
                        "children": [{
                            "name": "J"
                        }, {
                            "name": "K"
                        }],
                        "name": "G"
                    },
                    {
                        "name": "H"
                    },
                ],
                "name":
                "D",
            },
        ],
        "name":
        "A",
    }]
    ctree = Tree()
    ctree.add("", data)
    ctree.set_global_opts(title_opts=opts.TitleOpts(title="Tree-基本示例"))
    ctree.set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=True,
                                      trigger="item",
                                      trigger_on="click",
                                      is_always_show_content=True))
    ctree.render("outdata/tree_base.html")


def echar_ffbmtree():
    import time

    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    data = [{
        "children": [
            {
                "name": "github",
                "value": localtime,
                "title": "github交朋友",
                "uri": "www.github.com",
                "site": "github.com"
            },
            {
                "children": [{
                    "children": [{
                        "name": "百度",
                        "title": localtime,
                        "uri": "www.baidu.com",
                        "site": "baidu.com"
                    }],
                    "name":
                    "E"
                }, {
                    "name": "F",
                    "value": localtime
                }],
                "name":
                "C",
            },
            {
                "children": [
                    {
                        "children": [{
                            "name": "J"
                        }, {
                            "name": "K"
                        }],
                        "name": "G"
                    },
                    {
                        "name": "H"
                    },
                ],
                "name":
                "D",
            },
        ],
        "name":
        "天气网",
        "title":
        "天气网有天气",
        "uri":
        "http://www.weather.com.cn/",
        "site":
        "weather.com.cn",
        "value":
        "http://www.weather.com.cn/"
    }]
    ffbmformater = """
        function (params) {
            if (typeof(params.data.site) == 'undefined')
               {	params.data.site='site none'}
            if (typeof(params.data.uri) == 'undefined')            
               {	params.data.uri='uri none'}
            if (typeof(params.data.title) == 'undefined')
               {	params.data.title='title none'}            
            return ''+params.data.title+'\\n<br/>'+params.data.site+'\\n<br/>'+params.data.uri
        }
        """
    ctree = Tree()
    ctree.add("", data)
    ctree.set_global_opts(title_opts=opts.TitleOpts(title="Tree-基本示例"))
    ctree.set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=True,
                                      trigger="item",
                                      trigger_on="mousemove",
                                      is_always_show_content=True,
                                      formatter=utils.JsCode(ffbmformater)))

    ctree.render("outdata/ffbmtree.html")


print(pyecharts.__version__)
os.makedirs("outdata")
echar()
echar_tree()
echar_ffbmtree()