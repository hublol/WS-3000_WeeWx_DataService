# WS-3000 data service for WeeWX

## Description

This is a simple weewx data service used to combine the data coming from the WS-3000 station with the data from another station.

## Pre-Requisites

The WS-3000 driver must be installed,
and the station configured.

## Installation

1) Download the WS-3000 data service extension package from the Releases page:

wget -O weewx-ws3000ds.tar.gz https://github.com/hublol/WS-3000_WeeWx_DataService/archive/refs/tags/weewx-ws3000ds-0.2.tar.gz


2) Install the extension:

wee_extension --install weewx-ws3000ds.tar.gz

3) Check if the extension is correctly installed:

./bin/wee_extension --list

## Configuration

Add the data service to the weewx.conf file:

[Engine]
    [[Services]]
        data_services = user.ws3000DataService.AddWS300Data,
