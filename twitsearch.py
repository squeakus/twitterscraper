# This file is part of twitterscraper.
# Architype is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# Architype is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public License 
# along with twitterscraper.  If not, see <http://www.gnu.org/licenses/>.
# Author Jonathan Byrne 2014

import urllib2, json, pprint
HASHTAG = "garda"
u = urllib2.urlopen('http://search.twitter.com/search.json?q='+HASHTAG+'&rpp=25')
resultdict = json.load(u)

pprint.pprint(resultdict)
for tweet in resultdict['results']:
    print tweet['text']
