#!/usr/bin/env python2

from verdandi.verdandi import Verdandi
from verdandi.modules.page import Page
from verdandi.modules.commonassets import CommonAssets
from verdandi.modules.sassassets import SassAssets


class LandingPage(Page):
	title = "Seidenstrasse :: OpenSource Rohrpost"
	menu_title = "Home"
	menu_label = "home"
	content_file = "landing.html"
	content_is_markdown = False

class Assets(CommonAssets):
	assets = [('css/normalize.css', 'css/'),
				('fonts/', 'fonts/'),
				('js/jquery-2.2.3.min.js', 'js/'),
				('images/', 'images/')]


class Sass(SassAssets):
	assets = [('css/main.scss', 'css/main.css')]

class SeidenstrasseSite(Verdandi):
	modules = [LandingPage(),
				Sass(),
				Assets()]



site = SeidenstrasseSite()
site.run()
