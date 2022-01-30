import json
from turtle import width
from pyecharts.charts import Tree
from pyecharts import options as opts
from pyecharts.commons import utils

from firefoxbookmarks.Bookmarks import BookMarks


def echar_ffbmtree(data, w, h):

    ffbmformater = """
        function (params) {   
            showstr='';                 
            if (typeof(params.data.iconuri) != 'undefined') 
               {	showstr+='<img src='+params.data.iconuri+' alt='+params.data.title+'/>'}               
            if (typeof(params.data.title) != 'undefined')
               {	showstr+='Title:'+params.data.title}            
            if (typeof(params.data.uri) != 'undefined')            
               {	showstr+='\\n<br/>uri:'+params.data.uri}
            if (typeof(params.data.tags) != 'undefined')            
               {	showstr+='\\n<br/>tags:'+params.data.tags}            
            if (typeof(params.data.iconuri) != 'undefined')            
               {	showstr+='\\n<br/>iconuri:'+params.data.iconuri}            
            return showstr
        }
        """

    ctree = Tree(
        init_opts=opts.InitOpts(width=str(w) + 'px', height=str(h) + 'px'))
    ctree.add("书签", data, is_roam=True, initial_tree_depth=2)

    ctree.set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=True,
                                      trigger="item",
                                      trigger_on="mousemove",
                                      is_always_show_content=True,
                                      formatter=utils.JsCode(ffbmformater)))

    ctree.render("outdata/ffbmtree.html")
