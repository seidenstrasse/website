#!/usr/bin/env python2

from verdandi.verdandi import Verdandi
from verdandi.modules.page import Page
from verdandi.modules.commonassets import CommonAssets


class MainPage(Page):
	title = "Seidenstrasse :: OpenSource Rohrpost"
	menu_title = "Home"
	menu_label = "home"

class Assets(CommonAssets):
	assets = [('css/normalize.css', 'css/'),
				('css/main.css', 'css/'),
				('fonts/', 'fonts/'),
				('js/jquery-2.2.3.min.js', 'js/'),]

class SeidenstrasseSite(Verdandi):
	modules = [MainPage(),
				Assets()]



site = SeidenstrasseSite()
site.run()
