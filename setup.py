# coding=utf-8

########################################################################################################################
plugin_identifier = "ScreenSquish"
plugin_package = "octoprint_%s" % plugin_identifier
plugin_name = "OctoPrint-ScreenSquish"
plugin_version = "0.2"
plugin_description = "Scalable UI that does some old fashioned (2.3) bootstrap responsive and some collapse etc."
plugin_author = "Mark Walker"
plugin_author_email = "markwal@hotmail.com"
plugin_url = "https://github.com/markwal/OctoPrint-ScreenSquish"
plugin_license = "AGPLv3"
plugin_requires = []
plugin_additional_data = []
########################################################################################################################

from setuptools import setup

try:
	import octoprint_setuptools
except:
	print("Could not import OctoPrint's setuptools, are you sure you are running that under "
	      "the same python installation that OctoPrint is installed under?")
	import sys
	sys.exit(-1)

setup(**octoprint_setuptools.create_plugin_setup_parameters(
	identifier=plugin_identifier,
	name=plugin_name,
	version=plugin_version,
	description=plugin_description,
	author=plugin_author,
	mail=plugin_author_email,
	url=plugin_url,
	license=plugin_license,
	requires=plugin_requires,
	additional_data=plugin_additional_data
))
