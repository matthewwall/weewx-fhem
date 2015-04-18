weewx skin that produces data for FHEM

Installation instructions:

1) run the installer:

setup.py install --extension weewx-fhem.tgz

2) restart weewx:

sudo /etc/init.d/weewx stop
sudo /etc/init.d/weewx start

Additional instructions:

The output file "fhem.txt" must go to the a folder where FHEM can see it, such
as the public_html/fhem folder of a web server.  Use an FTP or RSYNC report
in weewx to transfer the file.  For example, this fhem_xfer stanza in
weewx.conf would upload the fhem.txt file using FTP:

[StdReport]
    [[fhem]]
        skin = fhem
        HTML_ROOT = fhem
    [[fhem_xfer]]
        skin = Ftp
        HTML_ROOT = fhem
        user = username
        password = pw
        server = hostname
        path = /home/username/public_html/fhem

The file fhem.cfg is a configuration file for FHEM's module HTTPMOD. 
There are two variations included in this package.  fhem-klimalogg.cfg uses
the klimalogg schema, fhem-wview.cfg uses the default weewx schema (wview).   

The fhem.cfg file contains the configuration examples for current values only;
for min/max values, heatindex and dewpoint values use similar syntax
for setting readingXXExpr /readingXXName / readingXXRegex.

Credits:

Thanks to Steffen for sorting this out and sharing the fhem files with us.
