# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

# Example 1:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# Example 2:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
# Note:
# The length of both lists will be in the range of [1, 1000].
# The length of strings in both lists will be in the range of [1, 30].
# The index is starting from 0 to the list length minus 1.
# No duplicates in both lists.

# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

# use only dictioanry, more elegant solution
class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # construct dictionary retaurant-index pair for the first list
        dict_1 = {rest:i for i, rest in enumerate(list1)}
        # construct dictionary for common items using restaurant - index sum pair
        dict_common = {rest:i+dict_1[rest] for i,rest in enumerate(list2) if rest in dict_1}
        # get the min index sum
        min_index_sum = min(value for value in dict_common.values())
        # return all keys with values equal to min index sum
        return [key for key,value in dict_common.items() if value == min_index_sum]

# use set, list and dictionary, less efficient
class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        # construct the common list
        common  = list(set(list1).intersection(set(list2)))
        # dictionary to store the common item - index sum pair
        index_sums = {}

        # assume always exist an answer
        # if only one common interst, directly return
        if(len(common)==1):
            return common
        # iterate the common list to udpate the dictioanry
        else:
            for item in common:
                index_sum = list1.index(item) + list2.index(item)
                index_sums[item] = index_sum
            # find the min value of the dicitonary
            min_index_sum = min(index_sums.values())
            # return all keys with the minimum value
            return [key for key, value in index_sums.items() if value == min_index_sum]

