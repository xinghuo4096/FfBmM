import codecs
import json
import os
import time
from pyecharts.charts import Tree
from pyecharts import options as opts
from pyecharts.commons import utils
from pyecharts.globals import ThemeType
from pyecharts.globals import CurrentConfig

import firefoxbookmarks


def simple_ffbmtree(infile='tests/bookmarks-show.json', outfile='outdata/ffbmtree.html'):
    bms = firefoxbookmarks.Manager()
    assert isinstance(bms, firefoxbookmarks.Manager)
    bms.loadbms('bookmarks-show.json')
    assert isinstance(bms.root, firefoxbookmarks.MozBaseItem)

    listjson = [json.loads(bms.root.toJSON())]

    w = len(bms.folders) * 100
    h = len(bms.bookmarks) / len(bms.folders) * 450
    echar_ffbmtree(data=listjson, outfile=outfile,
                   tree_depth=2, w=w, h=h, is_cdn_jsdelivr=True)


def echar_ffbmtree(data: list, infile='', outfile='outdata/ffbmtree.html', tree_depth=2, w=1280, h=720, is_cdn_jsdelivr=True):
    if (is_cdn_jsdelivr):
        CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/npm/echarts@latest/dist/"

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
            if (typeof(params.data.keyword) != 'undefined')            
               {	showstr+='\\n<br/>keyword:'+params.data.keyword}   
            if (typeof(params.data.index) != 'undefined')            
               {	showstr+='\\n<br/>index:'+params.data.index}         
            return showstr
        }
        """
    assert isinstance(outfile, str)
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    ctree = Tree(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE,
                                         page_title='FfBmM Show' + localtime,
                                         width=str(w) + 'px',
                                         height=str(h) + 'px'))

    ctree.set_global_opts(title_opts=opts.TitleOpts(title='Bookmarks show'))
    ctree.add('书签',
              data,
              orient='LR',
              pos_top='1%',
              pos_bottom='1%',
              is_roam=False,
              initial_tree_depth=tree_depth,
              layout='orthogonal',
              edge_fork_position='190%',
              itemstyle_opts=opts.ItemStyleOpts(color='red'),
              label_opts=opts.LabelOpts(color="blue"),
              tooltip_opts=opts.TooltipOpts(
                  background_color='rgba(193,203,215, 0.8)',
                  is_show=True,
                  trigger='item',
                  trigger_on='mousemove',
                  formatter=utils.JsCode(ffbmformater)))
    ctree.render(outfile)

    if os.path.isfile(outfile) and is_cdn_jsdelivr:
        fix_cdn_jsdelivr(outfile)


def fix_cdn_jsdelivr(outfile):
    f = codecs.open(outfile, "r", "utf-8")
    s = f.read()
    f.close()
    assert len(s) > 0

    s = s.replace('dist/themes/vintage.js', 'theme/vintage.min.js')

    f = codecs.open(outfile, "w", "utf-8")
    s = f.write(s)
    f.close()
