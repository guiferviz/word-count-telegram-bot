

from service import WordCountService

import test_suite


class ServicesTests(test_suite.AppEngineTestBase):

    def test_count_letters_1(self):
        text = "Harry??"
        letters = WordCountService.count_letters(text)
        self.assertEqual(7, letters)

    def test_count_letters_2(self):
        text = "Voldemort\nHarry"
        letters = WordCountService.count_letters(text)
        self.assertEqual(15, letters)

    def test_get_word_tokens(self):
        text = "Hermione?? Crookshanks??? Miaaaauuu :)"
        tokens = WordCountService.get_word_tokens(text)
        self.assertEqual(3, len(tokens))

    def test_get_word_symbols_tokens(self):
        text = "Ron?? Scabbers??? Chiiii :3"
        tokens = WordCountService.get_word_symbols_tokens(text)
        self.assertEqual(4, len(tokens))

    def test_count_lines(self):
        text = "Voldemort\nHarry"
        lines = WordCountService.count_lines(text)
        self.assertEqual(2, lines)

    def test_count_1(self):
        text_1 = "Hi there!\n:)"
        result = WordCountService.count(text_1)
        self.assertEquals(result["letters"], 12)
        self.assertEquals(result["words"], 3)
        self.assertEquals(result["lines"], 2)
