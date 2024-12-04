from helper.action import *
from POM.POM_Home import *

def test_detail_artikelTerbaru(openDriver):
    element_click(openDriver, detailArtikelTerbaru)
    validate_is_display(openDriver, judul_artikel)

def test_subkanal_Lifestyle(openDriver):
    element_click(openDriver, Lifestyle_Btn)
    element_click(openDriver, detailArtikelLifestyle)
    validate_is_display(openDriver, detailArtikelLifestyle)

def test_subkanal_Tech(openDriver):
    element_click(openDriver, Tech_Btn)
    element_click(openDriver, detailArtikelTech)
    validate_is_display(openDriver, detailArtikelTech)

def test_button_TampilkanLebihBanyak(openDriver):
    element_click(openDriver, Lifestyle_Btn)
    element_click(openDriver, Btn_More)

def test_search_not_found(openDriver):
    element_input(openDriver, search, "sdsfdfdfdfd")
    element_click(openDriver, btn_search)
    validate_is_display(openDriver, search_notFound)

def test_search_found(openDriver):
    element_input(openDriver, search, "Tiktok")
    element_click(openDriver, btn_search)
    validate_is_display(openDriver, artikel_tiktok)

def test_open_ArtikelPopuler(openDriver):
    element_click(openDriver, artikel_populer)
    validate_is_display(openDriver, artikel_populer)

def test_open_TopikPopuler_Tiktok(openDriver):
    element_click(openDriver, tag_TikTok)
    validate_is_display(openDriver, artikel_tiktok)

def test_button_more_in_topik(openDriver):
    element_click(openDriver, tag_TikTok)
    validate_is_display(openDriver, artikel_tiktok)
    element_click(openDriver, Btn_More)