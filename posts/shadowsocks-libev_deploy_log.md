title: deploy shadowsocks on vps
date: 2017-1-25 16:30:00
summary: how to deploy shadowsocks on vps

===

### shadowsocks-libev deploy log

I've bought the bandwagonhost for a few months(annual plan).

I finnaly managed to setup a shadowsocks proxy server on my VPS. The whole processs is actually much easier than I thought.

I followed the guide on the shadowsocks-libev, it went on all well. except for one thing. terminal says it can't find the shadowsocks-libev package in apt-get. If you met this problem as well, just change the name of the package from shadowsocks-libev to shadowsocks. that will fix it.

<code>$: apt-get install shadowsocks</code>
