"""
Add words in quotations to the "new_stopwords" list below to filter words
or characters out of the word/count output.

The lists below must follow the default format:
new_stopwords = {"word1", "word2", "word3"}
"""

new_stopwords = [".", ",", "'", "?", "I", "You", "The", "A", "’"]

"""
Use the list below to remove stopwords from the core library list.
If you remove them, they must be added again in the 'custom_stopwords.py' file.

The default nltk stopwords list can be viewed at this URL:
https://gist.github.com/sebleier/554280

This file must follow the default format:
remove_stopwords = {"word1", "word2"}
remove_stopwords = {"word1", "word2", "word3"}
"""

ignore_stopwords = {"amazing_word1", "amazined_word2", "amazined_word3"}
