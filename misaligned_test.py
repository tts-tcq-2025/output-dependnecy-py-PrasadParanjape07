import unittest
import color_map

class TestPrintColorMap(unittest.TestCase):

    def test_print_color_map_output(self):
        captured_lines = []

        def fake_output_func(line):
            captured_lines.append(line)

        result = color_map.print_color_map(fake_output_func)

        expected_lines = [
            " 0 | White  | Blue  ",
            " 1 | White  | Orange",
            " 2 | White  | Green ",
            " 3 | White  | Brown ",
            " 4 | White  | Slate ",
            " 5 | Red    | Blue  ",
            " 6 | Red    | Orange",
            " 7 | Red    | Green ",
            " 8 | Red    | Brown ",
            " 9 | Red    | Slate ",
            "10 | Black  | Blue  ",
            "11 | Black  | Orange",
            "12 | Black  | Green ",
            "13 | Black  | Brown ",
            "14 | Black  | Slate ",
            "15 | Yellow | Blue  ",
            "16 | Yellow | Orange",
            "17 | Yellow | Green ",
            "18 | Yellow | Brown ",
            "19 | Yellow | Slate ",
            "20 | Violet | Blue  ",
            "21 | Violet | Orange",
            "22 | Violet | Green ",
            "23 | Violet | Brown ",
            "24 | Violet | Slate ",
        ]

        self.assertEqual(result, 25)
        self.assertEqual(captured_lines, expected_lines)

if __name__ == "__main__":
    unittest.main()
