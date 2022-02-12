from firefoxbookmarks.Manager import Manager


def main():
    #
    bms = Manager()
    bms.loadbms()
    bms = bms.movefunc_without_folder('tianqi.com')
    bms.save_firefoxbookmarksjson('outdata/without.json')
#
    bms = Manager()
    bms.loadbms()
    bms = bms.movefunc_with_folder('baidu.com')
    bms.save_firefoxbookmarksjson('outdata/with.json')
#
    path1 = 'z:/test/1500.json'
    bms = Manager()
    bms.loadbms(path1)
    bms = bms.movefunc_without_folder('rrys2020.com')
    bms.save_firefoxbookmarksjson('outdata/1500without.json')
#
    bms = Manager()
    bms.loadbms(path1)
    bms = bms.movefunc_with_folder('rrys2020.com')
    bms.save_firefoxbookmarksjson('outdata/1500with.json')


# -----------------------
if __name__ == '__main__':
    main()
