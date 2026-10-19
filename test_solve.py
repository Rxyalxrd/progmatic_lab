import unittest

from solve import find_solutions


class FindSolutionsTests(unittest.TestCase):
    def test_finds_every_expression_equal_to_200(self) -> None:
        self.assertEqual(
            set(find_solutions()),
            {
                "9-8+7-6-5-4-3+210",
                "9-8-7-6-5+4+3+210",
                "98+76-5+43-2-10",
                "98-7+65+43+2-1+0",
                "98-7+65+43+2-1-0",
            },
        )


if __name__ == "__main__":
    unittest.main()
