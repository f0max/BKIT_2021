import unittest
import sys, os

sys.path.append(os.getcwd())
from bot.messages import first_state_message, second_state_message


class TestMessages(unittest.TestCase):
    def test_first_state_message(self):
        res = 'Определимся, куда нам собираться:\n' \
                      '0. Лес\n' \
                      '1. Горы\n' \
                      '2. Пустыня'
        self.assertEqual(first_state_message, res)

    def test_secon_state_message(self):
        res = 'Что возьмем с собой?\n' \
                      '0. Палатка\n' \
                      '1. Карта\n' \
                      '2. Фен'
        self.assertEqual(second_state_message, res)


if __name__ == "__main__":
    unittest.main()