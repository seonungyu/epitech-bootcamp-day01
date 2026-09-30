#import random
#from english_words import get_english_words_set

#words = get_english_words_set(['web2'], lower=True)
#print(random.choice(list(words)))

import random
from english_words import english_words_lower_set

print(random.choice(list(english_words_lower_set)))