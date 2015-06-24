# -*- coding: utf-8 -*-
import xbmc,urllib

all_modules = [ 'https://raw.github.com/anphunl/kodi/master/p2p-parsers/8bongda.tar.gz','https://raw.github.com/anphunl/kodi/master/p2p-parsers/bongdatructuyen.tar.gz']

for parser in all_modules:
	xbmc.executebuiltin('XBMC.RunPlugin("plugin://plugin.video.p2p-streams/?mode=405&name=p2p&url=' + urllib.quote(parser) + '")')
	xbmc.sleep(1000)

xbmc.executebuiltin("Notification(%s,%s,%i,%s)" % ('P2P-Streams', "All parsers imported",1,''))
