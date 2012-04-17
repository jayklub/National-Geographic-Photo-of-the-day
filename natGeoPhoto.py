'''
Retrieve the national geographic photo of the day
and store it in ~/Pictures/desktops/
'''
import os
import re
import urllib2


if __name__ == '__main__':
    title = ''
    url = ''

    #
    # Loop until you find the image on the National Geographic page.
    #
    regex = re.compile('"download_link"><a href=".*"')
    regex_title = re.compile('.*<meta property="og:url" content=".*')

    for line in urllib2.urlopen('http://photography.nationalgeographic.com/photography/photo-of-the-day/petrified-dunes-barnes/').readlines():
        title_match = regex_title.findall(line)
        matches = regex.findall(line)
        if title_match:
            title = title_match[0].split('http')[1].split(' ')[0].replace('"','').split('/')[-2] + '.jpg'

        if matches:
            #url = line[len(matches):].split('"')[0]
            url = matches[0].split('=')[1].split(' ')[0].replace('"','')
            print url
            break

    if url:
        #
        # Copy the image.
        #
        cmd = 'curl --silent --show-error %s > ~/Pictures/natGeo/%s' % (
            url, title or url.split('/')[-1])
        os.system(cmd)
