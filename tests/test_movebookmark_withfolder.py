
from firefoxbookmarks.Manager import Manager


def test_move_bookmark_with_foler():
    bms = loadbms()
    bms2 = bms.movefunc_with_folder(findstr='baidu')
    assert isinstance(bms2, Manager)
    bms2.save_firefoxbookmarksjson()

    assert len(bms2) > 0


def loadbms() -> Manager:
    path1 = "z:/test/a.json"
    bms = Manager()
    bms.loadbms()
    return bms


# ----
def main():
    test_move_bookmark_with_foler()


if __name__ == '__main__':
    main()
