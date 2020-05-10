# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class ScreenSquishPlugin(octoprint.plugin.AssetPlugin, octoprint.plugin.TemplatePlugin, octoprint.plugin.SettingsPlugin):
	def __init__(self):
		pass

	def get_settings_defaults(self):
		return dict(
			octoprint_max_version = None
		)

	def get_assets(self):
		return dict(
			js=["js/squish.js"],
			css=["css/squish.css"]
		)

__plugin_name__ = "ScreenSquish"
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = ScreenSquishPlugin()

	# global __plugin_hooks__
	# __plugin_hooks__ = {"some.octoprint.hook": __plugin_implementation__.some_hook_handler}
