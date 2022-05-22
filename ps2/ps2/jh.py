import unittest

word_to_print='_'*len(secret_word)
for i in range(len(letters_guessed)):
    if letters_guessed[i] in secret_word:
        print(letters_guessed[i])
        word_to_print=word_to_print.replace(word_to_print[i],letters_guessed[i])
return word_to_print
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
