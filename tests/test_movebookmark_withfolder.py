
from firefoxbookmarks import MozPlace
from firefoxbookmarks.Manager import Manager
from firefoxbookmarks.MozPlaceContainer import MozPlaceContainer


def test_move_bookmark_with_foler():
    bms = loadbms()
    root = bms.root
    bms.AddTagsToBookmark(root, '')

    root = bms.root
    folder = root

    assert isinstance(root, MozPlaceContainer)
    assert isinstance(folder, MozPlaceContainer)
    assert root is folder

    menu = folder.children[0]

    news = menu.children[0]
    assert isinstance(folder, MozPlaceContainer)
    assert news.title.lower() == 'news'

    bd = news.children[0]
    assert isinstance(bd, MozPlace)
    assert bd.uri == 'http://news.baidu.com/'
    assert 'news' in bd.tags.lower()
    assert '百度新闻' in bd.title
    # baidu
    bms2 = bms.movefunc_with_folder(findstr='baidu')

    assert bms is not bms2

    root = bms2.root
    assert root is not folder
    assert isinstance(root, MozPlaceContainer)
    assert isinstance(folder, MozPlaceContainer)
    folder = root

    menu = folder.children[0]

    news = menu.children[0]
    assert isinstance(folder, MozPlaceContainer)
    assert news.title.lower() == 'news'

    sina = news.children[0]
    assert isinstance(sina, MozPlace)
    assert sina.uri == 'https://news.sina.com.cn/'
    assert 'news' in sina.tags.lower()
    print(sina.tags.lower())
    assert '新浪网' in sina.title

    newfolder = menu.children[len(menu.children)-1]
    assert isinstance(newfolder, MozPlaceContainer)
    assert isinstance(newfolder.title, str)
    assert 'newfolder' in newfolder.title.lower()

    menu = newfolder.children[0]
    toolbar = newfolder.children[1]
    unfiled = newfolder.children[2]
    assert isinstance(menu, MozPlaceContainer)
    assert isinstance(toolbar, MozPlaceContainer)
    assert isinstance(unfiled, MozPlaceContainer)
    assert menu.title.lower() == bms.ROOTS_ROOT[1].lower()
    assert toolbar.title.lower() == bms.ROOTS_ROOT[2].lower()
    assert unfiled.title.lower() == bms.ROOTS_ROOT[3].lower()

    news = menu.children[0]
    assert news.title.lower() == 'news'

    bd = news.children[0]
    assert isinstance(bd, MozPlace)
    assert '百度新闻' in bd.title
    assert bd.uri == 'http://news.baidu.com/'


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
