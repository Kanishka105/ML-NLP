from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("punkt_tab")
def nltk_stemming_function(text):

    text = str(text)
    tokens = word_tokenize(text)

    # Stopword Removal
    stop_words = set(stopwords.words("english"))
    stop_words.difference_update({"not", "no", "nor", "neither", "never"})

    tokens = [
        word
        for word in tokens
        if word not in stop_words
    ]

    # Stemming
    stemmer = PorterStemmer()

    tokens = [
        stemmer.stem(word)
        for word in tokens
    ]

    return " ".join(tokens)




def get_wordnet_pos(tag):
    """
    Convert Penn Treebank POS tags to WordNet POS tags.
    """

    if tag.startswith("J"):
        return wordnet.ADJ

    elif tag.startswith("V"):
        return wordnet.VERB

    elif tag.startswith("N"):
        return wordnet.NOUN

    elif tag.startswith("R"):
        return wordnet.ADV

    return wordnet.NOUN

def nltk_lemmatization_function(text):

    text = str(text).lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))

    stop_words.difference_update({
        "not", "no", "nor", "never", "neither"
    })

    extra_stopwords = {
    "see",
    "view",
    "click",
    "today",
    "now",
    "hi",
    "hello",
    "thanks",
    "thank",
    "regards",
    "best",
    "please",
    "within",
    "one",
    "get"
    }
    stop_words.update(extra_stopwords)

    tokens = [
        word
        for word in tokens
        if word not in stop_words
    ]
    print("After Stopwords:", tokens)

    # Remove numbers
    tokens = [
        word
        for word in tokens
        if word.isalpha()
    ]
    print("After Numbers:", tokens)

    # Remove fake URLs
    remove_words = {
        "bitlyfakeprize",
        "phishingsitecom",
        "scamdeliverycom"
    }

    tokens = [
        word
        for word in tokens
        if word not in remove_words
    ]
    print("After Fake URLs:", tokens)

    # POS tagging
    tagged_tokens = pos_tag(tokens)
    print("POS:", tagged_tokens)

    lemmatizer = WordNetLemmatizer()

    processed_tokens = []

    allowed_tags = {
        "NN","NNS","NNP","NNPS",
        "JJ","JJR","JJS",
        "VB","VBD","VBG","VBN","VBP","VBZ"
    }

    for word, tag in tagged_tokens:

        if tag in allowed_tags:

            processed_tokens.append(
                lemmatizer.lemmatize(
                    word,
                    get_wordnet_pos(tag)
                )
            )

    print("Final:", processed_tokens)

    return " ".join(processed_tokens)

def nltk_summarization_preprocessing(text):

    text = str(text).lower()

    # Original sentences
    original_sentences = sent_tokenize(text)

    # Processed sentences
    processed_sentences = []

    for sentence in original_sentences:

        processed_sentence = nltk_lemmatization_function(sentence)

        processed_sentences.append(processed_sentence)

    return original_sentences, processed_sentences