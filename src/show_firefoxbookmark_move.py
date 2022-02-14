import firefoxbookmarks


def main():
    #
    bms = firefoxbookmarks.Manager()
    bms.loadbms('bookmarks-show.json')
    bms = bms.movefunc_without_folder('tianqi.com')
    bms.save_firefoxbookmarksjson('without.json')
#
    bms = firefoxbookmarks.Manager()
    bms.loadbms('bookmarks-show.json')
    bms = bms.movefunc_with_folder('baidu.com')
    bms.save_firefoxbookmarksjson('with.json')
#
    path1 = 'z:/test/1500.json'
    bms = firefoxbookmarks.Manager()
    bms.loadbms(path1)
    bms = bms.movefunc_without_folder('rrys2020.com')
    bms.save_firefoxbookmarksjson('outdata/1500without.json')
#
    bms = firefoxbookmarks.Manager()
    bms.loadbms(path1)
    bms = bms.movefunc_with_folder('rrys2020.com')
    bms.save_firefoxbookmarksjson('outdata/1500with.json')


# -----------------------
if __name__ == '__main__':
    main()
