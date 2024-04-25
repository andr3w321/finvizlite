import unittest
import finvizlite as fl

class TestFinvizlite(unittest.TestCase):
    def test_rows_to_pages(self):
        self.assertEqual(fl.rows_to_pages(115), 6)
        self.assertEqual(fl.rows_to_pages(15), 1)
        self.assertEqual(fl.rows_to_pages(20), 1)
        self.assertEqual(fl.rows_to_pages(21), 2)
        self.assertEqual(fl.rows_to_pages(0), 0)

    def test_screener_overview_length(self):
        df = fl.scrape("https://finviz.com/screener.ashx?v=111")
        self.assertEqual(len(df), 20)

    def test_sp500(self):
        df = fl.scrape_all("https://finviz.com/screener.ashx?v=111&f=idx_sp500&o=-marketcap")
        self.assertGreaterEqual(len(df), 500)

    def test_all(self):
        df = fl.scrape_all("https://finviz.com/screener.ashx?v=111&o=-marketcap")
        self.assertGreaterEqual(len(df), 7000)

    def test_max_rows(self):
        df = fl.scrape_all("https://finviz.com/screener.ashx?v=111&o=-marketcap", rows=35)
        self.assertEqual(len(df), 35)

if __name__ == "__main__":
    unittest.main()
