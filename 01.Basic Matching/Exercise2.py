""" Bot or Not?
In this exercise you have to check if tweet are from bot or not 
and that's by check if "@bot" is found on the tweet
"""

# Import the necessary library
import re

# Function to check if tweet is from bot or not
def check_pattern(tweet):
    pattern = r".ot" # Add the pattern here
    if re.search(pattern, tweet):
        return True
    else:
        return False