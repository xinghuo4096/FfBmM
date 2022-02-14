import json
import firefoxbookmarks


def main():
    # show one

    firefoxbookmarks.simple_ffbmtree(
        infile='bookmarks-show.json', outfile='simple_ffbmtree.html')

    # show two

    bms = firefoxbookmarks.Manager()
    bms.loadbms('z:/test/1500.json')

    listjson = [json.loads(bms.root.toJSON())]
    w = len(bms.folders) * 100
    h = len(bms.bookmarks) / len(bms.folders) * 450

    if w < 1280:
        w = 1280
    if h < 720:
        h = 720

    firefoxbookmarks.echar_ffbmtree(
        data=listjson, outfile='show2_ffbmtree.html', tree_depth=10, w=w, h=h)


# -----------------------
if __name__ == '__main__':
    main()
