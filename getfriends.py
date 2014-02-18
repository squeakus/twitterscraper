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

user_friends = urllib2.urlopen('https://api.twitter.com/1/friends/ids.json?cursor=-1&screen_name=squeakusmaximus&stringify_ids=true')
resultdict = json.load(user_friends)

for result in resultdict:
    print result

print "ids:",resultdict['ids']
id_list = resultdict['ids']

for user_id in id_list:
    query_string = 'https://api.twitter.com/1/users/show.json?id=' + user_id
    user_info = urllib2.urlopen(query_string)
    userdict = json.load(user_info)
    print userdict['name']
    #for result in userdict:
    #print result

