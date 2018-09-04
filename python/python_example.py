#!/usr/bin/env python
#


def regular_expression():
    import re

    # When an "r" or "R" prefix (means raw string) is present, a character following a backslash is
    # included in the string without change, and all backslashes are left in the string.
    # For example, the string literal r"\n" consists of two characters: a backslash and a lowercase "n".

    print re.findall(r'[a-z]+[0-9\.]+', 'hello 42 I\'m a 32 str12ing 30.0')
    # ['str12']

    print re.findall(r'^hello.*world', 'hello, world; ...')
    # ["hello, world"]

    print re.findall(r'\d{4}-\d{1,2}-\d{1,2}', 'Today is 2018-08-23, or 2018-8-23')
    # ['2018-08-23', '2018-8-23']


def urllib():
    import tld
    import urllib2
    from bs4 import BeautifulSoup
    from urlparse import urlparse
    from cookielib import CookieJar

    host = 'http://google.com'
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) ' \
                 'Version/11.0 Mobile/15E148 Safari/604.1'
    try:
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(CookieJar()))
        urllib2.install_opener(opener)
        req = urllib2.Request(host, headers={'User-Agent': user_agent})
        content = urllib2.urlopen(req, timeout=30)
        content_type = content.info()['Content-Type'].split(';')[0]

        final_host = content.geturl()

        host_name = urlparse(final_host).hostname

        domain = tld.get_fld(host)

        title = BeautifulSoup(content, features="html5lib").title.string

    except urllib2.HTTPError as e:
        raise Exception('Error code: %s; Reason: %s' % (e.code, e.reason))
    except urllib2.URLError as e:
        raise Exception('Error Reason: %s' % e.reason)
    except Exception as e:
        raise Exception('Unknown Reason')

    return content_type, final_host, host_name, domain, title


def requests(host):
    import requests
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) ' \
                 'Version/11.0 Mobile/15E148 Safari/604.1'
    r = requests.get(host, headers={'User-Agent': user_agent}, timeout=30)

    print r.ok, r.status_code, r.reason, r.headers.get('Content-Type'), r.url


def tld(host):
    import tld
    # get_tld("www.google.co.uk", fix_protocol=True) return 'co.uk'
    # get_fld("www.google.co.uk", fix_protocol=True) return 'google.co.uk'

    try:
        domain = tld.get_fld('http://' + host)
    except:
        # These abnormal domain will be filtered out.
        domain = 'Invalid_Domain'
    return domain



def date_time():
    from datetime import datetime
    ts = 1530197524309
    _ts = datetime.utcfromtimestamp(ts / 1000).strftime('%Y-%m-%d %H:%M:%S')


def main():
    urllib()


if __name__ == '__main__':
    main()