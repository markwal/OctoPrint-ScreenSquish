$(function() {
    function ScreenSquishViewModel(parameters) {
        var self = this;

        self.settings = parameters[0];
        self.temperatureViewModel = parameters[1];
    
        self.override_version = ko.observable(false);
        self.show_override = ko.observable(false);

        self.temperatureTab = $('#temp');
        self.currentTabName = undefined;

        self.settingsTabs = $('#settingsTabs a[data-toggle="tab"]');
        self.settingsTabs.on('shown', function(e) {
            self.ensureSettingsTabName();
        });

        self.ensureSettingsTabName = function() {
            if (self.currentTabName != undefined) {
                self.currentTabName.text($('#settingsTabs .active').text());
                if ($('#squishSettingsTabButton').css('display') != 'none') {
                    $('#squishSettingsMenuList').collapse('hide');
                }
            }
        };

        self.onStartup = function() {
            // add the viewport
            $('head').prepend('<meta name="viewport" content="width=device-width, initial-scale=1">');

            // add title bar nav button
            $('#navbar .container').prepend('<a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse"><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span></a>');

            // set up the collapsible settings nav
            settingsDialogMenu = $('#settings_dialog_menu');
            settingsTabButton = $('<button class="btn dropdown-toggle" id="squishSettingsTabButton"><i class="icon-align-justify"></i><span id="squishSettingsTabName"></span></button>');
            settingsDialogMenu.append(settingsTabButton);
            self.settingsMenuList = $('<div class="collapse in" id="squishSettingsMenuList"></div>');
            settingsDialogMenu.append(self.settingsMenuList);
            self.settingsMenuList.append($('#settingsTabs'));
            self.currentTabName = $('#squishSettingsTabName');
            settingsTabButton.on('click', function() {
                self.settingsMenuList.collapse('toggle');
            });
            self.ensureSettingsTabName();

            // gcode viewer
            $('#gcode_canvas').wrap('<div class="gcode_canvas_clipper"></div>');

            $('.nav-pills, .nav-tabs').tabdrop('layout');
        };

        self.onStartupComplete = function() {
            // hide the units in temperature settings at the tablet breakpoint for space
            $('#temp span.add-on').addClass('squish-temp-units');

            max_version = self.settings.settings.plugins.ScreenSquish.octoprint_max_version();
            if (max_version && max_version != '') {
                self.override_version(true);
                self.show_override(true);
            }
        };

        self.onSettingsBeforeSave = function() {
            version = '';
            if (self.override_version()) {
                version = $('span.version').text();
            }
            self.settings.settings.plugins.ScreenSquish.octoprint_max_version(version);
            if (version == '' && self.show_override()) {
                new PNotify({
                    title: gettext("ScreenSquish auto off"),
                    text: gettext("This won't take effect until OctoPrint has been restarted.")
                });
            }
        }

        self.updateScreenWidth = function() {
            if (self.temperatureTab.is(":visible")) {
                self.temperatureViewModel.updatePlot();
            }
        }

        self.delayResize = undefined;
        $(window).on("resize", function(e) {
            clearTimeout(self.delayResize);
            self.delayResize = setTimeout(function() {
                self.updateScreenWidth();
            }, 500);
        });
    }

    OCTOPRINT_VIEWMODELS.push([
        ScreenSquishViewModel,
        ["settingsViewModel", "temperatureViewModel"],
        ["#screen_squish_settings"]
    ]);
});
