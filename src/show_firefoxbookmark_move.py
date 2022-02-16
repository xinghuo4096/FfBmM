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


# -----------------------
if __name__ == '__main__':
    main()
