# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
from pkg_resources import parse_version

class ScreenSquishPlugin(octoprint.plugin.AssetPlugin, octoprint.plugin.TemplatePlugin, octoprint.plugin.SettingsPlugin):
	def __init__(self):
		# when octoprint is >= to octoprint_max_version, disable this plugin
		# automatically because of the fragile internal dependencies on HTML
		# this is the maintain by hand method, eventually responsive will be built
		# in or we'll do a complete alternate UI and we won't maintain it this
		# way
		self.octoprint_max_version = "1.2.0"

	def get_settings_defaults(self):
		return dict(
			octoprint_max_version = None
		)

	def get_assets(self):
		from octoprint._version import get_versions
		octoprint_version = get_versions()["version"]

		octoprint_max_version = self._settings.get(["octoprint_max_version"])
		if octoprint_max_version is None or octoprint_max_version == '' or parse_version(self.octoprint_max_version)[:2] > parse_version(octoprint_max_version)[:2]:
			self._settings.set(["octoprint_max_version"], None)
			octoprint_max_version = self.octoprint_max_version

		if parse_version(octoprint_version)[:2] > parse_version(octoprint_max_version)[:2]:
			return dict(
				js=["js/squishsettings.js"]
			)
		
		return dict(
			js=["js/squish.js"],
			css=["css/squish.css"]
		)

__plugin_name__ = "ScreenSquish"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = ScreenSquishPlugin()

	# global __plugin_hooks__
	# __plugin_hooks__ = {"some.octoprint.hook": __plugin_implementation__.some_hook_handler}
