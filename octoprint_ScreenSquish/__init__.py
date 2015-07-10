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

		octoprint_version = self._parse_version(get_versions()["version"])
		settings_max_version = self._parse_version(self._settings.get(["octoprint_max_version"]))
		default_max_version = self._parse_version(self.octoprint_max_version)

		self._logger.info("version: %s, max_version: %s, default_version: %s" % (octoprint_version, settings_max_version, default_max_version))

		if settings_max_version is None or settings_max_version == '' or default_max_version > settings_max_version:
			self._settings.set(["octoprint_max_version"], None)
			if octoprint_version >= default_max_version:
				return dict(js=["js/squishsettings.js"])
		elif octoprint_version > settings_max_version:
			return dict(
				js=["js/squishsettings.js"]
			)
		
		return dict(
			js=["js/squish.js"],
			css=["css/squish.css"]
		)

	def _parse_version(self, version):
		# if setuptools is old, let's just use the first two tuple elements,
		# otherwise we'll leave the comparison up to the Version objects
		version = parse_version(version)
		if isinstance(version, tuple):
			return version[:2]
		return version

__plugin_name__ = "ScreenSquish"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = ScreenSquishPlugin()

	# global __plugin_hooks__
	# __plugin_hooks__ = {"some.octoprint.hook": __plugin_implementation__.some_hook_handler}
