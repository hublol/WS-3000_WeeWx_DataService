# WS-3000 data service for WeeWX

## Description

This is a simple weewx data service used to combine the data coming from the WS-3000 station with the data from another station.

## Installation

. Download the WS-3000 data service extension package from the Releases page:
+
----
wget https://github.com/hublol/WS-3000_WeeWx/archive/refs/tags/weewx-ws3000-0.2.tar.gz
----

. Install the extension:
+
----
wee_extension --install weewx-ws3000-ds-x.x.tar.gz
----

. Check if the extension is correctly installed:
+
----
./bin/wee_extension --list
----
