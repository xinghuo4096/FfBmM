import json
from pyecharts.charts import Tree
from pyecharts import options as opts
from pyecharts.commons import utils


def echar_ffbmtree(data):
    ffbmformater = """
        function (params) {                        
            if (typeof(params.data.uri) == 'undefined')            
               {	params.data.uri='uri none'}
            if (typeof(params.data.title) == 'undefined')
               {	params.data.title='title none'}            
            return ''+params.data.title+'\\n<br/>'+params.data.uri
        }
        """
    ctree = Tree()
    ctree.add("", data)
    ctree.set_global_opts(title_opts=opts.TitleOpts(title="书签展示"))
    ctree.set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=True,
                                      trigger="item",
                                      trigger_on="mousemove",
                                      is_always_show_content=True,
                                      formatter=utils.JsCode(ffbmformater)))

    ctree.render("outdata/ffbmtree.html")
