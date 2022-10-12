# Underwolf

Underwolf is my best answer to updating my World of Warcraft addons, both on and off CurseForge after the retirement of the CurseForge API (staying away from the CurseForge application). 

It utilizes Python's built-in webbrowser library to navigate to [CurseForge](https://www.curseforge.com/) download pages (as well as other direct download URLs, such as [Tukui](https://www.tukui.org) and [Trade Skill Master](https://www.tradeskillmaster.com/)) and download the specified addons, unzip them, and move them into the WoW addon folder. The script utilizes Selenium for version checking (version checking is only implemented on CurseForge addons).

## Requirements

Clone the repo, cd into the directory, and run the following:

    python3 -m venv venv

then activate the virtual environment and run

    pip install -r requirements.txt

### Provide the path to uBlock Origin

The script currently **requires [Firefox](https://www.mozilla.org/en-US/firefox/new/) and [uBlock Origin](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/).** uBlock Origin "fast-forwards" the CurseForge imposed 5-second wait time (as well as other sites) before the download starts on the download pages.

In order to use uBlock Origin with Selenium, you'll have to provide the path to uBlock's .xpi file in the get_version() function at the bottom of main.py. On Windows, you can find Mozilla's extension folder here with a default installation:

    C:\Users\USER\AppData\Roaming\Mozilla\Firefox\Profiles\RANDOMSTRING.default-release\extensions\uBlock0@raymondhill.net.xpi

On Mac:

    /Users/user/Library/Application Support/Firefox/Profiles/RANDOMSTRING.default-release/extensions/uBlock0@raymondhill.net.xpi

main.py is currently populated with my personal path. You must make the above changes for the script to successfully execute.

**Without uBlock Origin and the above change, the script will not work.**

### Install the geckodriver

The script uses Selenium and built-in Python libraries - you must have the [Firefox Gecko driver](https://github.com/mozilla/geckodriver/releases) appropriate for your system. Unzip the driver into the Underwolf directory.

Note that the script calls **taskkill** on all Firefox processes at the end to clean up. Chrome implementation is planned for a later version (Although that may become obsolete with Manifest V3 and its effect on ad blockers).

### Add addons to addons_master_list.json

Add addons to addon_master_list.example.json like so:

    {
    "DBM" : {
        "curseforge" : 1, # int 1 for CurseForge addon, 0 for a direct download addon outside of CF (such as ElvUI)
        "anchor_link" : "https://www.curseforge.com/wow/addons/deadly-boss-mods", # landing page for CF mods (not needed for direct download addons)
        "dl_url" : "https://www.curseforge.com/wow/addons/deadly-boss-mods/download", # download page (required for all addons)
        "last_updated" : "" # leave blank. The script will populate this field on first run.
    },

Rename 
    addon_master_list_example.json
to
    addon_master_list.json

The script will also backup the list at the beginning of each run just in case something goes wrong.

## Copyright © 2022 Nicholas Johnson

Permission to use, copy, modify, distribute, and sell this software and its documentation for any purpose is hereby granted without fee, provided thatthe above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. No representations are made about the suitability of this software for any purpose.  It is provided "as is" without express or implied warranty.

Tested on **MacOS Ventura v13.0 Beta (22A5352e)** and **Windows 11 (Stable)** using **Firefox 104.0.2** with **uBlockOrigin 1.44.4**. Tested on Python 3.10.6, but should work with Python 3.5+.
