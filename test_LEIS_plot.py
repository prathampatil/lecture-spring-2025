import unittest
from unittest.mock import patch, mock_open
import urllib.request

# Assuming the LEIS_plot.py script is in the same directory or adjust the import accordingly
import LEIS_plot

class TestLEISPlot(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_data_extraction(self, mock_urlopen):
        # Mock the response of the urlopen function
        mock_data = "1.0 2.0\n3.0 4.0\n5.0 6.0"
        mock_urlopen.return_value.read.return_value = mock_data.encode('utf-8')

        # Reload the LEIS_plot module to apply the mock
        import importlib
        importlib.reload(LEIS_plot)

        # Check if the data was extracted correctly
        self.assertEqual(LEIS_plot.x_data, [1.0, 3.0, 5.0])
        self.assertEqual(LEIS_plot.y_data, [2.0, 4.0, 6.0])

    @patch('urllib.request.urlopen')
    def test_plotting(self, mock_urlopen):
        # Mock the response of the urlopen function
        mock_data = "1.0 2.0\n3.0 4.0\n5.0 6.0"
        mock_urlopen.return_value.read.return_value = mock_data.encode('utf-8')

        # Reload the LEIS_plot module to apply the mock
        import importlib
        importlib.reload(LEIS_plot)

        # Ensure that the script runs without errors
        try:
            LEIS_plot
        except Exception as e:
            self.fail(f"LEIS_plot script raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()