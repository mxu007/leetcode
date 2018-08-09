# A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

# Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

# We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.


# Example 2:
# Input:
# ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Output:
# ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
# Explanation:
# We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.

# Notes:

# The length of cpdomains will not exceed 100.
# The length of each domain name will not exceed 100.
# Each address will have either 1 or 2 "." characters.
# The input count in any count-paired domain will not exceed 10000.
# The answer output can be returned in any order.

# https://leetcode.com/problems/subdomain-visit-count/description/


class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        # init dictionary to store count
        subdomain_counts = {}

        # iterate through the list of count and full domain
        for string in cpdomains:
            # get the count
            count = int(string.split(" ")[0])
            # get the full domain
            domain = string.split(" ")[1]
            # get subdomain elements
            subdomains = domain.split(".")
            # generate subdomains and update count in the dictionary
            for i in range(0,len(subdomains)):
                subdomain = ('.'.join(subdomains[i:]))
                print(subdomain, count)
                subdomain_counts[subdomain] = subdomain_counts.get(subdomain, 0) + count

        print (subdomain_counts)

        # init result list
        result = []

        # iterate through the dictionary to generate string
        for key, val in subdomain_counts.items():
            result.append(str(val)+" "+str(key))

        return (result)
