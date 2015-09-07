

from nltk.tokenize.regexp import RegexpTokenizer


class WordCountService():

    @classmethod
    def count(cls, text):
        return {
            "letters": cls.count_letters(text),
            "words": cls.count_words(text),
            "lines": cls.count_lines(text),
        }

    @classmethod
    def count_letters(cls, text):
        return len(text)

    @classmethod
    def count_words(cls, text):
        tokens = cls.get_word_symbols_tokens(text)
        return len(tokens)

    @classmethod
    def count_lines(cls, text):
        return text.count("\n") + 1

    @classmethod
    def get_word_tokens(cls, text):
        tokenizer = RegexpTokenizer('\w+')
        return tokenizer.tokenize(text)

    @classmethod
    def get_word_symbols_tokens(cls, text):
        tokenizer = RegexpTokenizer('\s+', gaps=True)
        return tokenizer.tokenize(text)
