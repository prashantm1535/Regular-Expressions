# Import the necessary library
import re

# Function to check if tweet is from bot or not
def check_pattern(tweet):
    pattern = r".ot" # Add the pattern here
    if re.search(pattern, tweet):
        return True
    else:
        return False