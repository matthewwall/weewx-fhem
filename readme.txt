weewx skin that produces data for FHEM

Installation instructions:

1) run the installer:

setup.py install --extension weewx-fhem.tgz

2) restart weewx:

sudo /etc/init.d/weewx stop
sudo /etc/init.d/weewx start

The output file "fhem.txt" must go to the public_html\fhem folder of
your webserver.  Use the FTP or RSYNC report in weewx to upload fhem.txt
to a place where FHEM can see it.

The file fhem.cfg is a configuration file for FHEM's module HTTPMOD. 
There are two variations included in this package.  fhem-klimalogg.cfg uses
the klimalogg schema, fhem-wview.cfg uses the default weewx schema (wview).   

This file contains the configuration examples for current values only;
for min/max values, heatindex and dewpoint values use similar syntax
for setting readingXXExpr /readingXXName / readingXXRegex.

Credits:

Thanks to Steffen for sorting this out and sharing the fhem files with us.
