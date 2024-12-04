from helper.action import *
from POM.POM_Detail import *
from POM.POM_Home import *

def test_openDetailArtikel(openDriver):
    element_click(openDriver, detailArtikelTerbaru)
    validate_is_display(openDriver, detailArtikelTerbaru)

def test_openArtikelPopuler(openDriver):
    test_openDetailArtikel(openDriver)
    element_click(openDriver, artikelPizza)
    validate_is_display(openDriver, artikelPizza)

def test_openBacaJuga(openDriver):
    element_click(openDriver, detailArtikelTerbaru)
    element_click(openDriver, BacaJuga)

def test_topikTerpopuler(openDriver):
    element_click(openDriver, detailArtikelTerbaru)
    element_click(openDriver, TopikTerkait)

def test_openArtikelTerkait(openDriver):
    element_click(openDriver, detailArtikelTerbaru)
    element_click(openDriver, artikelTerkait)

def test_click_buttonLebihBanyak (openDriver):
    element_click(openDriver, detailArtikelTerbaru)
    element_click(openDriver, Btn_More)

def test_openArtikelTerbaru(openDriver):
    element_click(openDriver, detailArtikelTerbaru)
    element_click(openDriver, ArtikelTerbaru)

def test_PenilaianTerhiburDenganArtikel(openDriver):
    element_click(openDriver, detailArtikelTerbaru)
    element_click(openDriver, penilaianTerhibur)

def test_balankComen_submit(openDriver):
    element_click(openDriver, detailArtikelTerbaru)
    element_click(openDriver, btnKirim)

def test_fill_name_and_Comment(openDriver):
    element_click(openDriver, detailArtikelTerbaru)
    element_input(openDriver, fill_Name, "dhjsdhjhd")
    element_input(openDriver, fill_comment, "bagus sekali artikelnya")

def test_share_wa(openDriver):
    element_click(openDriver, detailArtikelTerbaru)
    element_click(openDriver, Share_WA)

def test_share_Fb(openDriver):
    element_click(openDriver, detailArtikelTerbaru)
    element_click(openDriver, Share_FB)

def test_Share_Linkedin(openDriver):
    element_click(openDriver, detailArtikelTerbaru)
    element_click(openDriver, Share_Linkedin)

def test_share_X(openDriver):
    element_click(openDriver, detailArtikelTerbaru)
    element_click(openDriver, Share_X)