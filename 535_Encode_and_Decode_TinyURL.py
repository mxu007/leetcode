# Note: This is a companion problem to the System Design problem: Design TinyURL.
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

# https://leetcode.com/problems/encode-and-decode-tinyurl/description/
import string
class Codec:
    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        while longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            # short-long and long-short mappings
            # so two dictionaries
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return 'http://tinyurl.com/' + self.url2code[longUrl]

    def decode(self, shortUrl):
        # last six elements in the list
        return self.code2url[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


# 2) variant of 1), use only one dictionary
import random
import string
class Codec:
    def __init__(self):
        self.url_pair = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL."""
        # Get a set of characters that will make up the suffix
        suffix_set = string.ascii_letters + string.digits

        # Make a tinyurl template
        tiny_url = "http://tinyurl.com/".join(random.choice(suffix_set) for _ in range(6))

        # Store the pair in the dictionary
        self.url_pair[tiny_url] = longUrl

        return tiny_url

    def decode(self, shortUrl):
        """Decodes the shortened URL to its original URL."""
        # Return the value from a given key from the dictionary
        return self.url_pair.get(shortUrl)

# 3) use default dictionary
import collections
class Codec:
    def __init__(self):
        self.encodeDict = collections.defaultdict()
        self.encodeDict.default_factory = self.encodeDict.__len__
        self.decodeDict = collections.defaultdict(str)

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        # map the longUrl to the length of dictionary
        self.decodeDict[self.encodeDict[longUrl]] = longUrl
        return self.encodeDict[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.decodeDict[shortUrl]

# 4) use hash function in Python 2
import random
import string

class Codec:
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.hash= {}
        if longUrl not in self.hash:
            # Return the hash value of the object (if it has one). Hash values are integers
            self.hash[hash(longUrl)]=longUrl
        return ('https://tinyurl.com/'+str(hash(longUrl)))

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return(self.hash[int(shortUrl[20:])])

# 5) use hashilib md5
from hashlib import md5

class Codec:
    tinies = {}

    def encode(self, longUrl):
        m = md5()
        m.update(longUrl)
        h = m.hexdigest()
        i = 0
        while h[:5+i] in self.tinies:
            i += 1
        self.tinies[h[:5+i]] = longUrl
        return 'http://tinyurl.com/' + h[:5+i]

    def decode(self, shortUrl):
        return self.tinies[shortUrl.split('/')[3]]
