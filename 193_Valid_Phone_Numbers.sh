# Given a text file file.txt that contains list of phone numbers (one per line), write a one liner bash script to print all valid phone numbers.

# You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

# You may also assume each line in the text file must not contain leading or trailing white spaces.

# Example:

# Assume that file.txt has the following content:

# 987-123-4567
# 123 456 7890
# (123) 456-7890
# Your script should output the following valid phone numbers:

# 987-123-4567
# (123) 456-7890

# https://leetcode.com/problems/valid-phone-numbers/description/


# Read from the file file.txt and output all valid phone numbers to stdout.

# 1) grep -p
# grep prints lines that contain a match for a pattern.

# \d{3} represent xxx, (\d{3}) represents (xxx), | represents OR
# https://www.gnu.org/savannah-checkouts/gnu/grep/manual/grep.html
grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt

# 2) sed
# sed is a stream editor. A stream editor is used to perform basic text transformations on an input stream

# https://www.computerhope.com/unix/used.htm
# -n suppress automatic printing
# -r use regular expression
# $ matches the last line of each file
# ^ matches the begining of the string
# \ is the escape character
# /p to print the line when -n silence is set
# http://www.grymoire.com/Unix/Sed.html#uh-9
sed -r '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/p' file.txt

# 3) awk
# a program that you can use to select particular records in a file and perform operations upon them.
# https://www.gnu.org/software/gawk/manual/gawk.html
# / A regular expression enclosed in slashes (`/') is an awk pattern that matches every input record whose text belongs to that set
awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/' file.txt

# grep -e
# -e for regex pattern
grep -e '\(^[0-9]\{3\}-[0-9]\{3\}-[0-9]\{4\}$\)' -e '\(^([0-9]\{3\})[ ]\{1\}[0-9]\{3\}-\([0-9]\{4\}\)$\)'  file.txt
grep -E '^\([0-9]{3}\)\s[0-9]{3}-[0-9]{4}$|^[0-9]{3}-[0-9]{3}-[0-9]{4}$' file.txt

# egrep
egrep -x '((([0-9]{3})-)|((\([0-9]{3}\)))\s)([0-9]{3})-([0-9]{4})' file.txt
